<?php

$yii = dirname(__FILE__) . '/../common/lib/yii/yii.php';
$config = dirname(__FILE__) . '/config/worker.php';

require_once ($yii);
require_once (dirname(__FILE__) . "/extensions/worker/WorkerApplication.php");

if (count($_SERVER["argv"]) > 1) {
    define("THREAD", $_SERVER["argv"][1]);
} else {
    define("THREAD", "xxx");
}
define("THREAD_TYPE", "SVG2PDF");
print "SVG2PDF Worker " . str_pad(THREAD, 3, "0", STR_PAD_LEFT) . " started...\n";

function thread_shutdown() {
    $isError = false;
    if ($error = error_get_last()) {
        switch ($error['type']) {
            case E_ERROR:
            case E_CORE_ERROR:
            case E_COMPILE_ERROR:
            case E_USER_ERROR:
                $isError = true;
                break;
        }
    }
    if ($isError) {
        date_default_timezone_set('Europe/Ljubljana');
        if (defined("THREAD") && defined("THREAD_TYPE")) {
            print date("d.m.Y H:i:s") . " :: " . THREAD_TYPE . " Thread :: " . str_pad(THREAD, 3, "0", STR_PAD_LEFT) . " :: Script execution halted ({$error['message']})\n";
        } else {
            print date("d.m.Y H:i:s") . " :: Script execution halted ({$error['message']})\n";
        }
        if (defined("THREAD") && defined("THREAD_TYPE")) {
            require_once dirname(__FILE__).'/../common/lib/Net/Gearman/Client.php';
            print date("d.m.Y H:i:s") . " :: " . THREAD_TYPE . " Thread :: " . str_pad(THREAD, 3, "0", STR_PAD_LEFT) . " :: Starting workers restart...\n";
            $set = new Net_Gearman_Set();
            $task = new Net_Gearman_Task("Worker_Restarter", 1);
            $task->type = Net_Gearman_Task::JOB_BACKGROUND;
            $set->addTask($task);
            $client = new Net_Gearman_Client(array('127.0.0.1:4730'));
            $client->runSet($set);
        }
    }
}

register_shutdown_function('thread_shutdown');

Yii::createApplication("WorkerApplication", $config)->run();

?>