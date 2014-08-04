<?php

date_default_timezone_set('Europe/Ljubljana');
require_once dirname(__FILE__) . '/../../../../common/lib/Net/Gearman/Job/Common.php';

class AllClasses extends Net_Gearman_Job_Common {

    public function run($arg) {
        try {
            $arg = unserialize(base64_decode($arg));
            if (!isset($arg['class']) || !isset($arg['function'])) {
                return array('result' => array('done' => false, 'job_id' => -1), 'WorkerJobSetIdentifier' => isset($arg['WorkerJobSetIdentifier']) ? $arg['WorkerJobSetIdentifier'] : -1, 'background' => isset($arg['background']) ? $arg['background'] : -1);
            }
            $log = $arg["class"] . '::' . $arg["function"];
            if (defined('THREAD') && defined('THREAD_TYPE')) {
                print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
            }
            $task_id = $arg['task_id'];
            $Job = Job::model()->find('id=:id', array(':id' => $task_id));
            if ($Job == null) {
                $Job = new Job();
                return null;
            }
            $Job->started = 1;
            $Job->starttime = date('Y-m-d H:i:s');
            $Job->save();
            $tmp = $this->runClassFunction($arg["class"], $arg["function"], $arg["params"]);
            $done = false;
            if ($tmp != null) {
                $Job->parameters = null;
                $Job->result = base64_encode(serialize($tmp));
                $Job->finishtime = date('Y-m-d H:i:s');
                $Job->save();
                $Job->finished = 1;
                $Job->save();
                $done = true;
            }
        } catch (CDbException $e) {
            if (function_exists('thread_shutdown')) {
                thread_shutdown();
            }
            die();
        }
        $log = $arg["class"] . '::' . $arg["function"] . ' :: DONE';
        if (defined('THREAD') && defined('THREAD_TYPE')) {
            print date('d.m.Y H:i:s') . ' :: ' . THREAD_TYPE . ' Thread :: ' . str_pad(THREAD, 3, '0', STR_PAD_LEFT) . ' :: ' . $log . "\n";
        }
        return array('result' => array('done' => $done, 'job_id' => $Job->id), 'WorkerJobSetIdentifier' => $arg['WorkerJobSetIdentifier'], 'background' => $arg['background']);
    }

    public function runClassFunction($class, $function, $params) {
        if (is_callable($class . "::" . $function)) {
            return call_user_func_array($class . "::" . $function, $params);
        } else {
            return null;
        }
    }

}

?>