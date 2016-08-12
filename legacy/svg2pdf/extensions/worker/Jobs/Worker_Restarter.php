<?php

date_default_timezone_set('Europe/Ljubljana');
require_once dirname(__FILE__) . '/../../../../common/lib/Net/Gearman/Job/Common.php';

class Worker_Restarter extends Net_Gearman_Job_Common {

    public function run($arg) {
        print date("d.m.Y H:i:s") . " :: Starting dead workers...\n";
        sleep(1);
        exec("/usr/bin/php " . dirname(__FILE__) . "/../../../init-worker.sh start");
        return true;
    }

}

?>