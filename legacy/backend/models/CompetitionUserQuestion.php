<?php

/**
 * This is the model class for table "competition_user_question".
 *
 * The followings are the available columns in table 'competition_user_question':
 * @property integer $id
 * @property integer $competition_user_id
 * @property integer $competition_question_id
 * @property integer $ordering
 * @property integer $question_answer_id
 * @property string $last_change
 * @property string $random_seed
 * @property string $custom_answer
 *
 * The followings are the available model relations:
 * @property CompetitionUser $competitionUser
 * @property CompetitionQuestion $competitionQuestion
 * @property QuestionAnswer $questionAnswer
 * @property CompetitionUserQuestionAnswer[] $competitionUserQuestionAnswers
 */
class CompetitionUserQuestion extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return CompetitionUserQuestion the static model class
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
		return 'competition_user_question';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('competition_user_id, competition_question_id, ordering', 'required'),
			array('competition_user_id, competition_question_id, ordering, question_answer_id', 'numerical', 'integerOnly'=>true),
			array('random_seed', 'length', 'max'=>11),
			array('last_change, custom_answer', 'safe'),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, competition_user_id, competition_question_id, ordering, question_answer_id, last_change, random_seed, custom_answer', 'safe', 'on' => 'search'),
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
			'competitionUser' => array(self::BELONGS_TO, 'CompetitionUser', 'competition_user_id'),
			'competitionQuestion' => array(self::BELONGS_TO, 'CompetitionQuestion', 'competition_question_id'),
			'questionAnswer' => array(self::BELONGS_TO, 'QuestionAnswer', 'question_answer_id'),
			'competitionUserQuestionAnswers' => array(self::HAS_MANY, 'CompetitionUserQuestionAnswer', 'competition_user_question_id'),
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => Yii::t('app', 'id'),
			'competition_user_id' => Yii::t('app', 'competition_user_id'),
			'competition_question_id' => Yii::t('app', 'competition_question_id'),
			'ordering' => Yii::t('app', 'ordering'),
			'question_answer_id' => Yii::t('app', 'question_answer_id'),
			'last_change' => Yii::t('app', 'last_change'),
			'random_seed' => Yii::t('app', 'random_seed'),
			'custom_answer' => Yii::t('app', 'custom_answer'),
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
		$criteria->compare('competition_user_id', $this->competition_user_id);
		$criteria->compare('competition_question_id', $this->competition_question_id);
		$criteria->compare('ordering', $this->ordering);
		$criteria->compare('question_answer_id', $this->question_answer_id);
		$criteria->compare('last_change', $this->last_change, true);
		$criteria->compare('random_seed', $this->random_seed, true);
		$criteria->compare('custom_answer', $this->custom_answer, true);

		return new CActiveDataProvider($this, array(
			'criteria' => $criteria,
		));
	}
}