<?php

class DiagnosticsController extends Controller {

    public function actionIndex() {
        echo 'Current date: ', date('Y-m-d H:i:s'), '<br />';
        echo 'Current MySQL date: ', $this->checkMysqlTime(), '<br />';
        echo 'Server software: ', isset($_SERVER['SERVER_SOFTWARE']) ? $_SERVER['SERVER_SOFTWARE'] : '/', '<br />';
        echo 'PHP version: ', PHP_VERSION, '<br />';
        echo 'PHP MySQL Client version: ', $this->checkMysqlClientVersion(), '<br />';
        echo 'MySQL Server version: ', $this->checkMysqlServerVersion(), '<br />';
        echo 'Memcached: ', class_exists('Memcache', false) || class_exists('Memcached', false) ? 'OK' : '<span style="color:red;">Missing</span>', '<br />';
        echo 'Memcached server: ', $this->checkMemcache() ? 'OK' : '<span style="color:red;">NOT AVAILABLE</span>', '<br />';
        die();
    }

    function checkMemcache() {
        $memCache = new \Memcache();
        $memCache->addServer('127.0.0.1', 11211);
        $stats = @$memCache->getExtendedStats();
        $available = (bool) $stats['127.0.0.1:11211'];
        if ($available && $memCache->connect('127.0.0.1', 11211) !== false) {
            return true;
        }
        return false;
    }

    function checkMysqlTime() {
        $mysqli = new mysqli("127.0.0.1", "bober", "YaB2sQR346VbNcee", "bober", 3307);

        /* check connection */
        if (mysqli_connect_errno()) {
            printf("Connect failed: %s\n", mysqli_connect_error());
            exit();
        }

        if ($result = $mysqli->query("select now()")) {
            while ($row = $result->fetch_row()) {
                return $row[0];
            }
            $result->close();
        }
        return -1;
    }

    function checkMysqlClientVersion() {
        $mysqli = new mysqli("127.0.0.1", "bober", "YaB2sQR346VbNcee", "bober", 3307);

        /* check connection */
        if (mysqli_connect_errno()) {
            printf("Connect failed: %s\n", mysqli_connect_error());
            exit();
        }

        return mysqli_get_client_version($mysqli);
    }

    function checkMysqlServerVersion() {
        $mysqli = new mysqli("127.0.0.1", "bober", "YaB2sQR346VbNcee", "bober", 3307);

        /* check connection */
        if (mysqli_connect_errno()) {
            printf("Connect failed: %s\n", mysqli_connect_error());
            exit();
        }

        return mysqli_get_server_version($mysqli);
    }

}

?>