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
 * @property Users $user
 * @property Users $activatedBy
 */
class SchoolMentorConfirmation extends CActiveRecord
{
	public $user_search;
        public $school_search;
        
        /**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return SchoolMentorConfirmation the static model class
	 */
	public static function model($className=__CLASS__)
	{
		return parent::model($className);
	}

	/**
	 * @return string the associated database table name
	 */
	public function tableName()
	{
		return 'school_mentor';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('school_id, user_id', 'required'),
			array('school_id, user_id, active, activated_by, coordinator', 'numerical', 'integerOnly'=>true),
			array('activated_timestamp', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, school_id, user_id, active, activated_by, activated_timestamp, coordinator, user_search, school_search', 'safe', 'on' => 'search'),
		);
	}

	/**
	 * @return array relational rules.
	 */
	public function relations()
	{
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
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'school_id' => Yii::t('app', 'school_id'),
			'user_id' => Yii::t('app', 'user_id'),
			'active' => Yii::t('app', 'active'),
			'activated_by' => Yii::t('app', 'activated_by'),
			'activated_timestamp' => Yii::t('app', 'activated_timestamp'),
			'coordinator' => Yii::t('app', 'coordinator'),
		);
	}
    
    public function getCanView()
    {
        return $this->CanView();
    }

    public function CanView()
    {
        return false;
    }

    public function getCanUpdate()
    {
        return $this->CanUpdate();
    }

    public function CanUpdate()
    {
        return false;
    }

    public function getCanDelete()
    {
        return $this->CanDelete();
    }

    public function CanDelete()
    {
        return true;
    }
    
    public function getCanActivate(){
        return $this->CanActivate();
    }
    
    public function CanActivate(){
        return true;
    }
    
    /**
	 * Retrieves a list of models based on the current search/filter conditions.
	 * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
	 */
	public function search()
	{
		// Warning: Please modify the following code to remove attributes that
		// should not be searched.

		$criteria = new CDbCriteria;

		$criteria->compare('id', $this->id);
		$criteria->compare('school_id', $this->school_id);
		$criteria->compare('user_id', $this->user_id);
		$criteria->compare('active', 0);
		$criteria->compare('activated_by', $this->activated_by);
		$criteria->compare('activated_timestamp', $this->activated_timestamp, true);
		$criteria->compare('coordinator', 1);
                $criteria->together = true;
                $criteria->with = array('user', 'user.profile','school');
                $criteria->compare('CONCAT_WS(\' \', `profile`.`last_name`, `profile`.`first_name`)', $this->user_search, true);
                $criteria->compare('CONCAT_WS(\' - \', `school`.`name`)', $this->school_search, true);
		
                $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;
        
        if ($superuser == 1) {
            // ok
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
                $criteria->with[] = 'school.country';
                $criteria->with[] = 'school.country.countryAdministrators';
                $criteria->compare('`countryAdministrators`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }
            else{
                throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
            }
        }
                
                return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}