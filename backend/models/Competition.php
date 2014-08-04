<?php

/**
 * This is the model class for table "competition".
 *
 * The followings are the available columns in table 'competition':
 * @property integer $id
 * @property string $name
 * @property integer $active
 * @property string $timestamp_start
 * @property string $timestamp_stop
 * @property integer $type
 * @property integer $public_access
 * @property integer $duration
 * @property string $timestamp_mentor_results
 * @property string $timestamp_mentor_awards
 * @property string $timestamp_mentor_advancing_to_next_level
 *
 * The followings are the available model relations:
 * @property CompetitionCategoryActive[] $competitionCategoryActives
 * @property CompetitionCategorySchool[] $competitionCategorySchools
 * @property CompetitionCountry[] $competitionCountries
 * @property CompetitionCommittee[] $competitionCommittees
 * @property CompetitionQuestion[] $competitionQuestions
 * @property CompetitionTranslation[] $competitionTranslations
 * @property CompetitionUser[] $competitionUsers
 */
class Competition extends CActiveRecord {

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return Competition the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name, timestamp_start, timestamp_stop', 'required'),
            array('active, type, public_access, duration', 'numerical', 'integerOnly' => true),
            array('name', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, name, active, timestamp_start, timestamp_stop, timestamp_mentor_results, timestamp_mentor_awards, timestamp_mentor_advancing_to_next_level,  type, public_access, duration', 'safe', 'on' => 'search'),
        );
    }

    protected function beforeSave() {
        $current_timestamp_mentor_results = isset($_POST["Competition"]["timestamp_mentor_results"]) ? $_POST["Competition"]["timestamp_mentor_results"] : null;
        $current_timestamp_mentor_awards = isset($_POST["Competition"]["timestamp_mentor_awards"]) ? $_POST["Competition"]["timestamp_mentor_awards"] : null;
        $current_timestamp_mentor_advancing_to_next_level = isset($_POST["Competition"]["timestamp_mentor_advancing_to_next_level"]) ? $_POST["Competition"]["timestamp_mentor_advancing_to_next_level"] : null;
        if (parent::beforeSave()) {
            $explode1 = count(explode('activate', Yii::app()->request->requestUri)) > 1;
            $explode2 = count(explode('deactivate', Yii::app()->request->requestUri)) > 1;
            if ($explode1 || $explode2) {
                // do not change
                return true;
            } else {
                $this->timestamp_start = date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($this->timestamp_start, 'medium', 'short')));
                $this->timestamp_stop = date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($this->timestamp_stop, 'medium', 'short')));
                $this->timestamp_mentor_results = $current_timestamp_mentor_results != null && $current_timestamp_mentor_results != '' ? date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($current_timestamp_mentor_results, 'medium', 'short'))) : null;
                $this->timestamp_mentor_awards = $current_timestamp_mentor_awards != null && $current_timestamp_mentor_awards != '' ? date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($current_timestamp_mentor_awards, 'medium', 'short'))) : null;
                $this->timestamp_mentor_advancing_to_next_level = $current_timestamp_mentor_advancing_to_next_level != null && $current_timestamp_mentor_advancing_to_next_level != '' ? date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($current_timestamp_mentor_advancing_to_next_level, 'medium', 'short'))) : null;
            }
            
            return true;
        } else {
            return false;
        }
    }
    
    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionCategoryActives' => array(self::HAS_MANY, 'CompetitionCategoryActive', 'competition_id'),
            'competitionCategorySchools' => array(self::HAS_MANY, 'CompetitionCategorySchool', 'competition_id'),
            'competitionCountries' => array(self::HAS_MANY, 'CompetitionCountry', 'competition_id'),
            'competitionQuestions' => array(self::HAS_MANY, 'CompetitionQuestion', 'competition_id'),
            'competitionTranslations' => array(self::HAS_MANY, 'CompetitionTranslation', 'competition_id'),
            'competitionUsers' => array(self::HAS_MANY, 'CompetitionUser', 'competition_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'name' => Yii::t('app', 'Competition Name'),
            'active' => Yii::t('app', 'Active'),
            'timestamp_start' => Yii::t('app', 'Start of Competition'),
            'timestamp_stop' => Yii::t('app', 'Stop of Competition'),
            'type' => Yii::t('app', 'Competition Type'),
            'public_access' => Yii::t('app', 'Public Access'),
            'duration' => Yii::t('app', 'Duration'),
            'timestamp_mentor_results' => Yii::t('app', 'Timestamp when mentors can see results'),
            'timestamp_mentor_awards' => Yii::t('app', 'Timestamp when mentors can see awards'),
            'timestamp_mentor_advancing_to_next_level' => Yii::t('app', 'Timestamp when mentors can see who is advancing to next level')
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $superuser = Generic::isSuperAdmin();
        $user_role = Generic::getUserRole();
        if ($superuser || $user_role >= 10) {
            return true;
        }
        return false;
    }

    public function getCanUpdate() {
        return $this->CanUpdate();
    }

    public function CanUpdate() {
        return $this->CanView();
        ;
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        return $this->CanView();
    }

    public function GetTypeOfCompetition($empty = false) {
        $options = array(
            1 => Yii::t('app', 'School Competition'),
            2 => Yii::t('app', 'National Competition'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All Types'));
        }

        return $options;
    }

    public function GetTypeOfCompetitionName($id) {
        $type = $this->GetTypeOfCompetition();
        if (isset($type[$id])) {
            return $type[$id];
        }
        return '';
    }

    public function GetPublicAccess($empty = false) {
        $options = array(
            1 => Yii::t('app', 'yes'),
            2 => Yii::t('app', 'no'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All'));
        }
        return $options;
    }

    public function GetPublicAccessName($id) {
        $access = $this->GetPublicAccess();
        if (isset($access[$id])) {
            return $access[$id];
        }
        return '';
    }

    public function save($runValidation = true, $attributes = null) {

        return parent::save($runValidation, $attributes);
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
        if ($this->public_access == 0) {
            $this->public_access = NULL;
        }
        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`name`', $this->name, true);
        $criteria->compare('t.`active`', $this->active);
        $criteria->compare('t.`timestamp_start`', $this->timestamp_start, true);
        $criteria->compare('t.`timestamp_stop`', $this->timestamp_stop, true);
        $criteria->compare('t.`type`', $this->type);
        $criteria->compare('t.`public_access`', $this->public_access);
        $criteria->compare('t.`duration`', $this->duration);
        $criteria->compare('t.`timestamp_mentor_results`', $this->timestamp_mentor_results);
        $criteria->compare('t.`timestamp_mentor_awards`', $this->timestamp_mentor_awards);
        $criteria->compare('t.`timestamp_mentor_advancing_to_next_level`', $this->timestamp_mentor_advancing_to_next_level);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $criteria->order = 't.`name` asc';

        $options = array('criteria' => $criteria);

        if ($pagination == false) {
            $options['pagination'] = false;
        }

        return new CActiveDataProvider($this, $options);
    }

}
