<?php

/**
 * This is the model class for table "competition_category".
 *
 * The followings are the available columns in table 'competition_category':
 * @property integer $id
 * @property integer $active
 * @property integer $country_id
 * @property string $name
 * @property integer $level_of_education
 * @property integer $class_from
 * @property integer $class_to
 *
 * The followings are the available model relations:
 * @property Country $country
 * @property CompetitionCategoryActive[] $competitionCategoryActives
 * @property CompetitionCategorySchool[] $competitionCategorySchools
 * @property CompetitionCategoryTranslation[] $competitionCategoryTranslations
 * @property CompetitionQuestionCategory[] $competitionQuestionCategories
 * @property CompetitionUser[] $competitionUsers
 */
class CompetitionCategory extends CActiveRecord {

    public $search_action;
    public $search_category;
    public $search_education;
    public $country_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionCategory the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_category';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name, class_from, class_to', 'required'),
            array('active, country_id, level_of_education, class_from, class_to', 'numerical', 'integerOnly' => true),
            array('name', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, active, country_id, name, level_of_education, class_from, class_to, country_search', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'country' => array(self::BELONGS_TO, 'Country', 'country_id'),
            'competitionCategoryActives' => array(self::HAS_MANY, 'CompetitionCategoryActive', 'competition_category_id'),
            'competitionCategorySchools' => array(self::HAS_MANY, 'CompetitionCategorySchool', 'competition_category_id'),
            'competitionCategoryTranslations' => array(self::HAS_MANY, 'CompetitionCategoryTranslation', 'competition_category_id'),
            'competitionQuestionCategories' => array(self::HAS_MANY, 'CompetitionQuestionCategory', 'competition_category_id'),
            'competitionUsers' => array(self::HAS_MANY, 'CompetitionUser', 'competition_category_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'active' => Yii::t('app', 'Active'),
            'country_id' => Yii::t('app', 'Country'),
            'name' => Yii::t('app', 'Competition Category Name'),
            'level_of_education' => Yii::t('app', 'Level of Education'),
            'class_from' => Yii::t('app', 'Class from'),
            'class_to' => Yii::t('app', 'Class to'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $superuser = Generic::isSuperAdmin();

        if ($superuser) {
            return true;
            /*
            if ($user != null && $user->profile->user_role == 10) {
                $countryAdministratorCheck = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $this->country_id));

                $change_to_country_id = isset($_POST['CompetitionCategory']['country_id']) ? $_POST['CompetitionCategory']['country_id'] : -1;
                $countryAdministratorCheck2 = CountryAdministrator::model()->find('user_id=:user_id and country_id=:country_id', array(':user_id' => Yii::app()->user->id, ':country_id' => $change_to_country_id));

                if (($countryAdministratorCheck != null && $countryAdministratorCheck2 != null) || ($countryAdministratorCheck2 != null && $change_to_country_id != -1) || ($countryAdministratorCheck != null && $change_to_country_id == -1)) {
                    return true;
                }
            }*/
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

    public function GetLevelsOfEducation($empty = false) {
        $options = array(
            1 => Yii::t('app', 'Primary School'),
            2 => Yii::t('app', 'Secondary School'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All Levels'));
        }
        return $options;
    }

    public function GetLevelsOfEducationName($id) {
        $levels = $this->GetLevelsOfEducation();
        if (isset($levels[$id])) {
            return $levels[$id];
        }
        return '';
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        if ($this->level_of_education == 0) {
            $this->level_of_education = NULL;
        }
        $criteria->compare('id', $this->id);
        $criteria->compare('active', $this->active);
        $criteria->compare('country_id', $this->country_id);
        $criteria->compare('name', $this->name, true);
        $criteria->compare('level_of_education', $this->level_of_education);
        $criteria->compare('class_from', $this->class_from);
        $criteria->compare('class_to', $this->class_to);
        $criteria->together = true;
        $criteria->with = array('country');
        $criteria->compare('`country`.`country`', $this->country_search, true);

        $superuser = Generic::isSuperAdmin();
        $user_role = Generic::getUserRole();

        if ($superuser) {
            // ok
        } else {
            if ($user_role == 10) {
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

        if ($pagination == false) {
            $options['pagination'] = false;
        }

        return new CActiveDataProvider($this, $options);
    }

}