<?php

/**
 * This is the model class for table "country_administrator".
 *
 * The followings are the available columns in table 'country_administrator':
 * @property integer $id
 * @property integer $country_id
 * @property integer $user_id
 *
 * The followings are the available model relations:
 * @property User $user
 * @property Country $country
 */
class CountryAdministrator extends CActiveRecord {

    public $country_search;
    public $user_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CountryAdministrator the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'country_administrator';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('country_id, user_id', 'required'),
            array('country_id, user_id', 'numerical', 'integerOnly' => true),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, country_id, user_id, country_search, user_search', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'user' => array(self::BELONGS_TO, 'User', 'user_id'),
            'country' => array(self::BELONGS_TO, 'Country', 'country_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'country_id' => Yii::t('app', 'country_id'),
            'user_id' => Yii::t('app', 'Surname And Name'),
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

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('country_id', $this->country_id);
        $criteria->compare('user_id', $this->user_id);
        $criteria->together = true;
        $criteria->with = array('country', 'user', 'user.profile');
        $criteria->compare('`country`.`country`', $this->country_search, true);
        $criteria->compare('CONCAT_WS(\' \', `profile`.`last_name`, `profile`.`first_name`)', $this->user_search, true);

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
                    'user_search' => array(
                        'asc' => 'profile.last_name',
                        'desc' => 'profile.last_name DESC'
                    ),
                    '*',
                )
            ),
        );
        
        if($pagination = false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this, $options);
    }

}