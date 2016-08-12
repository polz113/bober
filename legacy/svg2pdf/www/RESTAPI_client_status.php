<?php

function CallAPI($method, $url, $data = false, $username = 'admin', $password = 'admin') {
    $curl = curl_init();

    switch ($method) {
        case "POST":
            curl_setopt($curl, CURLOPT_POST, 1);

            if ($data) {
                curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
            }
            break;
        case "PUT":
            curl_setopt($curl, CURLOPT_PUT, 1);
            break;
        default:
            if ($data) {
                $url = sprintf("%s?%s", $url, http_build_query($data));
            }
    }

    if ($username != '') {
        curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
        curl_setopt($curl, CURLOPT_USERPWD, $username . ":" . $password);
    }

    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

    return curl_exec($curl);
}

$data = false;
$remote = true;
if ($remote) {
    $url = 'https://bobersvg2pdf.comcode.si/index.php/api/convert/20';
} else {
    $url = 'http://svg2pdf.bober/index.php/api/convert';
}

$response = CallAPI('GET', $url, $data, 'admin', 'admin');
echo $response;
$response = json_decode($response, true);
if (isset($response['result']) && $response['result'] != null && $response['result'] != '') {
    file_put_contents(dirname(__FILE__).'/out.pdf', base64_decode($response['result']));
}
?>