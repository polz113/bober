<?php
require_once(dirname(__FILE__).'/../common/lib/Net/Gearman/Client.php');

// create set for tasks
$set = new Net_Gearman_Set();
$config = array();
$results = array();
for ($i = 100; $i < 140; $i++) {
    print "Starting process: id " . $i . "\n";
    $task = new Net_Gearman_Task("AllClasses", array("class" => "Svg2Pdf", "function" => "reverse", "params" => array("RandomString".$i)), rand(100, 200) . "_" . $i);

    //$task->type = Net_Gearman_Task::JOB_BACKGROUND; // uncomment to run job in background
    $task->attachCallback("result"); // add callback function, only available type != JOB_BACKGROUND
    // $results[$task->uniq];
    $set->addTask($task); // add task to the set
}

$client = new Net_Gearman_Client(array('localhost:4730'));
$client->runSet($set);
if ($set->finished()) {
    print "All tasks done...\n";
    $handles = $set->handles;
    // print_r($handles);
    // for ($i = 0; $i < $iterator->count(); $i++) {
    // print $handles[$keys[$i]]."\n";
    // print_r($iterator->$handles[$keys[$i]]);
    // $results[] = $iterator->$handles[$keys[$i]]->result;
    // }
    $reorder = array();
    // print_r($results);
    // $keys = array_keys($results);
    $key_handles = array_keys($handles);
    for ($i = 0; $i < count($results); $i++) {
        // print count($results[$keys[$i]])."\n";
        // $handle = array_search($key_handles[$i], $handles);
        // var_dump($handle);
        if (array_key_exists($key_handles[$i], $results)) {
            $reorder[] = $results[$key_handles[$i]];
        } else {
            die("Some results didn't come...\n");
        }
    }
    echo "Results:\n";
    print_r($reorder);
}

function result($func, $handle, $result) {
    global $results;
    $results[$handle] = $result;
}

?>