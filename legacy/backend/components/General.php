<?php

class General {

    /**
     * Normalno iskanje po Array-u
     *
     * @param Array		$array			Seznam
     * @param String	$key_value		Ključ iskanja
     * @param String	$search_string	Iskani niz
     * @param Integer	$count			Število elementov v seznamu
     *
     * @return Integer	Če je najden zadetek v seznamu vrne indeks elementa, drugače -1
     */
    private static function normal_search(&$array, $key_value, $search_string, $count, $trim = false) {
        if ($trim) {
            if ($array != array()) {
                if (isset($array[0])) {
                    $i = 0;
                    while ($i < $count) {
                        if (!array_key_exists($key_value, $array[$i])) {
                            print "<pre>";
                            debug_print_backtrace();
                            print "Error in general.class.php\n";
                            print "Error while searching key " . $key_value . " in array:\n";
                            print_r($array[$i]);
                            print "</pre>";
                            die();
                        }
                        if (trim($array[$i][$key_value]) == $search_string) {
                            return $i;
                        }
                        $i++;
                    }
                    return -1;
                } else {
                    $array_keys = array_keys($array);
                    $i = 0;
                    while ($i < $count) {
                        if (trim($array[$array_keys[$i]][$key_value]) == $search_string) {
                            return $array_keys[$i];
                        }
                        $i++;
                    }
                    return -1;
                }
            } else {
                return -1;
            }
        } else {
            if ($array != array()) {
                if (isset($array[0])) {
                    $i = 0;
                    while ($i < $count) {
                        if (!array_key_exists($key_value, $array[$i])) {
                            print "<pre>";
                            debug_print_backtrace();
                            print "Error in general.class.php\n";
                            print "Error while searching key " . $key_value . " in array:\n";
                            print_r($array[$i]);
                            print "</pre>";
                            die();
                        }
                        if ($array[$i][$key_value] == $search_string) {
                            return $i;
                        }
                        $i++;
                    }
                    return -1;
                } else {
                    $array_keys = array_keys($array);
                    $i = 0;
                    while ($i < $count) {
                        if ($array[$array_keys[$i]][$key_value] == $search_string) {
                            return $array_keys[$i];
                        }
                        $i++;
                    }
                    return -1;
                }
            } else {
                return -1;
            }
        }
    }

    /**
     * Normalno iskanje po Array-u brez ključa iskanja
     *
     * @param Array		$array			Seznam
     * @param String	$search_string	Iskani niz
     * @param Integer	$count			Število elementov v seznamu
     *
     * @return Integer	Če je najden zadetek v seznamu vrne indeks elementa, drugače -1
     */
    private static function normal_search_without_key_value(&$array, $search_string, $count, $trim = false) {
        if ($trim) {
            if ($array != array()) {
                if (isset($array[0])) {
                    $i = 0;
                    while ($i < $count) {
                        if (trim($array[$i]) == $search_string) {
                            return $i;
                        }
                        $i++;
                    }
                    return -1;
                } else {
                    $array_keys = array_keys($array);
                    $i = 0;
                    while ($i < $count) {
                        if (trim($array[$array_keys[$i]]) == $search_string) {
                            return $array_key[$i];
                        }
                    }
                    return -1;
                }
            } else {
                return -1;
            }
        } else {
            if ($array != array()) {
                if (isset($array[0])) {
                    $i = 0;
                    while ($i < $count) {
                        if ($array[$i] == $search_string) {
                            return $i;
                        }
                        $i++;
                    }
                    return -1;
                } else {
                    $array_keys = array_keys($array);
                    $i = 0;
                    while ($i < $count) {
                        if ($array[$array_keys[$i]] == $search_string) {
                            return $array_key[$i];
                        }
                    }
                    return -1;
                }
            } else {
                return -1;
            }
        }
    }

    /**
     * Binarno iskanje po Array-u s ključem iskanja
     *
     * @param Array		$array			Seznam
     * @param String	$key_value		Ključ iskanja
     * @param String	$search_string	Iskani niz
     * @param Integer	$min			Spodnja meja
     * @param Integer	$max			Zgornja meja
     *
     * @return Integer	Če je najden zadetek v seznamu vrne indeks elementa, drugače -1
     */
    private static function binary_search(&$array, $key_value, $search_string, $min, $max) {
        while ($max - $min > 1) {
            $polovicka = ceil(($min + $max) / 2);
            if ($array[$polovicka][$key_value] == $search_string) {
                return $polovicka;
            } elseif ($array[$polovicka][$key_value] < $search_string) {
                $min = $polovicka;
            } else {
                $max = $polovicka;
            }
        }
        if ($array[0][$key_value] == $search_string) {
            return 0;
        } elseif ($array[$max][$key_value] == $search_string) {
            return $max;
        } else {
            return -1;
        }
    }

    /**
     * Binarno iskanje po Array-u brez ključa iskanja
     *
     * @param Array		$array			Seznam
     * @param String	$search_string	Iskani niz
     * @param Integer	$min			Spodnja meja
     * @param Integer	$max			Zgornja meja
     *
     * @return Integer	Če je najden zadetek v seznamu vrne indeks elementa, drugače -1
     */
    private static function binary_search_without_key_value(&$array, $search_string, $min, $max) {
        while ($max - $min > 1) {
            $polovicka = ceil(($min + $max) / 2);
            if ($array[$polovicka] == $search_string) {
                return $polovicka;
            } elseif ($array[$polovicka] < $search_string) {
                $min = $polovicka;
            } else {
                $max = $polovicka;
            }
        }
        if ($array[0] == $search_string) {
            return 0;
        } elseif ($array[$max] == $search_string) {
            return $max;
        } else {
            return -1;
        }
    }

