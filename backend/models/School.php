<?php

/**
 * This is the model class for table "school".
 *
 * The followings are the available columns in table 'school':
 * @property integer $id
 * @property string $name
 * @property integer $school_category_id
 * @property integer $level_of_education
 * @property string $address
 * @property string $post
 * @property integer $postal_code
 * @property integer $municipality_id
 * @property integer $region_id
 * @property integer $country_id
 * @property string $tax_number
 * @property string $identifier
 * @property string $headmaster
 *
 * The followings are the available model relations:
 * @property SchoolCategory $schoolCategory
 * @property Municipality $municipality
 * @property Region $region
 * @property Country $country
 * @property SchoolMentor $schoolMentors
 */
class School extends CActiveRecord {

    public $country_search;
    public $school_category_search;
    public $region_search;
    public $uploadedData;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return School the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'school';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name, school_category_id', 'required'),
            array('school_category_id, level_of_education, postal_code, municipality_id, region_id, country_id', 'numerical', 'integerOnly' => true),
            array('name, address, post, headmaster', 'length', 'max' => 255),
            array('tax_number', 'length', 'max' => 12),
            array('identifier', 'length', 'max' => 20),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, name, school_category_id, level_of_education, address, post, postal_code, municipality_id, region_id, country_id, tax_number, identifier, country_search,school_category_search, region_search, headmaster, uploadedData', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competitionCategorySchools' => array(self::HAS_MANY, 'CompetitionCategorySchool', 'school_id'),
            'competitionUsers' => array(self::HAS_MANY, 'CompetitionUser', 'school_id'),
            'schoolCategory' => array(self::BELONGS_TO, 'SchoolCategory', 'school_category_id'),
            'municipality' => array(self::BELONGS_TO, 'Municipality', 'municipality_id'),
            'region' => array(self::BELONGS_TO, 'Region', 'region_id'),
            'country' => array(self::BELONGS_TO, 'Country', 'country_id'),
            'schoolMentors' => array(self::HAS_MANY, 'SchoolMentor', 'school_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'name' => Yii::t('app', 'name'),
            'school_category_id' => Yii::t('app', 'School Category'),
            'level_of_education' => Yii::t('app', 'level_of_education'),
            'address' => Yii::t('app', 'address'),
            'post' => Yii::t('app', 'Post'),
            'postal_code' => Yii::t('app', 'postal_code'),
            'municipality_id' => Yii::t('app', 'Municipality'),
            'region_id' => Yii::t('app', 'Region'),
            'country_id' => Yii::t('app', 'Country'),
            'tax_number' => Yii::t('app', 'tax_number'),
            'identifier' => Yii::t('app', 'Identifier'),
            'headmaster' => Yii::t('app', 'Headmaster'),
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
    
    public function GetLevelsOfEducation($empty = false){
        $options = array(
            1 => Yii::t('app','Primary School'),
            2 => Yii::t('app','Secondary School'),
        );
        if($empty){
            array_unshift($options,Yii::t('app','All Levels'));
        }
        return $options;
    }


    public function GetLevelsOfEducationName($id){
        $levels = $this->GetLevelsOfEducation();
        if(isset($levels[$id+1])){
            return $levels[$id+1];
        }
        return '';
    }

    

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false, $mentor_on_school_show_schools = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        if($this->level_of_education == 0){
            $this->level_of_education = NULL;
        }
        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`name`', $this->name, true);
        $criteria->compare('t.`school_category_id`', $this->school_category_id);
        if ($this->level_of_education != 0) {
            $this->level_of_education--;
            $criteria->compare('level_of_education', $this->level_of_education);
        }
        $criteria->compare('t.`address`', $this->address, true);
        $criteria->compare('t.`post`', $this->post, true);
        $criteria->compare('t.`postal_code`', $this->postal_code);
        $criteria->compare('t.`municipality_id`', $this->municipality_id);
        $criteria->compare('t.`region_id`', $this->region_id);
        $criteria->compare('t.`country_id`', $this->country_id);
        $criteria->compare('t.`tax_number`', $this->tax_number, true);
        $criteria->compare('t.`identifier`', $this->identifier, true);
        $criteria->compare('t.`headmaster`', $this->headmaster, true);
        $criteria->together = true;
        $criteria->with = array('country', 'schoolCategory', 'region');
        $criteria->compare('`country`.`country`', $this->country_search, true);
        $criteria->compare('`region`.`name`', $this->region_search, true);
        $criteria->compare('`schoolCategory`.`name`', $this->school_category_search, true);

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
            } else {
                if (!$mentor_on_school_show_schools) {
                    $criteria->with[] = 'schoolMentors';
                    $criteria->compare('`schoolMentors`.`user_id`', Yii::app()->user->id);
                    $criteria->compare('`schoolMentors`.`coordinator`', 1);
                    $criteria->together = true;
                } else {
                    $criteria->with[] = 'schoolMentors';
                    $criteria->compare('`schoolMentors`.`user_id`', Yii::app()->user->id);
                    $criteria->together = true;
                }
            }
        }
        
        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }
        
        $criteria->order = 't.`name` asc';
        
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
    
    public function import($content) {
        $header_cols = array(
            'name' => 0,
            'school_category_id' => 1,
            'level_of_education' => 2,
            'post' => 3,
            'postal_code' => 4,
            'municipality_id' => 5,
            'region_id' => 6,
            'country_id' => 7
        );
        header('Content-Type: text/html; charset=utf-8');
        $lines = explode("\n", $content);
        for ($i = 1; $i < count($lines); ++$i) {
            if (trim($lines[$i]) == '') {
                continue;
            }
            $cols = explode(";", $lines[$i]);
            // država
            $country_id = 0;
            $country = Country::model()->find('country=:country', array(':country' => trim($cols[$header_cols['country_id']])));
            if ($country == null) {
                echo Yii::t('app', 'Country does not exist! Country: ') . trim($cols[$header_cols['country_id']]);
                die();
            }
            $country_id = $country->id;
            // regija
            $region = Region::model()->find('name=:name and country_id=:country_id', array(':name' => trim($cols[$header_cols['region_id']]), ':country_id' => $country_id));
            if ($region == null) {
                $region = new Region();
                $region->country_id = $country_id;
                $region->name = trim($cols[$header_cols['region_id']]);
                $region->save();
            }
            $region_id = $region->id;
            // občina
            $municipality = Municipality::model()->find('name=:name and country_id=:country_id', array(':name' => trim($cols[$header_cols['municipality_id']]), ':country_id' => $country_id));
            if ($municipality == null) {
                $municipality = new Municipality();
                $municipality->country_id = $country_id;
                $municipality->name = trim($cols[$header_cols['municipality_id']]);
                $municipality->save();
            }
            $municipality_id = $municipality->id;
            
            $school_name = trim($cols[$header_cols['name']]);
            if ($school_name[0] == '"') {
                $school_name = mb_substr($school_name, 1, mb_strlen($school_name, 'UTF-8') - 2, 'UTF-8');
            }
            $school_name = str_replace('""', '"', $school_name);
            $school = School::model()->find('name=:name and country_id=:country_id', array(':name' => $school_name, ':country_id' => $country_id));
            if ($school == null) {
                $school = new School();
                $school->name = $school_name;
                $school->country_id = $country_id;
                $school->municipality_id = $municipality_id;
                $school->region_id = $region_id;
                $school->post = trim($cols[$header_cols['post']]);
                $school->postal_code = trim($cols[$header_cols['postal_code']]);
                $school->school_category_id = (int)trim($cols[$header_cols['school_category_id']]);
                $school->level_of_education = (int)trim($cols[$header_cols['level_of_education']]);
                $school->save();
                echo 'Imported: ', $school_name, "<br />\n";
                if (count($school->errors) > 0) {
                    print_r($school->errors);
                    die();
                }
            } else{
                echo 'Already imported: ', $school_name, "<br />\n";
            }
        }
    }

}