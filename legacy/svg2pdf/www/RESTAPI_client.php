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

$data = array();
$remote = true;
if ($remote) {
    $url = 'https://bobersvg2pdf.comcode.si/index.php/api/convert';
} else {
    $url = 'http://svg2pdf.bober/index.php/api/convert';
}
$data['svg'] = base64_encode(file_get_contents(dirname(__FILE__) . '/../bober-template.svg'));
$data_list = array(
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
       array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
       array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
       array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
    ),
    array(
        '###IME_IN_PRIIMEK###' => 'Janez Novak'
    ),
);
$data['data'] = json_encode($data_list);
$data['data_type'] = 'json';
$data['background'] = 1;

echo CallAPI('POST', $url, $data, 'admin', 'admin');
?>