    /**
     * Pametno iskanje po seznamu, funkcija se sama odloči kako bo iskala po seznamu
     *
     * @param Array		$array			Seznam
     * @param String	$key_value		Ključ iskanja
     * @param String	$search_string	Iskani niz
     * @param Boolean	$sorted			Če je seznam že urejen nastavi True, drugače False, privzeto False
     *
     * @return Integer	Če je najden zadetek v seznamu vrne indeks elementa, drugače -1
     */
    public static function search_in_array(&$array, $key_value, $search_string, $sorted = false, $trim = false) {
        $count = count($array);
        if ($sorted) {
            if ($key_value != "") {
                if ($count < 50) {
                    return self::normal_search($array, $key_value, $search_string, $count, $trim);
                } else {
                    return self::binary_search($array, $key_value, $search_string, 0, $count);
                }
            } else {
                if ($count < 50) {
                    return self::normal_search_without_key_value($array, $search_string, $count, $trim);
                } else {
                    return self::binary_search_without_key_value($array, $search_string, 0, $count);
                }
            }
        } else {
            if ($key_value != "") {
                return self::normal_search($array, $key_value, $search_string, $count, $trim);
            } else {
                return self::normal_search_without_key_value($array, $search_string, $count, $trim);
            }
        }
    }

    /**
     * Naključni hash
     *
     * @param Integer	$length		Dolžina hasha, privzeto 100
     *
     * @return String	Vrne nek random hash
     */
    public static function random_hash($length = 100, $charsString = '') {
        $hash = "";
        if ($charsString == '') {
            $chars = "abcdefghijklmnoprstuvzxy1234567890";
        }else{
            $chars = $charsString;
        }
        $chars_length = strlen($chars) - 1;
        for ($i = 0; $i < $length; $i++) {
            $hash .= $chars[mt_rand(0, $chars_length)];
        }
        return $hash;
    }

    /**
     * Besedilo spremni v male črke in naredi veliko začetnico samo pri prvi besedi
     *
     * @param String	$string		Besedilo
     * @param String	$e			Enkdoiranje besedila (privzeto: UTF-8)
     *
     * @return String				Spremenjeno besedilo
     */
    public static function mb_ucfirst($string, $e = 'utf-8') {
        if (function_exists('mb_strtoupper') && function_exists('mb_substr') && !empty($string)) {
            $string = mb_strtolower($string, $e);
            $upper = mb_strtoupper($string, $e);
            preg_match('#(.)#us', $upper, $matches);
            $string = $matches[1] . mb_substr($string, 1, mb_strlen($string, $e), $e);
        } else {
            $string = ucfirst($string);
        }
        return $string;
    }

    public static function remove_non_ascii_chars($msg) {
        $chars = array(
            "č" => "c",
            "Č" => "C",
            "ž" => "z",
            "Ž" => "Z",
            "š" => "s",
            "Š" => "S",
            "đ" => "dz",
            "Đ" => "Dz",
            "ö" => "o",
            "Ö" => "O",
            "ü" => "u",
            "Ü" => "U",
            "ä" => "a",
            "Ä" => "A"
        );
        $keys = array_keys($chars);
        for ($i = 0; $i < count($chars); $i++) {
            $msg = str_replace($keys[$i], $chars[$keys[$i]], $msg);
        }
        // remove all other non ascii without transformation
        $msg = preg_replace('/[^(\x20-\x7F)]*/', '', $msg);
        return $msg;
    }

    /**
     * Primerjava vseh vrednosti v prvem arrayu z vrednostmi v drugem arrayu
     * 
     * @param Array $array1
     * @param Array $array2
     * @param Array $defined_keys
     *
     * @return boolean Če se vse vrednost po ključih prvega arraya ujemajo z drugim arrayom vrne True, drugače False
     */
    public static function compare_array_key_values($array1, $array2, $defined_keys = array()) {
        if (count($defined_keys) > 0) {
            $keys = $defined_keys;
        } else {
            $keys = array_keys($array1);
        }
        for ($i = 0; $i < count($keys); $i++) {
            if (array_key_exists($keys[$i], $array2)) {
                if (is_array($array1[$keys[$i]])) {
                    if (!self::compare_array_key_values($array1[$keys[$i]], $array2[$keys[$i]])) {
                        return false;
                    }
                } else {
                    if ($array1[$keys[$i]] != $array2[$keys[$i]]) {
                        return false;
                    }
                }
            } else {
                return false;
            }
        }
        return true;
    }

}

// print_r(general::random_hash());

/* test cases
  $array = array();
  for ($i = 0; $i < 100; $i++) {
  $array[] = array("id" => $i);
  }
  print_r(general::search_in_array($array, "id", "150", 0) . "\n");

  $m = 0;
  $win_2 = 0;
  $win_3 = 0;
  while ($m < 100) {
  $k = 50;
  do {
  $array = array();
  for ($i = 0; $i < $k; $i++) {
  $array[] = $i;
  }

  $searched_number = rand(0, $k-1);

  $time_start = microtime(true);
  $value_2 = general::normal_search_without_key_value($array, $searched_number, $k);
  $time_end = microtime(true);
  $time_2 = $time_end - $time_start;
  // echo "Executing time: ".$time_2." seconds\n";

  $time_start = microtime(true);
  $value_3 = general::binary_search_without_key_value($array, $searched_number, 0, $k);
  $time_end = microtime(true);
  $time_3 = $time_end - $time_start;
  // echo "Executing time: ".$time_3." seconds\n";

  if ($time_2 < $time_3) {
  $win_2++;
  }else{
  $win_3++;
  }

  $k++;
  }while ($k < 100);
  $m++;
  }
  print_r("Normal search wins: ".$win_2."\n");
  print_r("Binary search wins: ".$win_3."\n");
 */
?>