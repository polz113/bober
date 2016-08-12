<?php

/**
 * This is the model class for table "question_answer".
 *
 * The followings are the available columns in table 'question_answer':
 * @property integer $id
 * @property integer $question_id
 * @property integer $type
 * @property string $value
 *
 * The followings are the available model relations:
 * @property CompetitionUserQuestion[] $competitionUserQuestions
 * @property CompetitionUserQuestionAnswer[] $competitionUserQuestionAnswers
 * @property Question $question
 * @property QuestionAnswerTranslation[] $questionAnswerTranslations
 */
class QuestionAnswer extends CActiveRecord {

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return QuestionAnswer the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'question_answer';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('question_id, value', 'required'),
            array('question_id, type', 'numerical', 'integerOnly' => true),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, question_id, type, value', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionUserQuestions' => array(self::HAS_MANY, 'CompetitionUserQuestion', 'question_answer_id'),
            'competitionUserQuestionAnswers' => array(self::HAS_MANY, 'CompetitionUserQuestionAnswer', 'question_answer_id'),
            'question' => array(self::BELONGS_TO, 'Question', 'question_id'),
            'questionAnswerTranslations' => array(self::HAS_MANY, 'QuestionAnswerTranslation', 'question_answer_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'question_id' => Yii::t('app', 'question_id'),
            'type' => Yii::t('app', 'type'),
            'value' => Yii::t('app', 'value'),
        );
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
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('question_id', $this->question_id);
        $criteria->compare('type', $this->type);
        $criteria->compare('value', $this->value, true);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }
        
        $options = array('criteria' => $criteria);
        
        if($pagination == false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this, $options);
    }

}