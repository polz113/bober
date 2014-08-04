<?php

/*
 * Register zavodov Slovenije je spletni servis, ki omogoča pridobiti vse podatke
 * o vseh izobraževalnih zavodih v Sloveniji
 * 
 * Uradna stran: https://paka1.mss.edus.si/WebServices/RegZavod/RegZavodServicePort
 * WSDL url: https://paka1.mss.edus.si/WebServices/RegZavod/RegZavodServicePort?wsdl
 */

/**
 * Description of RegisterZavodov
 *
 * @author Dean Gostiša <dean@black.si>
 */
class RegisterZavodov {

    public static function GetRegZavod() {
        $debug = false;
        $wsdl_url = dirname(__FILE__) . '/RegZavodServicePort.wsdl';
        if (!file_exists($wsdl_url)) {
            echo 'Missing WSDL shema for RegZavodServicePort.wsdl', "\n";
            echo 'WSDL PATH: ', $wsdl_url, "\n";
            die();
        }
        $client = new SoapClient($wsdl_url, array('exceptions' => 0, 'trace' => 1, 'user_agent' => 'Bober'));
        $result = $client->__soapCall('getRegZavod', array());
        if ($debug) {
            var_dump($client->__getFunctions());
            echo 'REQUEST HEADERS:', "\n", $client->__getLastRequestHeaders(), "\n";
            echo 'REQUEST:', "\n", $client->__getLastRequest(), "\n";
            var_dump($result);
            if (is_soap_fault($result)) {
                trigger_error('SOAP Fault: (faultcode: {$result->faultcode}, faultstring: {$result->faultstring})', E_USER_ERROR);
            }
            print_r($result);
        }
        if ($result != '' && !is_soap_fault($result)) {
            $result = json_decode(json_encode($result), true);
            return $result;
        } else {
            return array();
        }
    }

    public static function GetRegZavodProgHoriz($zavod_prs, $solsko_leto = '') {
        include_once dirname(__FILE__) . '/../CurlTool.php';
        if ($solsko_leto == '') {
            if (date('m') >= 9 && date('m') <= 12) {
                $solsko_leto = date('Y') . '/' . (date('Y') + 1);
            } else {
                $solsko_leto = (date('Y') - 1) . '/' . date('Y');
            }
        }
        $debug = true;
        $headers = array('Content-Type: text/xml; charset=utf-8', 'SOAPAction: \'https://paka1.mss.edus.si:443/WebServices/RegZavod/RegZavodServicePort\'');
        $curl = new curlTool(false, false, array(), $headers);
        $xml = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:si="http://si.edu.mss.si/">' . "\n";
        $xml .= "\t" . '<soapenv:Header/>' . "\n";
        $xml .= "\t" . '<soapenv:Body>' . "\n";
        $xml .= "\t\t" . '<si:getRegZavodProgHoriz>' . "\n";
        $xml .= "\t\t\t" . '<SOLSKO_LETO_NAZIV>' . $solsko_leto . '</SOLSKO_LETO_NAZIV>' . "\n";
        $xml .= "\t\t\t" . '<ZAVOD_PRS>' . $zavod_prs . '</ZAVOD_PRS>' . "\n";
        $xml .= "\t\t" . '</si:getRegZavodProgHoriz>' . "\n";
        $xml .= "\t" . '</soapenv:Body>' . "\n";
        $xml .= '</soapenv:Envelope>';
        // echo 'XML request:', "\n", $xml, "\n\n";
        $result = $curl->fetchContent('https://paka1.mss.edus.si:443/WebServices/RegZavod/RegZavodServicePort', false, $xml);
        // print_r($result . "\n\n");
        $explode = explode('<ns2:getRegZavodProgHorizResponse xmlns:ns2="http://si.edu.mss.si/">', $result);
        $explode = explode('</ns2:getRegZavodProgHorizResponse>', $explode[1]);
        $result = '<document>' . $explode[0] . '</document>';
        libxml_use_internal_errors(true);
        $doc = simplexml_load_string($result);
        $doc = json_decode(json_encode($doc), true);
        $result = $doc['return'];
        $curl->cleanup();
        return $result;
    }

    public static function GetZavodInfo($solsko_leto = '', $zavod_naziv = '', $zavprs = '') {
        $list = self::GetRegZavod();
        include_once dirname(__FILE__) . '/../General.php';
        if ($zavod_naziv != '') {
            $found_id = General::search_in_array($list['return'], 'ZAVOD_NAZIV', $zavod_naziv, false, true);
        } else {
            $found_id = General::search_in_array($list['return'], 'ZAVPRS', $zavprs);
        }
        if ($found_id != -1) {
            $list['return'][$found_id]['programi'] = self::GetRegZavodProgHoriz($list['return'][$found_id]['ZAVPRS'], $solsko_leto);
            return $list['return'][$found_id];
        } else {
            return array();
        }
    }
    
