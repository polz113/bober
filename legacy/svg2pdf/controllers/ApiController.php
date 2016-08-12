<?php

/**
 * ApiController class file
 * @author Dean Gostiša <dean@comcode.si> @ COMCODE d.o.o.
 * @license http://creativecommons.org/licenses/by-nc-nd/3.0/deed.sl CC BY-NC-ND 3.0
 */

/**
 * ApiController 
 * 
 * @uses Controller
 * @author Dean Gostiša <dean@comcode.si> @ COMCODE d.o.o.
 * @license http://creativecommons.org/licenses/by-nc-nd/3.0/deed.sl CC BY-NC-ND 3.0
 */
class ApiController extends Controller {

    Const APPLICATION_ID = 'SVG2PDF';

    private $format = 'json';
    
    private $user_id = 0;

    /**
     * @return array action filters
     */
    public function filters() {
        return array();
    }

// }}} 
    // {{{ *** Actions ***
    // {{{ actionIndex

    public function actionIndex() {
        $possibleCommands = array(
            '/index.php/api/convert/' => array(
                'POST' => array(
                    'description' => 'Function to convert SVG to PDF.',
                    'input' => array(
                        'svg' => array(
                            'type' => 'string',
                            'description' => 'Base64 encoded SVG template'
                        ),
                        'data' => array(
                            'type' => 'string',
                            'description' =>    'Data for replacing strings in SVG when creating PDFs.' . "\n" .
                                                'Data may be in format: csv, json' . "\n\n" .
                                                'Data in CSV format: header line columns define hotkeys for replacing ' .
                                                'string in SVG with real value. All lines after header line are data lines. ' .
                                                'Each line represent separate PDF page, hotkeys are replaced accordingly to column row cell values. ' .
                                                'Default columns delimiter is: \';\', default columns enclosure is: \'"\', this settings can be overriden with ' .
                                                'data_parameters param.' .
                                                'Data in JSON format: json encoded array of data, each element in array is one PDF page, each elements has ' .
                                                'format \'hotkey_to_be_replaced\'=>\'new value\''
                        ),
                        'data_type' => array(
                            'type' => 'string',
                            'description' => 'Possible values: json, csv. Is not defined, default value: json'
                        ),
                        'data_encoding' => array(
                            'type' => 'string',
                            'description' => 'If input string in data param is not encoded with UTF-8, please provide in which encoding it is.' .
                                             'Usually on Slovenian Windows it may be: WINDOWS-1250. If your string is in UTF-8 please leave this param empty'
                        ),
                        'data_parameters' => array(
                            'type' => 'string',
                            'description' => 'Additional parsing parameters for input data. Parameters are in format: \'setting==value||setting2==value2\'. '."\n".
                                             'Currently this option only available when importing in CSV format. '. "\n".
                                             'Data Type: csv. Possible parameters: delimiter, enclosure'."\n".
                                             'Example: \'delimiter==;||enclosure=="\''
                        ),
                        'background' => array(
                            'type' => 'integer',
                            'description' => 'With this setting we can schedule converting to process in background. '."\n".
                                             'If backgroud is set to: 0 - request to API will stay open until all PDFs are done, '.
                                             'it is possible that client is disconnect because of too long execution time'."\n".
                                             'If backgroud is set to: 1 - request to API is closed as soon server saves instruction to database, '.
                                             'client will be provided with ID with which he can monitor progres of his request'
                        )
                    ),
                    'output' => array(
                        'id' => array(
                            'type' => 'integer',
                            'description' => 'ID of conversion job. With this ID you can access to generated PDF if lunched processing in background.'
                        ),
                        'background' => array(
                            'type' => 'integer',
                            'description' => 'With this setting we can schedule converting to process in background. '."\n".
                                             'If backgroud is set to: 0 - request to API will stay open until all PDFs are done, '.
                                             'it is possible that client is disconnect because of too long execution time'."\n".
                                             'If backgroud is set to: 1 - request to API is closed as soon server saves instruction to database, '.
                                             'client will be provided with ID with which he can monitor progres of his request'
                        ),
                        'result' => array(
                            'type' => 'string',
                            'desctiption' => 'Base64 encoded string containing PDF. If background processing was selected. This variable will be null.'
                        )
                    )
                ),
                'GET' => array(
                    'description' => 'Function to get generated PDF or status of process for generating PDF.',
                    'input' => array(
                        'id' => array(
                            'type' => 'integer',
                            'desctiption' => 'ID of conversion job provided on creation'
                        )
                    ),
                    'output' => array(
                        'id' => array(
                            'type' => 'integer',
                            'description' => 'ID of conversion job. With this ID you can access to generated PDF if lunched processing in background.'
                        ),
                        'background' => array(
                            'type' => 'integer',
                            'description' => 'With this setting we can schedule converting to process in background. '."\n".
                                             'If backgroud is set to: 0 - request to API will stay open until all PDFs are done, '.
                                             'it is possible that client is disconnect because of too long execution time'."\n".
                                             'If backgroud is set to: 1 - request to API is closed as soon server saves instruction to database, '.
                                             'client will be provided with ID with which he can monitor progres of his request'
                        ),
                        'background_done' => array(
                            'type' => 'boolean',
                            'description' => 'It returns true if background process is finished or False if still in progress.'
                        ),
                        'result' => array(
                            'type' => 'string',
                            'desctiption' => 'Base64 encoded string containing PDF. If background processing was selected. This variable will be null.'
                        ),
                        'jobs_done' => array(
                            'type' => 'integer',
                            'description' => 'Number of finished jobs for this conversion job.'
                        ),
                        'jobs_to_do' => array(
                            'type' => 'integer',
                            'description' => 'Number of jobs planned for this conversion job.'
                        ),
                        'progress' => array(
                            'type' => 'float(3,2)',
                            'description' => 'Procent of progress of this conversion job. When 100.0 is reached means that conversion job is finished.'
                        )
                    )
                )
            )
        );
        echo CJSON::encode($possibleCommands);
    }

