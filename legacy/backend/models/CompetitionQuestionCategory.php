<?php

/**
 * This is the model class for table "competition_question_category".
 *
 * The followings are the available columns in table 'competition_question_category':
 * @property integer $id
 * @property integer $competition_question_id
 * @property integer $competition_category_id
 * @property integer $competiton_question_difficulty_id
 *
 * The followings are the available model relations:
 * @property CompetitionQuestion $competitionQuestion
 * @property CompetitionCategory $competitionCategory
 * @property CompetitionQuestionDifficulty $competitonQuestionDifficulty
 */
class CompetitionQuestionCategory extends CActiveRecord {

    public $competition_category_search;
    public $competition_question_difficulty_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionQuestionCategory the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_question_category';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('competition_question_id, competition_category_id, competiton_question_difficulty_id', 'required'),
            array('competition_question_id, competition_category_id, competiton_question_difficulty_id', 'numerical', 'integerOnly' => true),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, competition_question_id, competition_category_id, competiton_question_difficulty_id, competition_category_search, competition_question_difficulty_search', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionQuestion' => array(self::BELONGS_TO, 'CompetitionQuestion', 'competition_question_id'),
            'competitionCategory' => array(self::BELONGS_TO, 'CompetitionCategory', 'competition_category_id'),
            'competitionQuestionDifficulty' => array(self::BELONGS_TO, 'CompetitionQuestionDifficulty', 'competiton_question_difficulty_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'competition_question_id' => Yii::t('app', 'Competition Question'),
            'competition_category_id' => Yii::t('app', 'Competition Category'),
            'competiton_question_difficulty_id' => Yii::t('app', 'Competition Question Difficulty'),
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

    public function GetCompetitionCategoryNameIdList() {
        $modelData = CompetitionCategory::model()->search();
        $list = array();
        foreach ($modelData->getData() as $competitionCategory) {
            $competitionCategory['name'] = $competitionCategory->name;
            $list[] = $competitionCategory;
        }
        return $list;
    }

    public function GetCompetitionQuestionDifficultyNameIdList() {
        $modelData = CompetitionQuestionDifficulty::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competitionQuestionDifficulty) {
            $competitionQuestionDifficulty['name'] = $competitionQuestionDifficulty->name;
            $list[] = $competitionQuestionDifficulty;
        }
        return $list;
    }

    public function GetCompetitionQuestionName() {
        return $this->competitionQuestion->competition->name . ' - ' . $this->competitionQuestion->question->title;
    }

    public function GetCompetitionQuestionIdList() {
        $modelData = CompetitionQuestion::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competitionQuestion) {
            $competitionQuestion['competition_id'] = $competitionQuestion->id;
            // var_dump($competitionQuestion->competition);
            //echo"<br><BR><br><BR><br><BR><br><BR>";
            $competitionQuestion['id'] = $competitionQuestion->competition->name . ' - ' . $competitionQuestion->question->title;
            // $competitionQuestion['id'] = $competitionQuestion->competition->name . ' - ' . $competitionQuestion->question->title;
            $list[] = $competitionQuestion;
        }
        return $list;
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
        $criteria->compare('competition_question_id', $this->competition_question_id);
        $criteria->compare('competition_category_id', $this->competition_category_id);
        $criteria->compare('competiton_question_difficulty_id', $this->competiton_question_difficulty_id);
        $criteria->with = array('competitionCategory', 'competitionQuestionDifficulty', 'competitionQuestion', 'competitionQuestion.competition', 'competitionQuestion.question');
        $criteria->together = true;
        $criteria->compare('`competitionCategory`.`name`', $this->competition_category_search, true);
        $criteria->compare('`competitionQuestionDifficulty`.`name`', $this->competition_question_difficulty_search, true);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'defaultOrder'=>'competition.name ASC, question.title ASC, competitionCategory.name ASC, competitionQuestionDifficulty.name ASC',
                'attributes' => array(
                    'competition_category_search' => array(
                        'asc' => 'competitionCategory.name',
                        'desc' => 'competitionCategory.name DESC',
                    ),
                    'competition_question_difficulty_search' => array(
                        'asc' => 'competitionQuestionDifficulty.name',
                        'desc' => 'competitionQuestionDifficulty.name DESC',
                    ),
                    '*',
                ),
            ),
        );
        
        if($pagination == false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this, $options);
    }

}