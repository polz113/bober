<?php

require_once "Interfaces.php";

class WorkerApplication extends CApplication implements IWorkerApplication {

    /**
     * @return string the ID of the default controller. Defaults to 'worker'.
     */
    public $defaultController = 'worker';
    public $workerRestartOnError = true;

    /**
     * initialization
     */
    protected function init() {
        register_shutdown_function(array($this, 'onShutdownHandler'));
        parent::init();
    }

    /**
     * shutdown handler
     * @return void
     *
     */
    public function onShutdownHandler() {
        if ($e = error_get_last()) {
            if (defined("THREAD") && defined("THREAD_TYPE")) {
                require_once dirname(__FILE__) . '/../../../common/lib/Net/Gearman/Client.php';
                print date("d.m.Y H:i:s") . " :: " . THREAD_TYPE . " Thread :: " . str_pad(THREAD, 3, "0", STR_PAD_LEFT) . " :: Starting workers restart...\n";
                $set = new Net_Gearman_Set();
                $task = new Net_Gearman_Task("Worker_Restarter", 1);
                $task->type = Net_Gearman_Task::JOB_BACKGROUND;
                $set->addTask($task);
                $client = new Net_Gearman_Client(array('127.0.0.1:4730'));
                $client->runSet($set);
            }
            $this->raiseEvent('onEndRequest', new CEvent($this));
        }
    }

    /**
     * Start worker cycle.
     * To add custom route rules you can add in at worker.
     * <code>
     *
     * // add callback in php5.3 style
     * $app->getWorker()->setCommand("commandName", function($job){
     *      $job->setReturn($data->getMessage());
     * });
     *
     * // add callback as
     * $app->getWorker()->setCommand("commandName", array("controllerId", "action"));
     * </code>
     */
    public function processRequest() {
        $worker = $this->getWorker();

        $worker->run();
    }

    /**
     * Get worker daemon component.
     * Also you can call $app->getComponent("worker") or $app->worker.
     * 
     * @return IWorkerDaemon
     */
    public function getWorker() {
        return $this->getComponent("worker");
    }

    /**
     * Set worker daemon component.
     * Also you can call $app->setWorker("router", $component) or $app->router = $component.
     *
     * @param mixed $worker
     * @see setComponent
     */
    public function setWorker($worker) {
        $this->setComponent("worker", $worker);
    }

    /**
     * Displays the captured PHP error.
     * This method displays the error in console mode when there is
     * no active error handler.
     * @param integer $code error code
     * @param string $message error message
     * @param string $file error file
     * @param string $line error line
     */
    public function displayError($code, $message, $file, $line) {
        echo "PHP Error[$code]: $message\n";
        echo "    in file $file at line $line\n";
        $trace = debug_backtrace();
        // skip the first 4 stacks as they do not tell the error position
        if (count($trace) > 4)
            $trace = array_slice($trace, 4);
        foreach ($trace as $i => $t) {
            if (!isset($t['file']))
                $t['file'] = 'unknown';
            if (!isset($t['line']))
                $t['line'] = 0;
            if (!isset($t['function']))
                $t['function'] = 'unknown';
            echo "#$i {$t['file']}({$t['line']}): ";
            if (isset($t['object']) && is_object($t['object']))
                echo get_class($t['object']) . '->';
            echo "{$t['function']}()\n";
        }
    }

    /**
     * Displays the uncaught PHP exception.
     * This method displays the exception in console mode when there is
     * no active error handler.
     * @param Exception $exception the uncaught exception
     */
    public function displayException($exception) {
        if (YII_DEBUG) {
            echo get_class($exception) . "\n";
            echo $exception->getMessage() . ' (' . $exception->getFile() . ' : ' . $exception->getLine() . "\n";
            echo $exception->getTraceAsString() . "\n";
        } else {
            echo get_class($exception) . "\n";
            echo $exception->getMessage() . "\n";
        }
    }

    /**
     * Registers the core application components.
     * This method overrides the parent implementation by registering additional core components.
     * @see setComponents
     */
    protected function registerCoreComponents() {
        parent::registerCoreComponents();

        $components = array(
            'worker' => array(
                'class' => 'WorkerDaemon',
            ),
        );

        $this->setComponents($components);
    }

}
