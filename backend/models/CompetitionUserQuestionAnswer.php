<?php

/**
 * This is the model class for table "competition_user_question_answer".
 *
 * The followings are the available columns in table 'competition_user_question_answer':
 * @property integer $id
 * @property integer $competition_user_question_id
 * @property integer $question_answer_id
 * @property integer $ordering
 *
 * The followings are the available model relations:
 * @property CompetitionUserQuestion $competitionUserQuestion
 * @property QuestionAnswer $questionAnswer
 */
class CompetitionUserQuestionAnswer extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return CompetitionUserQuestionAnswer the static model class
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
		return 'competition_user_question_answer';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('competition_user_question_id, question_answer_id, ordering', 'required'),
			array('competition_user_question_id, question_answer_id, ordering', 'numerical', 'integerOnly'=>true),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, competition_user_question_id, question_answer_id, ordering', 'safe', 'on' => 'search'),
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
			'competitionUserQuestion' => array(self::BELONGS_TO, 'CompetitionUserQuestion', 'competition_user_question_id'),
			'questionAnswer' => array(self::BELONGS_TO, 'QuestionAnswer', 'question_answer_id'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'competition_user_question_id' => Yii::t('app', 'competition_user_question_id'),
			'question_answer_id' => Yii::t('app', 'question_answer_id'),
			'ordering' => Yii::t('app', 'ordering'),
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
		$criteria->compare('competition_user_question_id', $this->competition_user_question_id);
		$criteria->compare('question_answer_id', $this->question_answer_id);
		$criteria->compare('ordering', $this->ordering);

		return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}