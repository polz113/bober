<?php

require_once(dirname(__FILE__) . '/../../../common/lib/Net/Gearman/Client.php');

class WorkerJobSet {

    private $taskList;
    private $randomHash = '';
    private $jobCounter = 0;
    public $results = array();
    private $JobSet;
    private $background = false;
    private $auto_destroy_results = false;

    public function __construct($background = false, $auto_destroy_results = true) {
        $this->background = $background;
        $this->auto_destroy_results = $auto_destroy_results;
        $hash_ok = false;
        do {
            $this->randomHash = self::generateRandomString(25);
            $job_set = JobSet::model()->find('hash=:hash', array(':hash' => $this->randomHash));
            if ($job_set == null) {
                $hash_ok = true;
            }
        } while (!$hash_ok);

        $this->JobSet = new JobSet();
        $this->JobSet->hash = $this->randomHash;
        $this->JobSet->needed = 1;
        $this->JobSet->save();

        $this->taskList = new Net_Gearman_Set();
        $this->jobCounter = 0;
        global $WorkerJobSetResults;
        if (!isset($WorkerJobSetResults)) {
            $WorkerJobSetResults = array();
        }
        $WorkerJobSetResults[$this->randomHash] = array();
        $this->results = array();
    }

    public function addTask($class, $function, $params = array()) {
        $Job = new Job();
        $Job->job_set_id = $this->JobSet->id;
        $Job->enqueue = date('Y-m-d H:i:s');
        $Job->timeout = 30;
        $Job->needed = 1;
        if ($Job->save()) {
            $task_id = $Job->id;
            $parameters = array(
                'class' => $class,
                'function' => $function,
                'params' => $params,
                'WorkerJobSetIdentifier' => $this->randomHash,
                'task_id' => $task_id,
                'background' => $this->background
            );
            $Job->parameters = base64_encode(serialize($parameters));
            $Job->save();
            $task = new Net_Gearman_Task('AllClasses', $Job->parameters, $this->randomHash . $task_id);
            if ($this->background) {
                $task->type = Net_Gearman_Task::JOB_BACKGROUND;
            }

            $task->attachCallback('WorkerJobSetReturnResult');
            $this->taskList->addTask($task);
            $this->jobCounter++;
            return $Job->id;
        }else{
            return -1;
        }
    }

    public function run() {
        $client = new Net_Gearman_Client(array('localhost:4730'));
        $this->JobSet->starttime = date('Y-m-d H:i:s');
        $this->JobSet->save();
        $client->runSet($this->taskList);
        if (!$this->background) {
            if ($this->taskList->finished()) {
                global $WorkerJobSetResults;
                $handles = $this->taskList->handles;
                $key_handles = array_keys($handles);
                for ($i = 0; $i < count($WorkerJobSetResults[$this->randomHash]); $i++) {
                    if (array_key_exists($key_handles[$i], $WorkerJobSetResults[$this->randomHash])) {
                        if ($WorkerJobSetResults[$this->randomHash][$key_handles[$i]]['done']) {
                            $job = Job::model()->find('id=:id', array(':id' => $WorkerJobSetResults[$this->randomHash][$key_handles[$i]]['job_id']));
                            if ($job != null) {
                                if ($job == null) {
                                    $job = new Job();
                                }
                                $this->results[] = unserialize(base64_decode($job->result));
                                // echo "Done";
                                $job->needed = 0;
                                $job->save();
                            } else {
                                die("Some results didn't come...\n");
                            }
                        }
                    } else {
                        die("Some results didn't come...\n");
                    }
                }
                $this->JobSet->finishtime = date('Y-m-d H:i:s');
                if ($this->auto_destroy_results) {
                    $this->JobSet->needed = 0;
                    $this->JobSet->delete();
                    $this->JobSet = null;
                }else{
                    $this->JobSet->save();
                }
                return $this->results;
            }
            echo "Task set could not be finished!<br />\n";
            return false;
        } else {
            // background work
            return true;
        }
    }

    private static function generateRandomString($length = 10) {
        $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, strlen($characters) - 1)];
        }
        return $randomString;
    }
    
    public function getJobSetId(){
        if (isset($this->JobSet->id)) {
            return $this->JobSet->id;
        }else{
            return -1;
        }
    }
    
    public function setFinalJobResultId($job_id) {
        if (isset($this->JobSet) && $this->JobSet instanceof JobSet) {
            $this->JobSet->final_job_result_id = $job_id;
            $this->JobSet->save();
            return true;
        }else{
            return false;
        }
    }

}

function WorkerJobSetReturnResult($func, $handle, $result) {
    global $WorkerJobSetResults;
    if (isset($result['WorkerJobSetIdentifier'])) {
        $WorkerJobSetResults[$result['WorkerJobSetIdentifier']][$handle] = $result['result'];
    }
}

?>