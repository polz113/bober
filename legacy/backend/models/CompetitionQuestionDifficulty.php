<?php

/**
 * This is the model class for table "competition_question_difficulty".
 *
 * The followings are the available columns in table 'competition_question_difficulty':
 * @property integer $id
 * @property integer $country_id
 * @property integer $active
 * @property string $name
 * @property string $correct_answer_points
 * @property string $wrong_answer_points
 *
 * The followings are the available model relations:
 * @property CompetitionQuestionCategory[] $competitionQuestionCategories
 * @property Country $country
 * @property CompetitionQuestionDifficultyTranslation[] $competitionQuestionDifficultyTranslations
 */
class CompetitionQuestionDifficulty extends CActiveRecord {

    public $country_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionQuestionDifficulty the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_question_difficulty';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name', 'required'),
            array('country_id, active', 'numerical', 'integerOnly' => true),
            array('name', 'length', 'max' => 255),
            array('correct_answer_points, wrong_answer_points', 'length', 'max' => 10),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, country_id, active, name, correct_answer_points, wrong_answer_points, country_search', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionQuestionCategories' => array(self::HAS_MANY, 'CompetitionQuestionCategory', 'competiton_question_difficulty_id'),
            'country' => array(self::BELONGS_TO, 'Country', 'country_id'),
            'competitionQuestionDifficultyTranslations' => array(self::HAS_MANY, 'CompetitionQuestionDifficultyTranslation', 'competition_question_difficulty_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'country_id' => Yii::t('app', 'Country'),
            'active' => Yii::t('app', 'active'),
            'name' => Yii::t('app', 'Question Difficulty'),
            'correct_answer_points' => Yii::t('app', 'Correct Answer Points'),
            'wrong_answer_points' => Yii::t('app', 'Wrong Answer Points'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            return true;
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                $countryAdministratorCheck = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $this->country_id));

                $change_to_country_id = isset($_POST['School']['country_id']) ? $_POST['School']['country_id'] : -1;
                $countryAdministratorCheck2 = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $change_to_country_id));

                if (($countryAdministratorCheck != null && $countryAdministratorCheck2 != null) || ($countryAdministratorCheck2 != null && $change_to_country_id != -1) || ($countryAdministratorCheck != null && $change_to_country_id == -1)) {
                    return true;
                }
            }
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

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`country_id`', $this->country_id);
        $criteria->compare('t.`active`', $this->active);
        $criteria->compare('t.`name`', $this->name, true);
        $criteria->compare('t.`correct_answer_points`', $this->correct_answer_points, true);
        $criteria->compare('t.`wrong_answer_points`', $this->wrong_answer_points, true);
        $criteria->together = true;
        $criteria->with = array('country');
        $criteria->compare('`country`.`country`', $this->country_search, true);


        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            // ok
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
                $criteria->with[] = 'country.countryAdministrators';
                $criteria->compare('`countryAdministrators`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }
        }

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'attributes' => array(
                    'country_search' => array(
                        'asc' => 'country.name',
                        'desc' => 'country.name DESC'
                    ),
                    '*',
                )
            ),
        );
        
        if($pagination == false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this, $options);
    }

}