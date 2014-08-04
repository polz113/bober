<?php

/**
 * This is the model class for table "competition_category_school_mentor".
 *
 * The followings are the available columns in table 'competition_category_school_mentor':
 * @property integer $id
 * @property integer $competition_category_school_id
 * @property integer $user_id
 * @property string $access_code
 * @property integer $disqualified
 * @property integer $disqualified_by
 * @property string $disqualified_reason
 *
 * The followings are the available model relations:
 * @property Users $disqualifiedBy
 * @property CompetitionCategorySchool $competitionCategorySchool
 * @property User $user
 * @property CompetitionUser[] $competitionUsers
 */
class CompetitionCategorySchoolMentor extends CActiveRecord {

    public $competition_school_search;
    public $user_search;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionCategorySchoolMentor the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_category_school_mentor';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('competition_category_school_id, user_id', 'required'),
            array('competition_category_school_id, user_id, disqualified, disqualified_by', 'numerical', 'integerOnly' => true),
            array('access_code', 'length', 'max' => 20),
            array('disqualified_reason', 'safe'),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, competition_category_school_id, user_id, access_code, competition_school_search, user_search, disqualified, disqualified_by, disqualified_reason', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'disqualifiedBy' => array(self::BELONGS_TO, 'Users', 'disqualified_by'),
            'competitionCategorySchool' => array(self::BELONGS_TO, 'CompetitionCategorySchool', 'competition_category_school_id'),
            'user' => array(self::BELONGS_TO, 'User', 'user_id'),
            'competitionUsers' => array(self::HAS_MANY, 'CompetitionUser', 'competition_category_school_mentor_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'competition_category_school_id' => Yii::t('app', 'Competition - Category - School'),
            'user_id' => Yii::t('app', 'Mentor'),
            'access_code' => Yii::t('app', 'Access code'),
            'disqualified' => Yii::t('app', 'Disqualified'),
            'disqualified_by' => Yii::t('app', 'Disqualified by'),
            'disqualified_reason' => Yii::t('app', 'Disqualified Reason'),
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
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;
        return $superuser == 1;
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;
        return $superuser == 1;
    }

