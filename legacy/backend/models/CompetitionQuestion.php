<?php

/**
 * This is the model class for table "competition_question".
 *
 * The followings are the available columns in table 'competition_question':
 * @property integer $id
 * @property integer $competition_id
 * @property integer $question_id
 *
 * The followings are the available model relations:
 * @property Competition $competition
 * @property Question $question
 * @property CompetitionQuestionCategory[] $competitionQuestionCategories
 * @property CompetitionUserQuestion[] $competitionUserQuestions
 */
class CompetitionQuestion extends CActiveRecord {

    public $question_search;
    public $competition_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionQuestion the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_question';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('competition_id, question_id', 'required'),
            array('competition_id, question_id', 'numerical', 'integerOnly' => true),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, competition_id, question_id, competition_search, question_search', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competition' => array(self::BELONGS_TO, 'Competition', 'competition_id'),
            'question' => array(self::BELONGS_TO, 'Question', 'question_id'),
            'competitionQuestionCategories' => array(self::HAS_MANY, 'CompetitionQuestionCategory', 'competition_question_id'),
            'competitionUserQuestions' => array(self::HAS_MANY, 'CompetitionUserQuestion', 'competition_question_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'competition_id' => Yii::t('app', 'Competition'),
            'question_id' => Yii::t('app', 'Question'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1 || $user->profile->user_role >= 10) {
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

    public function GetCompetitionNameIdList() {
        $modelData = Competition::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competition) {
            $competition['name'] = $competition->name;
            $list[] = $competition;
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
        $criteria->compare('competition_id', $this->competition_id);
        $criteria->compare('question_id', $this->question_id);
        $criteria->with = array('competition', 'question');
        $criteria->together = true;
        $criteria->compare('`competition`.`name`', $this->competition_search, true);
        $criteria->compare('`question`.`title`', $this->question_search, true);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'defaultOrder' => 'competition.name ASC, question.title ASC',
                'attributes' => array(
                    'competition_search' => array(
                        'asc' => 'competition.name',
                        'desc' => 'competition.name DESC',
                    ),
                    'question_search' => array(
                        'asc' => 'question.title',
                        'desc' => 'question.title DESC',
                    ),
                    '*',
                ),
            ),
        );

        if ($pagination == false) {
            $options['pagination'] = false;
        }
        return new CActiveDataProvider($this, $options);
    }

    public static function getQuestionTitle($competitionQuestionId) {
        $cache_key = 'CompetitionQuestionTitle#' . $competitionQuestionId;
        $cached = Yii::app()->cache->get($cache_key);
        if ($cached == null) {
            $competitionQuestion = CompetitionQuestion::model()->findByPk($competitionQuestionId);
            if ($competitionQuestion != null) {
                $cached = $competitionQuestion->question->title;
            } else {
                $cached = '';
            }
            Yii::app()->cache->set($cache_key, $cached, 600);
        }
        return $cached;
    }

}
