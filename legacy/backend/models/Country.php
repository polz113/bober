<?php

/**
 * This is the model class for table "country".
 *
 * The followings are the available columns in table 'country':
 * @property integer $id
 * @property string $country
 *
 * The followings are the available model relations:
 * @property CompetitionCategory[] $competitionCategories
 * @property CompetitionCountry[] $competitionCountries
 * @property CompetitionQuestionDifficulty[] $competitionQuestionDifficulties
 * @property CountryAdministrator[] $countryAdministrators
 * @property Municipality[] $municipalities
 * @property Profiles[] $profiles
 * @property Region[] $regions
 * @property School[] $schools
 */
class Country extends CActiveRecord {

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return Country the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'country';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('country', 'required'),
            array('country', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, country', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionCategories' => array(self::HAS_MANY, 'CompetitionCategory', 'country_id'),
            'competitionCountries' => array(self::HAS_MANY, 'CompetitionCountry', 'country_id'),
            'competitionQuestionDifficulties' => array(self::HAS_MANY, 'CompetitionQuestionDifficulty', 'country_id'),
            'countryAdministrators' => array(self::HAS_MANY, 'CountryAdministrator', 'country_id'),
            'municipalities' => array(self::HAS_MANY, 'Municipality', 'country_id'),
            'profiles' => array(self::HAS_MANY, 'Profiles', 'country_id'),
            'regions' => array(self::HAS_MANY, 'Region', 'country_id'),
            'schools' => array(self::HAS_MANY, 'School', 'country_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'country' => Yii::t('app', 'country'),
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

    public function GetCountriesICanEdit() {
        $modelData = $this->search(true);
        $list = array();
        foreach ($modelData->getData() as $country) {
            $list[] = $country;
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

        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`country`', $this->country, true);

        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            // ok
        } else {
            if ($user != null && $user->profile->user_role == 10) {
                // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
                $criteria->with[] = 'countryAdministrators';
                $criteria->compare('`countryAdministrators`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }
        }

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