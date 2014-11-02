<?php

/**
 * This is the model class for table "question".
 *
 * The followings are the available columns in table 'question':
 * @property integer $id
 * @property integer $country_id
 * @property integer $country_of_origin
 * @property string $identifier
 * @property integer $type
 * @property string $title
 * @property string $text
 * @property string $data
 * @property string $version
 * @property integer $verification_function_type   =>  0 == internal, 1 == JavaScript
 * @property string $verification_function
 * @property string $last_change_date
 * @property string $authors
 * @property string $css
 *
 * The followings are the available model relations:
 * @property CompetitionQuestion[] $competitionQuestions
 * @property Country $country
 * @property QuestionAnswer[] $questionAnswers
 * @property QuestionResource[] $questionResources
 * @property QuestionTranslation[] $questionTranslations
 */
class Question extends CActiveRecord {

    public $country_search;
    public $uploadedData;
    public $importZIP;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return Question the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'question';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
// NOTE: you should only define rules for those attributes that
// will receive user inputs.
        return array(
            array('country_id, identifier, title', 'required'),
            array('country_id, type, verification_function_type', 'numerical', 'integerOnly' => true),
            array('country_of_origin', 'length', 'max' => 5), /* same as Language.short */
            array('title, version', 'length', 'max' => 255),
            array('text, data, verification_function, authors, css', 'safe'),
            // The following rule is used by search().
// Please remove those attributes that should not be searched.
            array('id, country_id, identifier, type, title, text, data, version,country_search, verification_function_type, verification_function, authors, uploadedData, css', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
// NOTE: you may need to adjust the relation name and the related
// class name for the relations automatically generated below.
        return array(
            'competitionQuestions' => array(self::HAS_MANY, 'CompetitionQuestion', 'question_id'),
            'country' => array(self::BELONGS_TO, 'Country', 'country_id'),
            'questionAnswers' => array(self::HAS_MANY, 'QuestionAnswer', 'question_id'),
            'questionResources' => array(self::HAS_MANY, 'QuestionResource', 'question_id'),
            'questionTranslations' => array(self::HAS_MANY, 'QuestionTranslation', 'question_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'country_id' => Yii::t('app', 'Country'),
            'country_of_origin' => Yii::t('app', 'Country of Origin'),
            'identifier' => Yii::t('app', 'Identifier'),
            'type' => Yii::t('app', 'Type'),
            'title' => Yii::t('app', 'Title'),
            'text' => Yii::t('app', 'Text'),
            'data' => Yii::t('app', 'Data'),
            'version' => Yii::t('app', 'Version'),
            'verification_function_type' => Yii::t('app', 'Verification Function Type'),
            'verification_function' => Yii::t('app', 'Verification Function'),
            'last_change_date' => Yii::t('app', 'Last Change Date'),
            'authors' => Yii::t('app', 'Authors'),
            'css' => Yii::t('app', 'CSS'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            return true;
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                $countryAdministratorCheck = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $this->country_id));

                $change_to_country_id = isset($_POST['Question']['country_id']) ? $_POST['Question']['country_id'] : -1;
                $countryAdministratorCheck2 = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $change_to_country_id));

                if (($countryAdministratorCheck != null && $countryAdministratorCheck2 != null) || ($countryAdministratorCheck2 != null && $change_to_country_id != -1) || ($countryAdministratorCheck != null && $change_to_country_id == -1)) {
                    return true;
                }
            }
        }
        return false;
    }

    public function getCanUpdate() {
        return $this->CanUpdate();
    }

    public function CanUpdate() {
        return $this->CanView();
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        return $this->CanView();
    }

    public function GetQuestionType($empty = false) {
        $options = array(
            1 => Yii::t('app', 'Simple Question'),
            2 => Yii::t('app', 'Interactive Question')
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All Types'));
        }

        return $options;
    }

    public function GetQuestionTypeName($id) {
        $types = $this->GetQuestionType();
        if (isset($types[$id])) {
            return $types[$id];
        }
        return '';
    }

    public function GetVerificationFunctionType($empty = false) {
        $options = array(
            1 => Yii::t('app', 'JavaScript'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All Types'));
        }
        return $options;
    }

    public function GetVerificationFunctionTypeName($id) {
        $type = $this->GetVerificationFunctionType();
        if (isset($type[$id])) {
            return $type[$id];
        }
        return '';
    }

    public function ValidateJSONMAnifestAgainstShema($json) {
        include_once dirname(__FILE__) . '/../extensions/JSONShemaValidator/JsonSchema.php';
        include_once dirname(__FILE__) . '/../extensions/JSONShemaValidator/JsonSchemaUndefined.php';
        $shema = file_get_contents(dirname(__FILE__) . '/../extensions/JSONShemaValidator/Bober_Interacitve_Task_Object_Shema.json');
        $schema = json_decode($shema);
        if (!$schema) {
            return array('return' => false, 'error' => 'Could not parse the SCHEMA object.');
        } else {
            $schema = null;
        }
        $json = json_decode($json);
        if (!$json) {
            switch (json_last_error()) {
                case JSON_ERROR_NONE:
                    echo ' - No errors';
                    break;
                case JSON_ERROR_DEPTH:
                    echo ' - Maximum stack depth exceeded';
                    break;
                case JSON_ERROR_STATE_MISMATCH:
                    echo ' - Underflow or the modes mismatch';
                    break;
                case JSON_ERROR_CTRL_CHAR:
                    echo ' - Unexpected control character found';
                    break;
                case JSON_ERROR_SYNTAX:
                    echo ' - Syntax error, malformed JSON';
                    break;
                case JSON_ERROR_UTF8:
                    echo ' - Malformed UTF-8 characters, possibly incorrectly encoded';
                    break;
                default:
                    echo ' - Unknown error';
                    break;
            }
            return array('return' => false, 'error' => 'Could not parse the JSON object.');
        }
        $result = json_decode(json_encode(JsonSchema::validate($json, $schema)), true);

        return array('return' => $result['valid'], 'error' => implode("\n", $result['errors']));
    }

    public function processImport($fileName) {
        $tmpdirname = tempnam(sys_get_temp_dir(), 'questionImport');
        $tmpdir = $tmpdirname . '_dir';
        mkdir($tmpdir);
        $error = false;
        $id = -1;
        try {
            if (is_dir($tmpdir)) {
                if (QuestionController::unzip($fileName, $tmpdir)) {
                    if (file_exists($tmpdir . '/Manifest.json')) {
                        $json = file_get_contents($tmpdir . '/Manifest.json');
                        $jsonValidation = $this->ValidateJSONMAnifestAgainstShema($json);

                        if ($jsonValidation['return']) {
                            $manifest = json_decode($json, true);
                            $id = $this->processJSONData($manifest, $tmpdir);
                        } else {
                            // json ni tak kot zahetva shema
                            throw new CHttpException(405, Yii::t('app', $jsonValidation['error']));
                        }
                    } else {
                        throw new CHttpException(405, Yii::t('app', 'Manifest.json does not exist.'));
                    }
                    QuestionController::delTree($tmpdir);
                } else {
                    throw new CHttpException(405, Yii::t('app', 'Unzip unsuccessful'));
                }
            }
        } catch (Exception $e) {
            $error = true;
            $exception = $e;
        }
        if (is_dir($tmpdir)) {
            QuestionController::delTree($tmpdir);
        }
        unlink($tmpdirname);
        if ($error) {
            throw $exception;
        }
        return $id;
    }

    public function getJSONAttribute($attribute, $manifest) {
        if (array_key_exists($attribute, $manifest)) {
            return $manifest[$attribute];
        } else {
            throw new CHttpException(405, Yii::t('app', "Missing " . $attribute . " in JSON file."));
        }
    }

    public function processJSONData($manifest, $tmpdir) {
        $acceptedAnswers = false;

        $model = Question::model()->find("identifier=:identifier", array(':identifier' => $this->getJSONAttribute('id', $manifest)));
        if ($model != NULL) {
            //exist task with equal identifier
        } else {
            $model = new Question();
        }

        $model->attributes = $_POST['Question'];


        $model->identifier = $this->getJSONAttribute('id', $manifest);
        $language = $this->getJSONAttribute('language', $manifest);
        $languageModel = Language::model()->find('short=:short', array(':short' => $language));
        $model->version = $this->getJSONAttribute('version', $manifest);
        $model->type = 2;
        $model->title = $this->getJSONAttribute('title', $manifest);
        $model->authors = $this->getJSONAttribute('authors', $manifest);
        if (array_key_exists('country', $manifest)){
            $model->country_of_origin = $this->getJSONAttribute('country', $manifest);
        } else {
            $model->country_of_origin = '';
        }
        if (array_key_exists('browserSupport', $manifest) && count($manifest['browserSupport'] != 0)) {
            $model->data = $this->processBrowserSupport($manifest['browserSupport']);
        }
        if (array_key_exists('acceptedAnswers', $manifest)) {
            if (count($manifest['acceptedAnswers']) != '') {
                $model->verification_function_type = 0;
                $model->verification_function = serialize($manifest['acceptedAnswers']);
                $acceptedAnswers = true;
            } else {
                $acceptedAnswers = false;
            }
        }
        if (array_key_exists('grader', $manifest) && count($manifest['grader']) != 0 && !$acceptedAnswers) {
            if (array_key_exists('type', $manifest['grader'][0])) {
                if (!strcmp('javascript', strtolower($manifest['grader'][0]['type']))) {
                    $model->verification_function_type = 1;
                    $model->verification_function = 'grader.gradeTask(###RANDOM_SEED###, ###ANSWER###, ###MINSCORE###, ###MAXSCORE###)';
                } else {
                    //   $this->verification_function_type = 0;
                }
            } else {
                throw new CHttpException(405, Yii::t('app', 'Missing "grader[0][type]" in JSON file.'));
            }
        }
        if ($model->save()) {

            $CurrentResources = array();
            foreach ($model->questionResources as $resource) {
                if ($resource->language_id == $languageModel->id) {
                    $CurrentResources[$resource->id] = false;
                }
            }

            $resourceType = array('task', 'solution', 'grader', 'task_modules', 'solution_modules', 'grader_modules');
            for ($i = 0; $i < count($resourceType); $i++) {
                $type = $resourceType[$i];
                if ($i == 2 && $acceptedAnswers) {
                    continue;
                }
                if ($i < 3) {
                    $this->processResourceType($model, $this->getJSONAttribute($type, $manifest), $tmpdir, $i + 1, $language, $CurrentResources);
                } elseif (array_key_exists($type, $manifest) && count($manifest[$type] != 0)) {
                    $this->processResourceType($model, $this->getJSONAttribute($type, $manifest), $tmpdir, $i + 1, $language, $CurrentResources);
                }
            }
            foreach ($CurrentResources as $id => $used) {
                if (!$used) {
                    $questionResource = QuestionResource::model()->find('id=:id', array(':id' => $id));
                    if ($questionResource != null) {
                        if (!$questionResource->delete()) {
                            print_r($questionResource->getErrors());
                            die();
                        }
                    }
                }
            }
            return $model->id;
        } else {
            return -1;
        }
    }

    public function processBrowserSupport($browserSupport) {
        $data = '';
        for ($i = 0; $i < count($browserSupport); $i++) {
            if (!array_key_exists('name', $browserSupport[$i])) {
                throw new CHttpException(405, Yii::t('app', 'Missing "browserSupport[' . $i . '][name]" in JSON file.'));
            }
            if (!array_key_exists('version', $browserSupport[$i])) {
                throw new CHttpException(405, Yii::t('app', 'Missing "browserSupport[' . $i . '][version]" in JSON file.'));
            }
            if (!array_key_exists('os', $browserSupport[$i])) {
                throw new CHttpException(405, Yii::t('app', 'Missing "browserSupport[' . $i . '][os]" in JSON file.'));
            }
            if (!array_key_exists('supported', $browserSupport[$i])) {
                throw new CHttpException(405, Yii::t('app', 'Missing "browserSupport[' . $i . '][supported]" in JSON file.'));
            }
            $data1 = $browserSupport[$i]['name'];
            $data1 = $data1 . ' ' . $browserSupport[$i]['version'];
            $data1 = $data1 . ' ' . $browserSupport[$i]['os'];
            $data1 = $data1 . ' ' . $browserSupport[$i]['supported'];
            $data = $data . ' ' . $data1;
        }
        return $data;
    }

    /**
     * @param Question $QuestionModel
     * @param array $resourceType
     * @param type $tmpdir
     * @param int $type 1 == task, 2 == solution, 3 == grader, 4 == task_modules, 5 == solution_modules, 6 == grader_modules
     * @throws CHttpException
     */
    public function processResourceType($QuestionModel, $resourceType, $tmpdir, $type, $language_code, &$CurrentResources) {
        $foundHtmlFile = false;
        for ($i = 0; $i < count($resourceType); $i++) {
            $fileData = '';
            $fileName = '';
            $path = '';
            if (!array_key_exists('type', $resourceType[$i])) {
                throw new CHttpException(405, Yii::t('app', 'Missing "' . $resourceType . '[' . $i . '][type]" in JSON file.'));
            }
            if (array_key_exists('url', $resourceType[$i])) {
                $FileData = $this->GetJSONUrl($tmpdir, $resourceType[$i]['url']);
                $fileName = $FileData[1];
                $path = $FileData[2];
                $fileData = $FileData[0];
            } elseif (array_key_exists('content', $resourceType[$i])) {
                $fileData = $resourceType[$i]['content'];
            } else {
                throw new CHttpException(405, Yii::t('app', 'Missing "' . $resourceType . '[' . $i . '][url]" or "' . $resourceType . '[' . $i . '][content]" in JSON file.'));
            }
            $fileType = trim(mb_strtolower($resourceType[$i]['type'], 'UTF-8'));
            $fileType = $this->GetJSONResourceType($fileType, $tmpdir, $fileName, $path);
            if ($fileType == 'text/html' && $type == 1 && !$foundHtmlFile) {
                $start_up = 1;
                $foundHtmlFile = true;
            } else {
                $start_up = 0;
            }
            $this->FillQuestionResource($QuestionModel, $fileData, $fileName, $path, $fileType, $type, $start_up, $language_code, $CurrentResources);
        }
    }

    public function GetJSONResourceType($type, $tmpdir, $fileName, $path) {
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        if ($type == 'html') {
            $type = 'text/html';
        } elseif ($type == 'javascript') {
            $type = 'application/javascript';
        } elseif ($type == 'css') {
            $type = 'text/css';
        } elseif ($type == 'image') {
            $type = finfo_file($finfo, $tmpdir . '/' . $path . $fileName);
        } else {
            throw new CHttpException(405, Yii::t('app', 'Invalid resource type'));
        }
        return $type;
    }

    public function GetJSONUrl($tmpdir, $url) {
        $fileData = '';
        $fileName = '';
        $path = '';
        if (file_exists($tmpdir . '/' . $url)) {
            $positionName = mb_strrpos($url, '/', 0, 'UTF-8');
            if ($positionName != NULL) {
                $fileName = mb_substr($url, $positionName + 1, mb_strlen($url, 'UTF-8'), 'UTF-8');
                $path = mb_substr($url, 0, $positionName + 1, 'UTF-8');
            } else {
                $fileName = $url;
            }
            $fileData = file_get_contents($tmpdir . '/' . $url);
        } else {
            //file not exists or it is http//...
        }
        return array($fileData, $fileName, $path);
    }

    public function FillQuestionResource($QuestionModel, $fileData, $fileName, $path, $file_type, $type, $start_up, $language_code, &$CurrentResources) {
        $language = Language::model()->find("short=:short", array(':short' => $language_code));
        if ($language == null) {
            throw new CHttpException(405, Yii::t('app', 'Language code is not exists'));
        }
        $questionResource = QuestionResource::model()->find('question_id=:question_id and language_id=:language_id and path=:path and filename=:filename', array(':question_id' => $QuestionModel->id, ':language_id' => $language->id, ':path' => $path, ':filename' => $fileName));
        if ($questionResource == null) {
            $questionResource = new QuestionResource();
            $questionResource->question_id = $QuestionModel->id;
            $questionResource->language_id = $language->id;
            $questionResource->filename = $fileName;
            $questionResource->path = $path;
        }
        $questionResource->data = $fileData;
        $questionResource->file_type = $file_type;
        $questionResource->type = $type;
        $questionResource->start_up = $start_up;
        if ($questionResource->save()) {
            //Saved OK
            $CurrentResources[$questionResource->id] = true;
        } else {
            throw new CHttpException(405, Yii::t('app', 'Save question resource failed'));
        }
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
// Warning: Please modify the following code to remove attributes that
// should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('country_id', $this->country_id);
        if ($this->type == 0) {
            $this->type = NULL;
        }
        $criteria->compare('identifier', $this->identifier, true);
        $criteria->compare('type', $this->type);
        $criteria->compare('title', $this->title, true);
        $criteria->compare('text', $this->text, true);
        $criteria->compare('data', $this->data, true);
        $criteria->compare('version', $this->version, true);
        $criteria->compare('verification_function_type', $this->verification_function_type);
        $criteria->compare('verification_function', $this->verification_function, true);
        $criteria->compare('last_change_date', $this->last_change_date, true);
        $criteria->compare('authors', $this->authors, true);
        $criteria->together = true;
        $criteria->with = array('country');
        $criteria->compare('`country`.`country`', $this->country_search, true);

        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            // ok
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
                $criteria->with[] = 'country.countryAdministrators';
                $criteria->compare('`countryAdministrators`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }
        }

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'attributes' => array(
                    'country_search' => array(
                        'asc' => 'country.name',
                        'desc' => 'country.name DESC'
                    ),
                    '*',
                )
            ),
        );
        if ($pagination == false) {
            $options['pagination'] = false;
        }

        return new CActiveDataProvider($this, $options);
    }

    public function beforeSave() {
        $this->last_change_date = new CDbExpression('NOW()');
        return parent::beforeSave();
    }

}
