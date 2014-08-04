<?php

/**
 * This is the model class for table "municipality".
 *
 * The followings are the available columns in table 'municipality':
 * @property integer $id
 * @property string $name
 * @property integer $country_id
 *
 * The followings are the available model relations:
 * @property Country $country
 * @property School[] $schools
 */
class Municipality extends CActiveRecord {

    public $country_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return Municipality the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'municipality';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name, country_id', 'required'),
            array('country_id', 'numerical', 'integerOnly' => true),
            array('name', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, name, country_id, country_search', 'safe', 'on' => 'search'),
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
            'schools' => array(self::HAS_MANY, 'School', 'municipality_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'name' => Yii::t('app', 'Municipality name'),
            'country_id' => Yii::t('app', 'Country'),
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

                $change_to_country_id = isset($_POST['Municipality']['country_id']) ? $_POST['Municipality']['country_id'] : -1;
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

    public function GetMunicipalityICanEdit() {
        $modelData = $this->search();
        $list = array();
        foreach ($modelData->getData() as $municipality) {
            $list[] = $municipality;
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
        $criteria->compare('t.`name`', $this->name, true);
        $criteria->compare('t.`country_id`', $this->country_id);
        $criteria->with = array('country');
        $criteria->together = true;
        $criteria->compare('country.country', $this->country_search, true);

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

        $options =  array(
            'criteria' => $criteria,
            'sort' => array(
                'attributes' => array(
                    'country_search' => array(
                        'asc' => 'country.conutry',
                        'desc' => 'country.country DESC',
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