    public function GetCompetitionCategorySchoolNameIdList() {
        $modelData = CompetitionCategorySchool::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competitionCatSch) {
            if ($competitionCatSch == null) {
                $competitionCatSch = new CompetitionCategorySchool();
            }
            // $competitionCatSch['id'] = $competitionCatSch->id;      
            $competitionCatSch['name'] = $competitionCatSch->competition->name . ' - ' . $competitionCatSch->competitionCategory->name . ' - ' . $competitionCatSch->school->name;

            $list[] = $competitionCatSch;
        }
        return $list;
    }

    public function GetCompetitionCategorySchoolMentorNameIdList() {
        $modelData = CompetitionCategorySchoolMentor::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competitionCatSch) {
            if ($competitionCatSch == null) {
                $competitionCatSch = new CompetitionCategorySchoolMentor();
            }
            $data = array(
                'id' => $competitionCatSch->id,
                'name' => $competitionCatSch->competitionCategorySchool->school->name . ' - ' . $competitionCatSch->competitionCategorySchool->competition->name . ' - ' . $competitionCatSch->competitionCategorySchool->competitionCategory->name . ' - ' . $competitionCatSch->user->profile->last_name . ' ' . $competitionCatSch->user->profile->first_name
            );
            $list[] = $data;
        }
        $this->orderBy($list, 'order by name asc', true, false);
        return $list;
    }

    public function orderBy(&$ary, $clause, $ascending = true, $numeric = true) {
        setlocale(LC_ALL, 'sl_SI.UTF-8');
        $clause = str_ireplace('order by', '', $clause);
        $clause = preg_replace('/\s+/', ' ', $clause);
        $keys = explode(',', $clause);
        $dirMap = array('desc' => 1, 'asc' => -1);
        $def = $ascending ? -1 : 1;

        $keyAry = array();
        $dirAry = array();
        foreach ($keys as $key) {
            $key = explode(' ', trim($key));
            $keyAry[] = trim($key[0]);
            if (isset($key[1])) {
                $dir = strtolower(trim($key[1]));
                $dirAry[] = $dirMap[$dir] ? $dirMap[$dir] : $def;
            } else {
                $dirAry[] = $def;
            }
        }

        $fnBody = '';
        for ($i = count($keyAry) - 1; $i >= 0; $i--) {
            $k = $keyAry[$i];
            $t = $dirAry[$i];
            $f = -1 * $t;
            $aStr = '$a[\'' . $k . '\']';
            $bStr = '$b[\'' . $k . '\']';
            if (strpos($k, '(') !== false) {
                $aStr = '$a->' . $k;
                $bStr = '$b->' . $k;
            }
            if ($numeric) {
                if ($fnBody == '') {
                    $fnBody .= "if({$aStr} == {$bStr}) { return 0; }\n";
                    $fnBody .= "return ({$aStr} < {$bStr}) ? {$t} : {$f};\n";
                } else {
                    $fnBody = "if({$aStr} == {$bStr}) {\n" . $fnBody;
                    $fnBody .= "}\n";
                    $fnBody .= "return ({$aStr} < {$bStr}) ? {$t} : {$f};\n";
                }
            } else {
                if ($fnBody == '') {
                    $fnBody .= "if({$aStr} == {$bStr}) { return 0; }\n";
                    $fnBody .= "return (strcoll({$aStr}, {$bStr}) < 0) ? {$t} : {$f};\n";
                } else {
                    $fnBody = "if({$aStr} == {$bStr}) {\n" . $fnBody;
                    $fnBody .= "}\n";
                    $fnBody .= "return (strcoll({$aStr}, {$bStr}) < 0) ? {$t} : {$f};\n";
                }
            }
        }

        if ($fnBody) {
            $sortFn = create_function('$a,$b', $fnBody);
            if (is_array($ary)) {
                usort($ary, $sortFn);
            }
        }
    }

    public function GetCompetitionCategorySchool() {
        return $this->competitionCategorySchool->competition->name . ' - ' . $this->competitionCategorySchool->competitionCategory->name . ' - ' . $this->competitionCategorySchool->school->name;
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false, $competition_id = 0, $competition_category_id = 0) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`competition_category_school_id`', $this->competition_category_school_id);
        $criteria->compare('t.`user_id`', $this->user_id);
        $criteria->compare('t.`access_code`', $this->access_code, true);
        $criteria->compare('t.`disqualified`', $this->disqualified);
        $criteria->compare('t.`disqualified_by`', $this->disqualified_by);
        $criteria->compare('t.`disqualified_reason`', $this->disqualified_reason, true);
        $criteria->together = true;
        $criteria->with = array('competitionCategorySchool', 'competitionCategorySchool.school.schoolMentors', 'user', 'user.profile', 'competitionCategorySchool.competition', 'competitionCategorySchool.school', 'competitionCategorySchool.competitionCategory');
        $criteria->compare('CONCAT_WS(\' \', `profile`.`last_name`, `profile`.`first_name`)', $this->user_search, true);
        $criteria->compare('CONCAT_WS(\' - \', `competition`.`name`, `competitionCategory`.`name`, `school`.`name`)', $this->competition_school_search, true);
        
        if ($competition_id != 0) {
            $criteria->compare('`competitionCategorySchool`.`competition_id`', $competition_id);
        }
        
        if ($competition_category_id != 0) {
            $criteria->compare('`competitionCategorySchool`.`competition_category_id`', $competition_category_id);
        }

        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            // ok
        } else {
            if ($user->profile->user_role >= 10) {
                $criteria->compare('`schoolMentors`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }else {
                // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
                $criteria->compare('`schoolMentors`.`user_id`', Yii::app()->user->id);
                $criteria->together = true;
            }
        }
        $criteria->group = 't.`id`';

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
        );
        if ($pagination == false) {
            $options['pagination'] = false;
        }

        return new CActiveDataProvider($this, $options);
    }

}