    public function actionList() {
        $this->_checkAuth();
        $currentModel = mb_strtolower($_GET['model'], 'UTF-8');

        switch ($currentModel) {
            case 'convert': 
                $models = Convert::model()->findAll('user_id=:user_id', array(':user_id' => $this->user_id));
                break; // }}} 
            default: // {{{ 
                $this->_sendResponse(501, sprintf('Error: Mode <b>list</b> is not implemented for model <b>%s</b>', $_GET['model']));
                exit; // }}} 
        }
        if (is_null($models)) {
            $this->_sendResponse(200, sprintf('No items where found for model <b>%s</b>', $_GET['model']));
        } else {
            $rows = array();
            foreach ($models as $model) {
                $rows[] = array('id' => $model->id);
            }

            $this->_sendResponse(200, CJSON::encode($rows));
        }
    }


    /* Shows a single item
     * 
     * @access public
     * @return void
     */
    public function actionView() {
        $this->_checkAuth();
        // Check if id was submitted via GET
        if (!isset($_GET['id'])) {
            $this->_sendResponse(500, 'Error: Parameter <b>id</b> is missing');
        }

        $currentModel = mb_strtolower($_GET['model'], 'UTF-8');
        $return_array = array();
        $return_custom = false;

        switch ($currentModel) {
            // Find respective model    
            case 'convert': // {{{ 
                $return_custom = true;
                $model = Convert::model()->findByPk($_GET['id'], 'user_id=:user_id', array(':user_id' => $this->user_id));
                if ($model != null) {
                    if ($model == null) {
                        $model = new Convert();
                    }
                    if ($model->result == null) {
                        if (isset($model->backgroudJobSet->finalJobResult->result)) {
                            if ($model->backgroudJobSet->finalJobResult->result != null) {
                                $result = unserialize(base64_decode($model->backgroudJobSet->finalJobResult->result));
                                $model->result = base64_encode($result);
                            }
                            // cleanup
                            if ($model->result != null) {
                                $model->backgroudJobSet->delete();
                                $model->backgroud_job_set_id = null;
                            }
                            $model->save();
                        }
                    }
                    $background_done = false;
                    $jobs_done = 0;
                    $jobs_to_do = 0;
                    if ($model->background) {
                        if ($model->result != null) {
                            $background_done = true;
                        }
                        $jobs_done = Job::model()->count('job_set_id=:job_set_id and finished=:finished', array(':job_set_id' => $model->backgroud_job_set_id, ':finished' => 1));
                        $jobs_to_do = Job::model()->count('job_set_id=:job_set_id', array(':job_set_id' => $model->backgroud_job_set_id));
                    }
                    $return_array = array(
                        'id' => $model->id,
                        'background' => $model->background,
                        'background_done' => $background_done,
                        'result' => $model->result,
                        'jobs_done' => $jobs_done,
                        'jobs_to_do' => $jobs_to_do,
                        'progress' => $jobs_to_do != 0 ? round($jobs_done / $jobs_to_do * 10000) / 100 : 100,
                    );
                }
                break; // }}} 
            default: // {{{ 
                $this->_sendResponse(501, sprintf('Mode <b>view</b> is not implemented for model <b>%s</b>', $_GET['model']));
                exit; // }}} 
        }
        if (is_null($model)) {
            $this->_sendResponse(404, 'No Item found with id ' . $_GET['id']);
        } else {
            $this->_sendResponse(200, $this->_getObjectEncoded($_GET['model'], $return_custom ? $return_array : $model->attributes));
        }
    }

