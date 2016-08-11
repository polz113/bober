#!/usr/bin/php
<?php
define("THREADS_SVG2PDF", 10);
define("DAEMON", "/sbin/start-stop-daemon");
define("SCRIPT_WORKER_SVG2PDF", dirname(__FILE__) . '/worker_main.php');
define("RESTARTER", dirname(__FILE__) . '/extensions/worker/WorkerRestarter.php');
define("NAME_PREFIX", "phpworker");
define("PHP_CLI", "/usr/bin/php");


$args = isset($argv) ? $argv : $_SERVER['argv'];
if (array_key_exists(1, $args)) {
    $action = $args[1];
} else {
    print "Available commands: start | stop | restart\n";
    die();
}

switch ($action) {

    case "start":
        start();
        break;

    case "stop":
        stop();
        break;

    case "restart":
        stop();
        start();
        break;
}

function start() {
    exec("mkdir -p /var/run/gearman_worker");
    exec("mkdir -p /var/log/gearman_worker");
    exec(DAEMON . " -n worker_restarter -x " . PHP_CLI . " " . RESTARTER . " -b -1 /var/log/gearman_worker/workerRestarter.log -2 /var/log/gearman_worker/workerRestarter_error.log -m -p /var/run/gearman_worker/WorkerRestarter.pid");
    for ($i = 0; $i < THREADS_SVG2PDF; $i++) {
        $name = "SVG2PDF_" . NAME_PREFIX . "_" . $i;
        exec(DAEMON . " -n " . $name . " -x " . PHP_CLI . " " . SCRIPT_WORKER_SVG2PDF . " " . $i . " -b -1 /var/log/gearman_worker/svg2pdf.log -2 /var/log/gearman_worker/svg2pdf_error.log -m -p /var/run/gearman_worker/" . $name . ".pid");
    }
}

function stop() {
    for ($i = 0; $i < THREADS_SVG2PDF; $i++) {
        $name = "SVG2PDF_" . NAME_PREFIX . "_" . $i;
        exec(DAEMON . " -p /var/run/gearman_worker/" . $name . ".pid --stop");
    }
    exec(DAEMON . " -p /var/run/gearman_worker/WorkerRestarter.pid --stop");
}
?>