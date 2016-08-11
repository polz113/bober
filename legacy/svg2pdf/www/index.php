<?php

$u_agent = array_key_exists('HTTP_USER_AGENT', $_SERVER) ? $_SERVER['HTTP_USER_AGENT'] : '';
if (preg_match('/MSIE/i', $u_agent)) {
    header('X-UA-Compatible: IE=edge,chrome=1');
}

// change the following paths if necessary
$yii=dirname(__FILE__).'/../../common/lib/yii/yii.php';
$config=dirname(__FILE__).'/../config/main.php';

// remove the following line when in production mode
// defined('YII_DEBUG') or define('YII_DEBUG',true);

require_once($yii);
Yii::createWebApplication($config)->run();