    /**
     * Creates a new item
     * 
     * @access public
     * @return void
     */
    public function actionCreate() {
        $this->_checkAuth();
        $currentModel = mb_strtolower($_GET['model'], 'UTF-8');
        $return_array = array();
        $return_custom = false;

        switch ($currentModel) {
            // Get an instance of the respective model
            case 'convert':
                $model = new Convert();
                break;
            default:
                $this->_sendResponse(501, sprintf('Mode <b>create</b> is not implemented for model <b>%s</b>', $_GET['model']));
                exit;
        }
        // Try to assign POST values to attributes
        foreach ($_POST as $var => $value) {
            // Does the model have this attribute?
            if ($model->hasAttribute($var)) {
                $model->$var = $value;
            } else {
                // No, raise an error
                $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is not allowed for model <b>%s</b>', $var, $_GET['model']));
            }
        }

        if ($currentModel == 'convert') {
            $model->user_id = $this->user_id;
            $return_custom = true;
            if ($model->data_encoding != '' && $model->data_encoding != null) {
                $model->data_encoding = trim(mb_strtoupper($model->data_encoding, 'UTF-8'));
                if (!Encoding::EncodingExists($model->data_encoding)) {
                    $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is not valid for model <b>%s</b>. Valid values: ' . implode(', ', Encoding::$list), 'data_encoding', $_GET['model']));
                }
            } else {
                $model->data_encoding = null;
            }

            if ($model->data_encoding != null) {
                $model->data = iconv($model->data_encoding, 'UTF-8', $model->data);
            }

            switch (mb_strtolower($model->data_type, 'UTF-8')) {
                case 'json':
                    if ($model->data != '') {
                        $list = json_decode($model->data, true);
                        // check if array is designed as: array( array("###KEY_TO_REPLACE###" => "Replaced value"), array(...))
                        $keys = array_keys($list);
                        $keys_ok = true;
                        for ($i = 0; $i < count($keys); ++$i) {
                            if (!is_numeric($keys[$i])) {
                                $keys_ok = false;
                            }
                        }
                        if ($keys_ok) {
                            $model->data_to_use = base64_encode(serialize($list));
                        } else {
                            $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is invalid json format for model <b>%s</b>. JSON structure should be: [{"###KEY_TO_REPLACE###":"Replaced Value 1","###KEY###":"Key 1"},{"###KEY_TO_REPLACE###":"Replaced Value 2","###KEY###":"Key 2"}]', 'data', $_GET['model']));
                        }
                    } else {
                        $model->data_to_use = base64_encode(serialize(array()));
                    }
                    break;
                case 'csv':
                    $delimiter = ';';
                    $enclosure = '"';
                    if ($model->data_parameters != null && $model->data_parameters != '') {
                        $params = explode('||', $model->data_parameters);
                        foreach ($params as $param) {
                            $param = explode('==', $param);
                            $key = $param[0];
                            $value = isset($param[1]) ? $param[1] : '';
                            switch ($key) {
                                case 'delimiter':
                                    $delimiter = $value;
                                    break;
                                case 'enclosure':
                                    $enclosure = $value;
                                    break;
                                default:
                                    $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is invalid format for model <b>%s</b>. Valid value for CSV is: \'setting1==value||setting2==value\', example: \'delimiter==;||enclosure=="\', default delimiter is: \';\', default enclosure is: \'"\'', 'data_parameters', $_GET['model']));
                                    break;
                            }
                        }
                    }
                    $data = CSV::toArray($model->data, $delimiter, $enclosure);
                    if (count($data) > 0) {
                        if (count($data) > 1) {
                            $header = $data[0];
                            $list = array();
                            for ($i = 1; $i < count($data); ++$i) {
                                $row = array();
                                for ($c = 0; $c < count($header); ++$c) {
                                    $row[$header[$c]] = isset($data[$c]) ? $data[$c] : '';
                                }
                                $list[] = $row;
                            }
                            $model->data_to_use = base64_encode(serialize($list));
                        } else {
                            $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is empty for model <b>%s</b>. CSV should contain more lines. Not only one header line.', 'data', $_GET['model']));
                        }
                    } else {
                        $model->data_to_use = base64_encode(serialize(array()));
                    }
                    break;
                default:
                    $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is invalid for model <b>%s</b>, allowed values: [json, csv]', 'data_type', $_GET['model']));
                    break;
            }
        }


        // Try to save the model
        if ($model->save()) {
            // Saving was OK
            if ($currentModel == 'convert') {
                if ($model->background == 1) {
                    // we send work to background, user can pool status of convert
                    $jobSetId = Svg2Pdf::BatchConvert(base64_decode($model->svg), unserialize(base64_decode($model->data_to_use)), $model->background);
                    $model->backgroud_job_set_id = $jobSetId;
                    $model->save();
                } else {
                    // we send work to do it now, user wait for result in open connection
                    $pdf = base64_encode(Svg2Pdf::BatchConvert(base64_decode($model->svg), unserialize(base64_decode($model->data_to_use))));
                    $model->result = $pdf;
                    $model->save();
                }
                // do not return all data
                $return_array = array(
                    'id' => $model->id,
                    'background' => $model->background,
                    'result' => $model->result
                );
            }
            $this->_sendResponse(200, $this->_getObjectEncoded($_GET['model'], $return_custom ? $return_array : $model->attributes));
        } else {
            // Errors occurred
            $msg = "<h1>Error</h1>";
            $msg .= sprintf("Couldn't create model <b>%s</b>", $_GET['model']);
            $msg .= "<ul>";
            foreach ($model->errors as $attribute => $attr_errors) {
                $msg .= "<li>Attribute: $attribute</li>";
                $msg .= "<ul>";
                foreach ($attr_errors as $attr_error) {
                    $msg .= "<li>$attr_error</li>";
                }
                $msg .= "</ul>";
            }
            $msg .= "</ul>";
            $this->_sendResponse(500, $msg);
        }

        var_dump($_REQUEST);
    }

    /**
     * Update a single iten
     * 
     * @access public
     * @return void
     */
    public function actionUpdate() {
        $this->_checkAuth();
        // Get PUT parameters
        parse_str(file_get_contents('php://input'), $put_vars);

        switch ($_GET['model']) {
            // Find respective model
            case 'posts':
                $model = Post::model()->findByPk($_GET['id']);
                break;
            default:
                $this->_sendResponse(501, sprintf('Error: Mode <b>update</b> is not implemented for model <b>%s</b>', $_GET['model']));
                exit;
        }
        if (is_null($model))
            $this->_sendResponse(400, sprintf("Error: Didn't find any model <b>%s</b> with ID <b>%s</b>.", $_GET['model'], $_GET['id']));

        // Try to assign PUT parameters to attributes
        foreach ($put_vars as $var => $value) {
            // Does model have this attribute?
            if ($model->hasAttribute($var)) {
                $model->$var = $value;
            } else {
                // No, raise error
                $this->_sendResponse(500, sprintf('Parameter <b>%s</b> is not allowed for model <b>%s</b>', $var, $_GET['model']));
            }
        }
        // Try to save the model
        if ($model->save()) {
            $this->_sendResponse(200, sprintf('The model <b>%s</b> with id <b>%s</b> has been updated.', $_GET['model'], $_GET['id']));
        } else {
            $msg = "<h1>Error</h1>";
            $msg .= sprintf("Couldn't update model <b>%s</b>", $_GET['model']);
            $msg .= "<ul>";
            foreach ($model->errors as $attribute => $attr_errors) {
                $msg .= "<li>Attribute: $attribute</li>";
                $msg .= "<ul>";
                foreach ($attr_errors as $attr_error) {
                    $msg .= "<li>$attr_error</li>";
                }
                $msg .= "</ul>";
            }
            $msg .= "</ul>";
            $this->_sendResponse(500, $msg);
        }
    }

    /**
     * Deletes a single item
     * 
     * @access public
     * @return void
     */
    public function actionDelete() {
        $this->_checkAuth();
        $currentModel = mb_strtolower($_GET['model'], 'UTF-8');

        switch ($currentModel) {
            // Load the respective model
            case 'convert':
                $model = Convert::model()->findByPk($_GET['id'], 'user_id=:user_id', array(':user_id' => $this->user_id));
                break;
            default:
                $this->_sendResponse(501, sprintf('Error: Mode <b>delete</b> is not implemented for model <b>%s</b>', $_GET['model']));
                exit;
        }
        // Was a model found?
        if (is_null($model)) {
            // No, raise an error
            $this->_sendResponse(400, sprintf("Error: Didn't find any model <b>%s</b> with ID <b>%s</b>.", $_GET['model'], $_GET['id']));
        }

        // Delete the model
        $num = $model->delete();
        if ($num > 0) {
            $this->_sendResponse(200, sprintf("Model <b>%s</b> with ID <b>%s</b> has been deleted.", $_GET['model'], $_GET['id']));
        } else {
            $this->_sendResponse(500, sprintf("Error: Couldn't delete model <b>%s</b> with ID <b>%s</b>.", $_GET['model'], $_GET['id']));
        }
    }

    /**
     * Sends the API response 
     * 
     * @param int $status 
     * @param string $body 
     * @param string $content_type 
     * @access private
     * @return void
     */
    private function _sendResponse($status = 200, $body = '', $content_type = 'text/html') {
        $status_header = 'HTTP/1.1 ' . $status . ' ' . $this->_getStatusCodeMessage($status);
        // set the status
        header($status_header);
        // set the content type
        header('Content-type: ' . $content_type);

        // pages with body are easy
        if ($body != '') {
            // send the body
            echo $body;
            exit;
        } else { // we need to create the body if none is passed
            // create some body messages
            $message = '';

            // this is purely optional, but makes the pages a little nicer to read
            // for your users.  Since you won't likely send a lot of different status codes,
            // this also shouldn't be too ponderous to maintain
            switch ($status) {
                case 401:
                    $message = 'You must be authorized to view this page.';
                    break;
                case 404:
                    $message = 'The requested URL ' . $_SERVER['REQUEST_URI'] . ' was not found.';
                    break;
                case 500:
                    $message = 'The server encountered an error processing your request.';
                    break;
                case 501:
                    $message = 'The requested method is not implemented.';
                    break;
                default:
                    break;
            }

            // servers don't always have a signature turned on (this is an apache directive "ServerSignature On")
            $signature = ($_SERVER['SERVER_SIGNATURE'] == '') ? $_SERVER['SERVER_SOFTWARE'] . ' Server at ' . $_SERVER['SERVER_NAME'] . ' Port ' . $_SERVER['SERVER_PORT'] : $_SERVER['SERVER_SIGNATURE'];

            // this should be templatized in a real-world solution
            $body = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
                        <html>
                            <head>
                                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
                                <title>' . $status . ' ' . $this->_getStatusCodeMessage($status) . '</title>
                            </head>
                            <body>
                                <h1>' . $this->_getStatusCodeMessage($status) . '</h1>
                                <p>' . $message . '</p>
                                <hr />
                                <address>' . $signature . '</address>
                            </body>
                        </html>';

            echo $body;
            exit;
        }
    }

    /**
     * Gets the message for a status code
     * 
     * @param mixed $status 
     * @access private
     * @return string
     */
    private function _getStatusCodeMessage($status) {
        // these could be stored in a .ini file and loaded
        // via parse_ini_file()... however, this will suffice
        // for an example
        $codes = Array(
            100 => 'Continue',
            101 => 'Switching Protocols',
            200 => 'OK',
            201 => 'Created',
            202 => 'Accepted',
            203 => 'Non-Authoritative Information',
            204 => 'No Content',
            205 => 'Reset Content',
            206 => 'Partial Content',
            300 => 'Multiple Choices',
            301 => 'Moved Permanently',
            302 => 'Found',
            303 => 'See Other',
            304 => 'Not Modified',
            305 => 'Use Proxy',
            306 => '(Unused)',
            307 => 'Temporary Redirect',
            400 => 'Bad Request',
            401 => 'Unauthorized',
            402 => 'Payment Required',
            403 => 'Forbidden',
            404 => 'Not Found',
            405 => 'Method Not Allowed',
            406 => 'Not Acceptable',
            407 => 'Proxy Authentication Required',
            408 => 'Request Timeout',
            409 => 'Conflict',
            410 => 'Gone',
            411 => 'Length Required',
            412 => 'Precondition Failed',
            413 => 'Request Entity Too Large',
            414 => 'Request-URI Too Long',
            415 => 'Unsupported Media Type',
            416 => 'Requested Range Not Satisfiable',
            417 => 'Expectation Failed',
            500 => 'Internal Server Error',
            501 => 'Not Implemented',
            502 => 'Bad Gateway',
            503 => 'Service Unavailable',
            504 => 'Gateway Timeout',
            505 => 'HTTP Version Not Supported'
        );

        return (isset($codes[$status])) ? $codes[$status] : '';
    }

    /**
     * Checks if a request is authorized
     * 
     * @access private
     * @return void
     */
    private function _checkAuth() {
        // Check if we have the USERNAME and PASSWORD HTTP headers set?
        if (!(isset($_SERVER['PHP_AUTH_USER']) and isset($_SERVER['PHP_AUTH_PW']))) {
            // Error: Unauthorized
            header('WWW-Authenticate: Basic realm="' . self::APPLICATION_ID . '"');
            $this->_sendResponse(401);
        }
        $username = $_SERVER['PHP_AUTH_USER'];
        $password = $_SERVER['PHP_AUTH_PW'];
        // Find the user
        $user = User::model()->find('LOWER(username)=?', array(strtolower($username)));
        if ($user === null) {
            // Error: Unauthorized
            header('WWW-Authenticate: Basic realm="' . self::APPLICATION_ID . '"');
            $this->_sendResponse(401, 'Error: User Name is invalid');
            if ($user == null) {
                $user = new User();
            }
        } else if (!$user->validatePassword($password)) {
            // Error: Unauthorized
            header('WWW-Authenticate: Basic realm="' . self::APPLICATION_ID . '"');
            $this->_sendResponse(401, 'Error: User Password is invalid');
        }else{
            $this->user_id = $user->id;
        }
    }

    /**
     * Returns the json or xml encoded array
     * 
     * @param mixed $model 
     * @param mixed $array Data to be encoded
     * @access private
     * @return void
     */
    private function _getObjectEncoded($model, $array) {
        if (isset($_GET['format'])) {
            $this->format = $_GET['format'];
        }

        if ($this->format == 'json') {
            return CJSON::encode($array);
        } else if ($this->format == 'xml') {
            $result = '<?xml version="1.0">';
            $result .= "\n" . '<' . $model . '>' . "\n";
            foreach ($array as $key => $value) {
                $result .= '    <' . $key . '>' . utf8_encode($value) . '</' . $key . '>' . "\n";
            }
            $result .= '</' . $model . '>';
            return $result;
        } else {
            return;
        }
    }
}

?>