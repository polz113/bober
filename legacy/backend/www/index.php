<?php

$u_agent = array_key_exists('HTTP_USER_AGENT', $_SERVER) ? $_SERVER['HTTP_USER_AGENT'] : '';
if (preg_match('/MSIE/i', $u_agent)) {
    header('X-UA-Compatible: IE=edge,chrome=1');
}

// change the following paths if necessary
$yii=dirname(__FILE__).'/../../common/lib/yii/yii.php';
$config=dirname(__FILE__).'/../config/main.php';

$debug_mode = true;
if (in_array($_SERVER['HTTP_HOST'], array('bober.comcode.si', 'boberadmin.comcode.si', 'bober1.acm.si', 'bober.acm.si', '193.2.76.42', '193.2.76.43', '193.2.76.37'))) {
    $debug_mode = false;
}

// remove the following lines when in production mode
defined('YII_DEBUG') or define('YII_DEBUG', $debug_mode);
// specify how many levels of call stack should be shown in each log message
defined('YII_TRACE_LEVEL') or define('YII_TRACE_LEVEL',3);

require_once($yii);
Yii::createWebApplication($config)->run();
