<?php

define('NET_GEARMAN_JOB_CLASS_PREFIX', '');
define('NET_GEARMAN_JOB_PATH', dirname(__FILE__) . "/Jobs");

class WorkerDaemon extends CApplicationComponent implements IWorkerDaemon {

    private $_worker;

    /**
     * Constructor.
     */
    public function __construct() {
        include_once dirname(__FILE__).'/../../../common/lib/Net/Gearman/Connection.php';
        include_once dirname(__FILE__).'/../../../common/lib/Net/Gearman/Worker.php';
        $this->_worker = new Net_Gearman_Worker(array('127.0.0.1:4730'));
    }

    /**
     * Start run worker. Before run, method automatically set active to true.
     *
     * If need stop worker, code must call setActive(false), and worker stops after work cycle end.
     */
    public function run() {
        $worker = $this->_worker;
        $worker->addAbility('AllClasses');
        $worker->beginWork();
    }

}
