<?php

class DemoController extends Controller {

    function actionIndex() {
        $svg = file_get_contents(dirname(__FILE__) . '/../bober-template.svg');
        $data = array(
            array(
                '###IME_IN_PRIIMEK###' => 'Dean Gostiša'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Janez Novak'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Franci na Balanci'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Zvonko Boštjančič'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Neža Čeč'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Gašper Černevšek'
            ),
            array(
                '###IME_IN_PRIIMEK###' => 'Tatjana Per'
            ),
        );
        $pdf = Svg2Pdf::BatchConvert($svg, $data);
        $name = 'Seznam priznanj.pdf';
        header('Content-Type: application/x-download');
        header('Content-Disposition: attachment; filename="' . $name . '"');
        header('Cache-Control: private, max-age=0, must-revalidate');
        header('Pragma: public');
        header('X-Content-Type-Options: nosniff');
        header('X-Frame-Options: SAMEORIGIN');
        // connection close if you want that file is loaded fast (Dean Gostiša)
        header('Connection: close');
        ini_set('zlib.output_compression', '0');
        header('Content-Length: ' . strlen($pdf));
        echo $pdf;
        die();
    }

}

?>