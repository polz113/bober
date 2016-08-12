<?php
if (array_key_exists('from', $_GET)) {
    $from = $_GET['from'];
}else{
    $from = 'sl';
}
if (array_key_exists('to', $_GET)) {
    $to = $_GET['to'];
}else{
    $to = 'en';
}
if (array_key_exists('text', $_GET)) {
    $text = urldecode($_GET['text']);
    include_once dirname(__FILE__).'/../../../common/lib/microsoft_translate/microsoft_translate.php';
    echo tryToTranslate($from, $to, $text);
    die();
}else{
    include_once dirname(__FILE__).'/../../../common/lib/microsoft_translate/microsoft_translate.php';
    getLanguages();
}
die();
?>