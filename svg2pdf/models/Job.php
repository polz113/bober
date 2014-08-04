<?php

/**
 * This is the model class for table "job".
 *
 * The followings are the available columns in table 'job':
 * @property integer $id
 * @property integer $job_set_id
 * @property string $parameters
 * @property string $enqueue
 * @property integer $started
 * @property string $starttime
 * @property integer $timeout
 * @property integer $finished
 * @property string $finishtime
 * @property string $result
 * @property integer $needed
 *
 * The followings are the available model relations:
 * @property JobSet $jobSet
 * @property JobSet[] $jobSets
 */
class Job extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Job the static model class
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
		return 'job';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('job_set_id', 'required'),
			array('job_set_id, started, timeout, finished, needed', 'numerical', 'integerOnly'=>true),
			array('parameters, enqueue, starttime, finishtime, result', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, job_set_id, parameters, enqueue, started, starttime, timeout, finished, finishtime, result, needed', 'safe', 'on' => 'search'),
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
			'jobSet' => array(self::BELONGS_TO, 'JobSet', 'job_set_id'),
			'jobSets' => array(self::HAS_MANY, 'JobSet', 'final_job_result_id'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'job_set_id' => Yii::t('app', 'job_set_id'),
			'parameters' => Yii::t('app', 'parameters'),
			'enqueue' => Yii::t('app', 'enqueue'),
			'started' => Yii::t('app', 'started'),
			'starttime' => Yii::t('app', 'starttime'),
			'timeout' => Yii::t('app', 'timeout'),
			'finished' => Yii::t('app', 'finished'),
			'finishtime' => Yii::t('app', 'finishtime'),
			'result' => Yii::t('app', 'result'),
			'needed' => Yii::t('app', 'needed'),
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
		$criteria->compare('job_set_id', $this->job_set_id);
		$criteria->compare('parameters', $this->parameters, true);
		$criteria->compare('enqueue', $this->enqueue, true);
		$criteria->compare('started', $this->started);
		$criteria->compare('starttime', $this->starttime, true);
		$criteria->compare('timeout', $this->timeout);
		$criteria->compare('finished', $this->finished);
		$criteria->compare('finishtime', $this->finishtime, true);
		$criteria->compare('result', $this->result, true);
		$criteria->compare('needed', $this->needed);

		return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}