    public static function GetZavodiKategorije() {
        $list = self::GetRegZavod();
        if (!isset($list['return'])) {
            return array();
        }
        $kategorija = array();
        $list = $list['return'];
        $count = count($list);
        for ($i = 0; $i < $count; ++$i) {
            if (!in_array(trim($list[$i]['KATEGORIJA']), $kategorija)) {
                $kategorija[] = trim($list[$i]['KATEGORIJA']);
            }
        }
        return $kategorija;
    }
    
    public static function SyncZavodiKategorije() {
        $kategorije = self::GetZavodiKategorije();
        for ($i = 0; $i < count($kategorije); ++$i) {
            $schoolCategory = SchoolCategory::model()->find('name=:name', array(':name' => $kategorije[$i]));
            if ($schoolCategory == null) {
                $schoolCategory = new SchoolCategory();
                $schoolCategory->name = $kategorije[$i];
                $schoolCategory->save();
            }
        }
    }
    
    public static function SyncZavodiWhereKategorijaActive() {
        $schoolCategories = SchoolCategory::model()->findAll('active=:active', array(':active' => 1));
        $kategorije = array();
        $kategorija_map = array();
        foreach ($schoolCategories as $schoolCategory) {
            $kategorije[] = $schoolCategory->name;
            $kategorija_map[$schoolCategory->name] = $schoolCategory->id;
        }
        echo "Current categories for sync:<br />";
        pre_print($kategorije);
        $list = self::GetRegZavod();
        if (!isset($list['return'])) {
            return array();
        }
        $list = $list['return'];
        echo "Current schools to sync:<br />";
        $country = Country::model()->find('country=:country', array(':country' => 'Slovenija'));
        if ($country == null) {
            echo "Add country Slovenija!<br />\n";
            die();
        }
        $country_id = $country->id;
        
        // cache all občine
        $municipalities = Municipality::model()->findAll('country_id=:country_id', array(':country_id' => $country_id));
        $municipality_map = array();
        foreach ($municipalities as $municipality) {
            $municipality_map[$municipality->name] = $municipality->id;
        }
        
        // cache all regije
        $regions = Region::model()->findAll('country_id=:country_id', array(':country_id' => $country_id));
        $region_map = array();
        foreach ($regions as $region) {
            $region_map[$region->name] = $region->id;
        }
        $counter = 0;
        $updated = 0;
        $inserted = 0;
        for ($i = 0; $i < count($list); ++$i) {
            if (in_array($list[$i]['KATEGORIJA'], $kategorije)) {
                $counter++;
                $el = $list[$i];
                $school = School::model()->find('name=:name and country_id=:country_id', array(':name' => trim($el['ZAVOD_NAZIV']), ':country_id' => $country_id));
                if ($school == null) {
                    $school = new School();
                    $school->name = trim($el['ZAVOD_NAZIV']);
                    $school->country_id = $country_id;
                    $inserted++;
                }
                $school->school_category_id = $kategorija_map[trim($el['KATEGORIJA'])];
                // občina
                if (!isset($municipality_map[trim($el['OBCINANAZIV'])])) {
                    $municipality = new Municipality();
                    $municipality->name = trim($el['OBCINANAZIV']);
                    $municipality->country_id = $country_id;
                    $municipality->save();
                    $municipality_map[trim($el['OBCINANAZIV'])] = $municipality->id;
                }
                $school->municipality_id = $municipality_map[trim($el['OBCINANAZIV'])];
                // regija
                if (!isset($region_map[trim($el['REGIJANAZIV'])])) {
                    $region = new Region();
                    $region->name = trim($el['REGIJANAZIV']);
                    $region->country_id = $country_id;
                    $region->save();
                    $region_map[trim($el['REGIJANAZIV'])] = $region->id;
                }
                $school->region_id = $region_map[trim($el['REGIJANAZIV'])];
                $school->post = trim($el['POSTANAZIV']);
                $school->postal_code = trim($el['POSTASIFRA']);
                $school->identifier = trim($el['ZAVPRS']);
                $school->headmaster = trim($el['ZAVRAVN']);
                if (isset($el['ZAVDAVST'])) {
                    $school->tax_number = trim($el['ZAVDAVST']);
                }
                if ($school->save()) {
                    $updated++;
                }
            }
        }
        echo 'Found schools to sync: ', $counter, "<br />\n";
        echo 'New schools imported: ', $inserted, "<br />\n";
        echo 'Updated schools: ', ($updated-$inserted), "<br />\n";
    }
    

}
//header('Content-Type: text/html; charset=utf-8');
//// pre_print(RegisterZavodov::SyncZavodiKategorije());
//pre_print(RegisterZavodov::SyncZavodiWhereKategorijaActive());
?>