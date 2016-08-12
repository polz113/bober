<?php

class CurlTool {

    private static $options = array(
        // CURLOPT_USERAGENT => "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; Tablet PC 2.0)",
        // CURLOPT_USERAGENT => "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        CURLOPT_AUTOREFERER => false,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_CRLF => false,
        CURLOPT_HEADER => false,
        // CURLOPT_ENCODING => 'gzip, deflate',
        CURLOPT_TIMEOUT => 30,
        CURLOPT_FORBID_REUSE => false,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_VERBOSE => false
    );
    private static $proxyServers = array("127.0.0.1:8118");
    private static $proxyCount = 1;
    private static $currentProxyIndex = 0;
    private $tmp_cookie_jar;
    public $curl;
    public $useProxy = false;

    public function __construct($verbose = false, $useProxy = false, $options = array(), $headers = array()) {
        $this->tmp_cookie_jar = tempnam(sys_get_temp_dir(), 'cookie_jar');
        if (($this->curl = curl_init()) == false) {
            throw new Exception("curl_init error no function");
        }
        $this->useProxy = $useProxy;
        if ($this->useProxy) {
            if (self::$proxyCount > 0) {
                $proxy = self::$proxyServers[self::$currentProxyIndex++ % self::$proxyCount];
                curl_setopt($this->curl, CURLOPT_PROXY, $proxy);
                if ($verbose === true) {
                    print "Using proxy: $proxy ...\n";
                }
            } else if ($verbose === true) {
                print "Not using proxy ...\n";
            }
        }
        curl_setopt($this->curl, CURLOPT_COOKIEFILE, $this->tmp_cookie_jar);
        curl_setopt($this->curl, CURLOPT_COOKIEJAR, $this->tmp_cookie_jar);
        $keys = array_keys($options);
        for ($i = 0; $i < count($keys); $i++) {
            self::$options[$keys[$i]] = $options[$keys[$i]];
        }
        curl_setopt_array($this->curl, self::$options);
        if ($headers != array()) {
            curl_setopt($this->curl, CURLOPT_HTTPHEADER, $headers);
        }
    }
    
    public function cleanup() {
        if (file_exists($this->tmp_cookie_jar)) {
            unlink($this->tmp_cookie_jar);
        }
        if ($this->curl != null) {
            curl_close($this->curl);
            unset($this->curl);
            $this->curl = null;
        }
    }

    public function __destruct() {
        $this->cleanup();
    }

    public static function addProxyServer($url) {
        self::$proxyServers[] = $url;
        ++self::$proxyCount;
    }

    public function fetchContent($url, $verbose = false, $post = array()) {
        if ($verbose) {
            print "Accessing: " . $url . "\n";
        }
        curl_setopt($this->curl, CURLOPT_URL, $url);
        if ($post != array()) {
            $custom = false;
            if ($custom) {
                curl_setopt($this->curl, CURLOPT_CUSTOMREQUEST, 'POST');
            }else{
                curl_setopt($this->curl, CURLOPT_POST, true);
                curl_setopt($this->curl, CURLOPT_POSTFIELDS, $post);
            }
        }
        $host_explode = explode("/", str_replace("//", "/", $url));

        $content = curl_exec($this->curl);
        if ($this->useProxy) {
            $counter = 10;
            while ($counter > 0 && $content === false) {
                print_r(shell_exec("/etc/init.d/tor restart"));
                $content = curl_exec($this->curl);
                $counter--;
            }
        }
        curl_setopt($this->curl, CURLOPT_REFERER, $url);
        if ($content === false) {
            throw new Exception("curl_exec error for url $url.");
        }
        if ($verbose === true) {
            echo "Done.\n";
        }
        return $content;
    }

    public function downloadContent($url, $filename, $verbose = false) {
        if ($filename == "") {
            die("No filename set!\n");
        }
        $curl = &$this->curl;
        curl_setopt($curl, CURLOPT_URL, $url);
        $host_explode = explode("/", str_replace("//", "/", $url));
        $host = $host_explode[1];
        $fp = fopen($filename, 'w+');
        curl_setopt($curl, CURLOPT_FILE, $fp);
        curl_setopt($curl, CURLOPT_BINARYTRANSFER, true);
        $content = curl_exec($curl);
        // curl_setopt($curl, CURLOPT_FILE, $fp);
        curl_setopt($curl, CURLOPT_BINARYTRANSFER, false);
        if ($content === false) {
            throw new Exception("curl_exec error for url $url.");
        }
        fclose($fp);
        if ($verbose === true) {
            echo "Done.\n";
        }
        return true;
    }

}

// $curl = new curlTool();
// print_r($curl->fetchContent("http://einstein.black.si/headers.php", true));
// print_r($curl->downloadContent("http://itm.siol.net/_siol/_svc/tv/48x48/SLO1.gif", "/tmp/nekaj.gif", true));
?>