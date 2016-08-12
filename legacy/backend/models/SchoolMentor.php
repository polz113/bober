<?php

/**
 * This is the model class for table "school_mentor".
 *
 * The followings are the available columns in table 'school_mentor':
 * @property integer $id
 * @property integer $school_id
 * @property integer $user_id
 * @property integer $active
 * @property integer $activated_by
 * @property string $activated_timestamp
 * @property integer $coordinator
 *
 * The followings are the available model relations:
 * @property School $school
 * @property User $user
 * @property User $activatedBy
 */
class SchoolMentor extends CActiveRecord {
    
    public $mentor_name;
    public $school_name;
        

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return SchoolMentor the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'school_mentor';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('school_id, user_id', 'required'),
            array('school_id, user_id, active, activated_by, coordinator', 'numerical', 'integerOnly' => true),
            array('activated_timestamp', 'safe'),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, school_id, user_id, active, activated_by, activated_timestamp, coordinator, mentor_name, school_name', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'school' => array(self::BELONGS_TO, 'School', 'school_id'),
            'user' => array(self::BELONGS_TO, 'User', 'user_id'),
            'activatedBy' => array(self::BELONGS_TO, 'User', 'activated_by'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'school_id' => Yii::t('app', 'School'),
            'user_id' => Yii::t('app', 'Mentor'),
            'active' => Yii::t('app', 'Active'),
            'activated_by' => Yii::t('app', 'Activated by'),
            'activated_timestamp' => Yii::t('app', 'Activated Timestamp'),
            'coordinator' => Yii::t('app', 'Coordinator'),
        );
    }

    public function IsCoordinator() {
        return $this->coordinator == 1;
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        return true;
    }

    public function getCanUpdate() {
        return $this->CanUpdate();
    }

    public function CanUpdate() {
        return true;
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        return true;
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search() {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('school_id', $this->school_id);
        if ($this->school_name != '') {
            $criteria->with[] = 'school';
            $criteria->compare('`school`.`name`', $this->school_name, true);
            $criteria->together = true;
        }
         if ($this->mentor_name != '') {
            $criteria->with[] = 'user.profile';
            $criteria->compare('CONCAT_WS(\' \', `profile`.`last_name`, `profile`.`first_name`)', $this->mentor_name, true);
            $criteria->together = true;
        }
        $criteria->compare('user_id', $this->user_id);
        $criteria->compare('active', $this->active);
        $criteria->compare('activated_by', $this->activated_by);
        $criteria->compare('activated_timestamp', $this->activated_timestamp, true);
        $criteria->compare('coordinator', $this->coordinator);

        return new CActiveDataProvider($this, array(
            'criteria' => $criteria,
        ));
    }
    
    public function GetSchoolName($id) {
        $school = School::model()->findByPk($id);
        if ($school != null) {
            return $school->name;
        }else{
            return '';
        }
    }
    
    public function GetTeacherName($id) {
        $user = User::model()->findByPk($id);
        if ($user != null) {
            return $user->profile->last_name . ' ' . $user->profile->first_name;
        }
        return '';
    }

}
