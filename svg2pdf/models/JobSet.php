<?php

/**
 * This is the model class for table "job_set".
 *
 * The followings are the available columns in table 'job_set':
 * @property integer $id
 * @property string $hash
 * @property string $starttime
 * @property string $finishtime
 * @property integer $needed
 * @property integer $final_job_result_id
 *
 * The followings are the available model relations:
 * @property Job[] $jobs
 * @property Job $finalJobResult
 */
class JobSet extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return JobSet the static model class
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
		return 'job_set';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('hash', 'required'),
			array('needed, final_job_result_id', 'numerical', 'integerOnly'=>true),
			array('hash', 'length', 'max'=>255),
			array('starttime, finishtime', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, hash, starttime, finishtime, needed, final_job_result_id', 'safe', 'on' => 'search'),
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
			'jobs' => array(self::HAS_MANY, 'Job', 'job_set_id'),
			'finalJobResult' => array(self::BELONGS_TO, 'Job', 'final_job_result_id'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'hash' => Yii::t('app', 'hash'),
			'starttime' => Yii::t('app', 'starttime'),
			'finishtime' => Yii::t('app', 'finishtime'),
			'needed' => Yii::t('app', 'needed'),
			'final_job_result_id' => Yii::t('app', 'final_job_result_id'),
		);
	}
    
    public function getCanView()
    {
        return $this->CanView();
    }

    public function CanView()
    {
        return true;
    }

    public function getCanUpdate()
    {
        return $this->CanUpdate();
    }

    public function CanUpdate()
    {
        return true;
    }

    public function getCanDelete()
    {
        return $this->CanDelete();
    }

    public function CanDelete()
    {
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
		$criteria->compare('hash', $this->hash, true);
		$criteria->compare('starttime', $this->starttime, true);
		$criteria->compare('finishtime', $this->finishtime, true);
		$criteria->compare('needed', $this->needed);
		$criteria->compare('final_job_result_id', $this->final_job_result_id);

		return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}