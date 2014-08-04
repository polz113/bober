<?php

define('NET_GEARMAN_JOB_CLASS_PREFIX', '');
define('NET_GEARMAN_JOB_PATH', dirname(__FILE__) . "/Jobs");

include_once dirname(__FILE__) . '/../../../common/lib/Net/Gearman/Connection.php';
include_once dirname(__FILE__) . '/../../../common/lib/Net/Gearman/Worker.php';

$worker = new Net_Gearman_Worker(array('127.0.0.1:4730')); // port 7003 is standard, you can add more jobservers with array('localhost:7003','localhost:7004')
$worker->addAbility('Worker_Restarter'); // make job "Redovalnica" available at this worker
$worker->beginWork();
?>