<?php

/**
 * This is the model class for table "convert".
 *
 * The followings are the available columns in table 'convert':
 * @property integer $id
 * @property integer $user_id
 * @property string $svg
 * @property string $data
 * @property string $data_type
 * @property string $data_encoding
 * @property string $data_parameters
 * @property string $data_to_use
 * @property integer $background
 * @property integer $backgroud_job_set_id
 * @property string $result
 *
 * The followings are the available model relations:
 * @property User $user
 * @property JobSet $backgroudJobSet
 */
class Convert extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Convert the static model class
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
		return 'convert';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('user_id, svg', 'required'),
			array('user_id, background, backgroud_job_set_id', 'numerical', 'integerOnly'=>true),
			array('data_type', 'length', 'max'=>10),
			array('data_encoding', 'length', 'max'=>50),
			array('data_parameters', 'length', 'max'=>255),
			array('data, data_to_use, result', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, user_id, svg, data, data_type, data_encoding, data_parameters, data_to_use, background, backgroud_job_set_id, result', 'safe', 'on' => 'search'),
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
			'user' => array(self::BELONGS_TO, 'User', 'user_id'),
			'backgroudJobSet' => array(self::BELONGS_TO, 'JobSet', 'backgroud_job_set_id'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'user_id' => Yii::t('app', 'user_id'),
			'svg' => Yii::t('app', 'svg'),
			'data' => Yii::t('app', 'data'),
			'data_type' => Yii::t('app', 'data_type'),
			'data_encoding' => Yii::t('app', 'data_encoding'),
			'data_parameters' => Yii::t('app', 'data_parameters'),
			'data_to_use' => Yii::t('app', 'data_to_use'),
			'background' => Yii::t('app', 'background'),
			'backgroud_job_set_id' => Yii::t('app', 'backgroud_job_set_id'),
			'result' => Yii::t('app', 'result'),
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
		$criteria->compare('user_id', $this->user_id);
		$criteria->compare('svg', $this->svg, true);
		$criteria->compare('data', $this->data, true);
		$criteria->compare('data_type', $this->data_type, true);
		$criteria->compare('data_encoding', $this->data_encoding, true);
		$criteria->compare('data_parameters', $this->data_parameters, true);
		$criteria->compare('data_to_use', $this->data_to_use, true);
		$criteria->compare('background', $this->background);
		$criteria->compare('backgroud_job_set_id', $this->backgroud_job_set_id);
		$criteria->compare('result', $this->result, true);

		return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}