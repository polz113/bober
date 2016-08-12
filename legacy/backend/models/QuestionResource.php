<?php

/**
 * This is the model class for table "question_resource".
 *
 * The followings are the available columns in table 'question_resource':
 * @property integer $id
 * @property integer $question_id
 * @property integer $language_id
 * @property string $path
 * @property integer $type
 * @property string $filename
 * @property string $file_type
 * @property string $data
 * @property integer $start_up
 *
 * The followings are the available model relations:
 * @property Question $question
 * @property Language $language
 */
class QuestionResource extends CActiveRecord {

    public $uploadedData;
    public $question_search;
    public $language_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return QuestionResource the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'question_resource';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('question_id, language_id, type', 'required'),
            array('question_id, language_id, type, start_up', 'numerical', 'integerOnly' => true),
            array('filename, path', 'length', 'max' => 250),
            array('file_type', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, question_id, filename, file_type, data, path, type, start_up, question_search, language_search', 'safe', 'on' => 'search'),
            array('uploadedData', 'file', 'types' => 'jpg, gif, png, html, js, css', 'allowEmpty' => true),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'language' => array(self::BELONGS_TO, 'Language', 'language_id'),
            'question' => array(self::BELONGS_TO, 'Question', 'question_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'question_id' => Yii::t('app', 'Question'),
            'language_id' => Yii::t('app', 'Language'),
            'type' => Yii::t('app', 'Type Resource'),
            'path' => Yii::t('app', 'File Path'),
            'filename' => Yii::t('app', 'File Name'),
            'file_type' => Yii::t('app', 'File Type'),
            'data' => Yii::t('app', 'Data'),
            'start_up' => Yii::t('app', 'Start Up'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;
        
        if($superuser == 1 || $user->profile->user_role >= 10){
            return true;
        }
        
        $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
        // demo
        if ($competition_user_id == 0) {
            $competition_user_id = 1;
        }
        
        if ($competition_user_id != 0) {
            return true;
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

    public function GetQuestionTitleId() {
        return $this->question->title . ' ( id: ' . $this->question->id . ' )';
    }

    public function GetQuestionTitleIdList() {
        $modelData = Question::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $question) {
            $question['title'] = $question->title . ' ( id: ' . $question->id . ' )';
            $list[] = $question;
        }
        return $list;
    }

    public function GetLanguageIdList() {
        $modelData = Language::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $language) {
            $language['name'] = $language->name;
            $list[] = $language;
        }
        return $list;
    }

    public function formatSizeUnits($bytes) {
        if ($bytes >= 1073741824) {
            $bytes = number_format($bytes / 1073741824, 2) . ' GB';
        } elseif ($bytes >= 1048576) {
            $bytes = number_format($bytes / 1048576, 2) . ' MB';
        } elseif ($bytes >= 1024) {
            $bytes = number_format($bytes / 1024, 2) . ' KB';
        } elseif ($bytes > 1) {
            $bytes = $bytes . ' B';
        } elseif ($bytes == 1) {
            $bytes = $bytes . ' B';
        } else {
            $bytes = '0 B';
        }

        return $bytes;
    }

    public function GetSize($data) {
        return $this->formatSizeUnits(strlen($data));
    }

    public function GetResourceType($empty = false) {
        $options = array(
            1 => Yii::t('app', 'Task'),
            2 => Yii::t('app', 'Solution'),
            3 => Yii::t('app', 'Grader'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All Types'));
        }
        return $options;
    }

    public function GetResourceTypeName($id) {
        $types = $this->GetResourceType();
        if (isset($types[$id])) {
            return $types[$id];
        }
        return '';
    }

    protected function beforeSave() {
        if ($file = CUploadedFile::getInstance($this, 'uploadedData')) {
            if ($this->filename == '') {
                $this->filename = $file->name;
            }
            if ($this->file_type == '') {
                $this->file_type = $file->type;
            }
            // $this->file_size = $file->size;
            $this->data = file_get_contents($file->tempName);
        }

        return parent::beforeSave();
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;
        if ($this->type == 0) {
            $this->type = NULL;
        }
        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`question_id`', $this->question_id);
        $criteria->compare('t.`language_id`', $this->language_id);
        $criteria->compare('t.`type`', $this->type);
        $criteria->compare('t.`path`', $this->path, true);
        $criteria->compare('t.`filename`', $this->filename, true);
        $criteria->compare('t.`file_type`', $this->file_type, true);
        $criteria->compare('t.`data`', $this->data, true);
        $criteria->compare('t.`start_up`', $this->start_up);
        $criteria->with = array('question', 'language');
        $criteria->together = true;
        $criteria->compare('question.title', $this->question_search, true, 'OR');
        $criteria->compare('question.`id`', $this->question_search, false, 'OR');
        $criteria->compare('language.name', $this->language_search, true);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'attributes' => array(
                    'question_search' => array(
                        'asc' => 'question.title',
                        'desc' => 'question.title DESC',
                    ),
                    'language_search' => array(
                        'asc' => 'language.name',
                        'desc' => 'language.name DESC',
                    ),
                    '*',
                )
            ),
        );
        
        if($pagination == false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this,$options);
    }

}