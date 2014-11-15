<?php

/**
 * This is the model class for table "competition_user".
 *
 * The followings are the available columns in table 'competition_user':
 * @property integer $id
 * @property integer $competition_id
 * @property integer $competition_category_id
 * @property integer $user_id
 * @property integer $competition_category_school_mentor_id
 * @property string $last_name
 * @property string $first_name
 * @property integer $gender
 * @property string $class
 * @property integer $school_id
 * @property integer $disqualified_request
 * @property integer $disqualified_request_by
 * @property integer $disqualified
 * @property integer $disqualified_by
 * @property string $disqualified_reason
 * @property integer $advancing_to_next_level
 * @property integer $award
 * @property string $ip_start
 * @property string $ip_stop
 * @property string $start_time
 * @property string $finish_time
 * @property integer $finished
 * @property integer $questions_prepared
 * @property string $total_points_via_answers
 * @property string $total_points_via_time
 * @property string $total_points_manual
 * @property string $total_points
 *
 * The followings are the available model relations:
 * @property Award[] $awards
 * @property Competition $competition
 * @property CompetitionCategory $competitionCategory
 * @property Users $user
 * @property CompetitionCategorySchoolMentor $competitionCategorySchoolMentor
 * @property School $school
 * @property Users $disqualifiedRequestBy
 * @property Users $disqualifiedBy
 * @property CompetitionUserQuestion[] $competitionUserQuestions
 */
class CompetitionUser extends CActiveRecord {

    public $access_code;
    public $competition_results;
    public $competition_name;
    public $competition_category_name;
    public $mentor_name;
    // these fields are used for checkdata
    public $timestamp_start;
    public $timestamp_stop;
    public $uploadedData;
    public $number_of_awards;
    public $school_name;
    public $number_of_points_needed_for_advancing_to_next_level;
    public $class_numberic;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionUser the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'competition_user';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('competition_id, competition_category_id, school_id', 'required'),
            array('competition_id, competition_category_id, user_id, competition_category_school_mentor_id, school_id, disqualified_request, disqualified_request_by, disqualified, disqualified_by, advancing_to_next_level, award, finished, questions_prepared, number_of_points_needed_for_advancing_to_next_level, class_numberic', 'numerical', 'integerOnly' => true),
            array('last_name, first_name, access_code', 'length', 'max' => 255),
            array('class', 'length', 'max' => 20),
            array('total_points_via_answers, total_points_via_time, total_points_manual, total_points, gender', 'length', 'max' => 10),
            array('disqualified_reason, start_time, finish_time', 'safe'),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, competition_id, number_of_points_needed_for_advancing_to_next_level, mentor_name, school_name, competition_name, competition_category_name, competition_category_id, user_id, competition_category_school_mentor_id, last_name, first_name, gender, class, school_id, disqualified_request, disqualified_request_by, disqualified, disqualified_by, disqualified_reason, advancing_to_next_level, award, start_time, finish_time, finished, questions_prepared, total_points_via_answers, total_points_via_time, total_points_manual, total_points, uploadedData, class_numberic, ip_start, ip_stop', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'awards' => array(self::HAS_MANY, 'Award', 'competition_user_id'),
            'competition' => array(self::BELONGS_TO, 'Competition', 'competition_id'),
            'competitionCategory' => array(self::BELONGS_TO, 'CompetitionCategory', 'competition_category_id'),
            'user' => array(self::BELONGS_TO, 'User', 'user_id'),
            'competitionCategorySchoolMentor' => array(self::BELONGS_TO, 'CompetitionCategorySchoolMentor', 'competition_category_school_mentor_id'),
            'school' => array(self::BELONGS_TO, 'School', 'school_id'),
            'disqualifiedRequestBy' => array(self::BELONGS_TO, 'User', 'disqualified_request_by'),
            'disqualifiedBy' => array(self::BELONGS_TO, 'User', 'disqualified_by'),
            'competitionUserQuestions' => array(self::HAS_MANY, 'CompetitionUserQuestion', 'competition_user_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'Competitor ID'),
            'competition_id' => Yii::t('app', 'Competition'),
            'competition_category_id' => Yii::t('app', 'Competition Category'),
            'user_id' => Yii::t('app', 'User'),
            'competition_category_school_mentor_id' => Yii::t('app', 'Mentor'),
            'last_name' => Yii::t('app', 'Last Name'),
            'first_name' => Yii::t('app', 'First Name'),
            'gender' => Yii::t('app', 'Gender'),
            'class' => Yii::t('app', 'Class'),
            'school_id' => Yii::t('app', 'School'),
            'disqualified_request' => Yii::t('app', 'Disqualified Request'),
            'disqualified_request_by' => Yii::t('app', 'Disqualified Request By'),
            'disqualified' => Yii::t('app', 'Disqualified'),
            'disqualified_by' => Yii::t('app', 'Disqualified By'),
            'disqualified_reason' => Yii::t('app', 'Disqualified Reason'),
            'advancing_to_next_level' => Yii::t('app', 'Advancing to next level'),
            'award' => Yii::t('app', 'Award'),
            'start_time' => Yii::t('app', 'Competition Start Time'),
            'finish_time' => Yii::t('app', 'Competition Finished Time'),
            'finished' => Yii::t('app', 'Competition Finished'),
            'questions_prepared' => Yii::t('app', 'questions_prepared'),
            'total_points_via_answers' => Yii::t('app', 'total_points_via_answers'),
            'total_points_via_time' => Yii::t('app', 'total_points_via_time'),
            'total_points_manual' => Yii::t('app', 'total_points_manual'),
            'total_points' => Yii::t('app', 'total_points'),
            'access_code' => Yii::t('app', 'Access code'),
            'timestamp_start' => Yii::t('app', 'From'),
            'timestamp_stop' => Yii::t('app', 'To'),
            'competition_results' => Yii::t('app', 'Competition Results'),
            'number_of_points_needed_for_advancing_to_next_level' => Yii::t('app', 'Number of points needed for advancing to next level of competition'),
            'ip_start' => Yii::t('app', 'IP start'),
            'ip_stop' => Yii::t('app', 'IP stop')
        );
    }

    public function checkAccessCode() {
        return CompetitionCategorySchoolMentor::model()->find('access_code=:access_code and disqualified=:disqualified', array(':access_code' => $this->access_code, ':disqualified' => 0));
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $superuser = Generic::isSuperAdmin();
        if ($superuser) {
            return true;
        }

        if ($this->competitionCategorySchoolMentor->user_id == Yii::app()->user->id) {
            return true;
        }
        $mentors = isset($this->competitionCategorySchoolMentor->competitionCategorySchool->school->schoolMentors) ? $this->competitionCategorySchoolMentor->competitionCategorySchool->school->schoolMentors : null;
        if ($mentors != null) {
            foreach ($mentors as $mentor) {
                if ($mentor->coordinator == 1 && $mentor->user_id == Yii::app()->user->id) {
                    return true;
                }
            }
        }
        if (isset(Yii::app()->session['competition_user_id']) && Yii::app()->session['competition_user_id'] == $this->id) {
            return true;
        }
        return false;
    }

    public function getCanUpdate() {
        return $this->CanUpdate();
    }

    public function CanUpdate() {
        $superuser = Generic::isSuperAdmin();
        if ($superuser) {
            return true;
        }

        if ($this->competitionCategorySchoolMentor->user_id == Yii::app()->user->id) {
            return true;
        }
        $mentors = isset($this->competitionCategorySchoolMentor->competitionCategorySchool->school->schoolMentors) ? $this->competitionCategorySchoolMentor->competitionCategorySchool->school->schoolMentors : null;
        if ($mentors != null) {
            foreach ($mentors as $mentor) {
                if ($mentor->coordinator == 1 && $mentor->user_id == Yii::app()->user->id) {
                    return true;
                }
            }
        }
        return false;
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        $superuser = Generic::isSuperAdmin();
        if ($superuser) {
            return true;
        }
    }

    public function GetGender($empty = false) {
        $options = array(
            0 => Yii::t('app', 'Male'),
            1 => Yii::t('app', 'Female'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All genders'));
        }
        return $options;
    }

    public function GetGenderName($id) {
        $genders = $this->GetGender();
        if (isset($genders[$id])) {
            return $genders[$id];
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
        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }
        $superuser = Generic::isSuperAdmin();

        $criteria = new CDbCriteria;

        $criteria->compare('t.`id`', $this->id);
        $criteria->compare('t.`competition_id`', $this->competition_id);
        $criteria->compare('t.`competition_category_id`', $this->competition_category_id);
        $criteria->compare('t.`user_id`', $this->user_id);
        $criteria->compare('t.`competition_category_school_mentor_id`', $this->competition_category_school_mentor_id);
        $criteria->compare('t.`last_name`', $this->last_name, true);
        $criteria->compare('t.`first_name`', $this->first_name, true);
        if ($this->gender == 0) {
            // skip
        } else {
            $criteria->compare('t.`gender`', $this->gender - 1);
        }
        $criteria->compare('t.`class`', $this->class, true);
        $criteria->compare('t.`school_id`', $this->school_id);
        if ($this->disqualified_request == 0) {
            // skip
        } else {
            $criteria->compare('t.`disqualified_request`', $this->disqualified_request - 1);
        }
        $criteria->compare('t.`disqualified_request_by`', $this->disqualified_request_by);
        if ($this->disqualified == 0) {
            // skip
        } else {
            $criteria->compare('t.`disqualified`', $this->disqualified - 1);
        }
        $criteria->compare('t.`disqualified_by`', $this->disqualified_by);
        $criteria->compare('t.`disqualified_reason`', $this->disqualified_reason, true);

        $criteria->compare('t.`start_time`', $this->start_time, true);
        $criteria->compare('t.`finish_time`', $this->finish_time, true);
        $criteria->compare('t.`finished`', $this->finished);
        $criteria->compare('t.`total_points_via_answers`', $this->total_points_via_answers, true);
        $criteria->compare('t.`total_points_via_time`', $this->total_points_via_time, true);
        $criteria->compare('t.`total_points_manual`', $this->total_points_manual, true);
        $criteria->compare('t.`total_points`', $this->total_points, true);

        $competition_ids = array();
        $filter_competition = False;
        $cc = new CDbCriteria();
        $cc->select = 'id';
        if ($this->competition_name != '') {
            $cc->compare('name', $this->competition_name);
            $filter_competition = True;
        }
        if (! $superuser) {
            $cc->addCondition('public_access=1');
            $filter_competition = True;
        }
        if ($filter_competition) {
            $competitions = Competition::model()->findAll($cc);
            foreach ($competitions as $el) {
                $competition_ids[] = $el->id;
            }
            $criteria->with[] = 'competition';
            $criteria->together = true;
            // error_log("PUBLIC_OK:" . implode(", ", $competition_ids));
            $criteria->addInCondition('t.`competition_id`', $competition_ids);
        }

        // award search should work only for admins / mentors who has set search parameter competition_name and they have access to this results
        if ($superuser || (count($competition_ids) == 1 && self::canShowAwardField($competition_ids[0]))) {
            if ($this->award != 0) {
                switch ($this->award) {
                    case 2:
                        $this->award = 5;
                        break;
                    case 3:
                        $this->award = 10;
                        break;
                    case 4:
                        $this->award = 15;
                        break;
                    default:
                        break;
                }
                $criteria->compare('t.`award`', $this->award);
            }
        }

        if ($superuser || (count($competition_ids) == 1 && self::canShowAdvancingToNextLevel($competition_ids[0]))) {
            if ($this->advancing_to_next_level != 0) {
                $criteria->compare('t.`advancing_to_next_level`', $this->advancing_to_next_level - 1);
            }
        }
        $competition_category_ids = array();

        if ($this->competition_category_name != '') {
            $criteria->with[] = 'competitionCategory';
            $criteria->together = true;
            $cc = new CDbCriteria();
            $cc->select = 'id';
            $cc->compare('name', $this->competition_category_name);
            $competitionCategories = CompetitionCategory::model()->findAll($cc);
            foreach ($competitionCategories as $el) {
                $competition_category_ids[] = $el->id;
            }
            if (count($competition_category_ids) > 0) {
                $criteria->addInCondition('t.`competition_category_id`', $competition_category_ids);
            }
        }

        $mentor_user_ids = array();

        if ($this->mentor_name != '') {
            $criteria->with[] = 'competitionCategorySchoolMentor.user.profile';
            $criteria->together = true;
            $pcr = new CDbCriteria();
            $pcr->select = 'user_id';
            $pcr->compare('CONCAT_WS(\' \', `last_name`, `first_name`)', $this->mentor_name, true);
            $profiles = Profile::model()->findAll($pcr);
            foreach ($profiles as $el) {
                $mentor_user_ids[] = $el->user_id;
            }
        }

        // seznam kje je uporabnik kooridinator
        $school_ids = array();
        $competition_category_school_ids = array();
        if (!$superuser) {
            $cs = new CDbCriteria();
            $cs->select = 'school_id';
            $cs->condition = 'user_id=:user_id and coordinator=:coordinator';
            $cs->params = array(':user_id' => Yii::app()->user->id, ':coordinator' => 1);
            $coordinatorOnSchools = SchoolMentor::model()->findAll($cs);
            foreach ($coordinatorOnSchools as $el) {
                $school_ids[] = $el->school_id;
            }

            if (count($school_ids) > 0) {
                $cs = new CDbCriteria();
                $cs->select = 'id';
                $cs->addInCondition('school_id', $school_ids);
                if (count($competition_category_ids) > 0) {
                    $cs->addInCondition('competition_category_id', $competition_category_ids);
                }
                if (count($competition_ids) > 0) {
                    $cs->addInCondition('competition_id', $competition_ids);
                }
                $ccs = CompetitionCategorySchool::model()->findAll($cs);
                foreach ($ccs as $el) {
                    $competition_category_school_ids[] = $el->id;
                }
            }
        }

        // competition_category_school_mentor_ids
        $competition_category_school_mentor_ids = array();
        $cr_condition_set = false;
        $cr = new CDbCriteria();
        $cr->select = 'id';
        if ($this->mentor_name != '' && count($mentor_user_ids) > 0) {
            $cr->addInCondition('user_id', $mentor_user_ids);
            $cr_condition_set = true;
        }
        if (!$superuser) {
            $cr->compare('user_id', Yii::app()->user->id);
            $cr_condition_set = true;

            if (count($competition_category_school_ids) > 0) {
                $cr2 = new CDbCriteria();
                $cr2->select = 'id';
                $cr2->addInCondition('competition_category_school_id', $competition_category_school_ids);
                if ($this->mentor_name != '' && count($mentor_user_ids) > 0) {
                    $cr2->addInCondition('user_id', $mentor_user_ids);
                }
                $cr->mergeWith($cr2, 'OR');
            }
        }

        if ($cr_condition_set) {
            $csm = CompetitionCategorySchoolMentor::model()->findAll($cr);
            foreach ($csm as $el) {
                $competition_category_school_mentor_ids[] = $el->id;
            }
        }

        if (count($competition_category_school_mentor_ids) > 0) {
            $criteria->addInCondition('t.`competition_category_school_mentor_id`', $competition_category_school_mentor_ids);
        }

        $criteria->group = 't.`id`';
        $options = array(
            'criteria' => $criteria,
        );

        if ($pagination == false) {
            $options['pagination'] = false;
        }

        return new CActiveDataProvider($this, $options);
    }

    public function searchAwardsByMentor() {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.
        $pagination = true;

        $criteria = new CDbCriteria;

        $criteria->compare('t.`competition_id`', $this->competition_id);
        $criteria->compare('t.`competition_category_id`', $this->competition_category_id);
        $criteria->compare('t.`school_id`', $this->school_id);
        $criteria->compare('t.`disqualified`', 0);

        $superuser = Generic::isSuperAdmin();

        $competition_ids = array();

        if ($this->competition_name != '') {
            $cc = new CDbCriteria();
            $cc->select = 'id';
            $cc->compare('name', $this->competition_name, true);
            $competitions = Competition::model()->findAll($cc);
            foreach ($competitions as $el) {
                $competition_ids[] = $el->id;
            }
            $criteria->with[] = 'competition';
            $criteria->together = true;
            if (count($competition_ids) > 0) {
                $criteria->addInCondition('t.`competition_id`', $competition_ids);
            }
        }

        $competition_category_ids = array();

        if ($this->competition_category_name != '') {
            $criteria->with[] = 'competitionCategory';
            $criteria->together = true;
            $cc = new CDbCriteria();
            $cc->select = 'id';
            $cc->compare('name', $this->competition_category_name, true);
            $competitionCategories = CompetitionCategory::model()->findAll($cc);
            foreach ($competitionCategories as $el) {
                $competition_category_ids[] = $el->id;
            }
            if (count($competition_category_ids) > 0) {
                $criteria->addInCondition('t.`competition_category_id`', $competition_category_ids);
            }
        }

        $mentor_user_ids = array();

        if ($this->mentor_name != '') {
            $criteria->with[] = 'competitionCategorySchoolMentor.user.profile';
            $criteria->together = true;
            $pcr = new CDbCriteria();
            $pcr->select = 'user_id';
            $pcr->compare('CONCAT_WS(\' \', `last_name`, `first_name`)', $this->mentor_name, true);
            $profiles = Profile::model()->findAll($pcr);
            foreach ($profiles as $el) {
                $mentor_user_ids[] = $el->user_id;
            }
        }

        // seznam kje je uporabnik kooridinator
        $school_ids = array();
        $competition_category_school_ids = array();
        if (!$superuser) {
            $cs = new CDbCriteria();
            $cs->select = 'school_id';
            $cs->condition = 'user_id=:user_id and coordinator=:coordinator';
            $cs->params = array(':user_id' => Yii::app()->user->id, ':coordinator' => 1);
            $coordinatorOnSchools = SchoolMentor::model()->findAll($cs);
            foreach ($coordinatorOnSchools as $el) {
                $school_ids[] = $el->school_id;
            }

            if (count($school_ids) > 0) {
                $cs = new CDbCriteria();
                $cs->select = 'id';
                $cs->addInCondition('school_id', $school_ids);
                if (count($competition_category_ids) > 0) {
                    $cs->addInCondition('competition_category_id', $competition_category_ids);
                }
                if (count($competition_ids) > 0) {
                    $cs->addInCondition('competition_id', $competition_ids);
                }
                $ccs = CompetitionCategorySchool::model()->findAll($cs);
                foreach ($ccs as $el) {
                    $competition_category_school_ids[] = $el->id;
                }
            }
        }

        // competition_category_school_mentor_ids
        $competition_category_school_mentor_ids = array();
        $cr_condition_set = false;
        $cr = new CDbCriteria();
        $cr->select = 'id';
        if ($this->mentor_name != '' && count($mentor_user_ids) > 0) {
            $cr->addInCondition('user_id', $mentor_user_ids);
            $cr_condition_set = true;
        }
        if (!$superuser) {
            $cr->compare('user_id', Yii::app()->user->id);
            $cr_condition_set = true;

            if (count($competition_category_school_ids) > 0) {
                $cr2 = new CDbCriteria();
                $cr2->select = 'id';
                $cr2->addInCondition('competition_category_school_id', $competition_category_school_ids);
                if ($this->mentor_name != '' && count($mentor_user_ids) > 0) {
                    $cr2->addInCondition('user_id', $mentor_user_ids);
                }
                $cr->mergeWith($cr2, 'OR');
            }
        }

        if ($cr_condition_set) {
            $csm = CompetitionCategorySchoolMentor::model()->findAll($cr);
            foreach ($csm as $el) {
                $competition_category_school_mentor_ids[] = $el->id;
            }
        }

        if (count($competition_category_school_mentor_ids) > 0) {
            $criteria->addInCondition('t.`competition_category_school_mentor_id`', $competition_category_school_mentor_ids);
        }

        if ($this->school_name != '') {
            $scriteria = new CDbCriteria();
            $scriteria->select = 'id';
            $scriteria->compare('t.`name`', $this->school_name, true);
            $schools = School::model()->findAll($scriteria);
            $school_ids = array();
            foreach ($schools as $sc) {
                $school_ids[] = $sc->id;
            }
            $criteria->addInCondition('t.`school_id`', $school_ids);
        }

        $criteria->with[] = 'competitionCategorySchoolMentor';

        $criteria->group = 't.`competition_id`, t.`competition_category_id`, t.`school_id`, `competitionCategorySchoolMentor`.user_id';

        return new CActiveDataProvider($this, array(
            'criteria' => $criteria,
        ));
    }

    public function getNumberOfAwards() {
        return $this->getNumberOfBronzeAwards() . '/' . $this->getNumberOfCompetitiors();
    }

    public function getNumberOfCompetitiors() {
        return CompetitionUser::model()->with('competitionCategorySchoolMentor')->count('t.`competition_id`=:competition_id and t.`competition_category_id`=:competition_category_id and t.`disqualified`=:disqualified and t.`school_id`=:school_id and competitionCategorySchoolMentor.user_id=:user_id', array(':competition_id' => $this->competition_id, ':competition_category_id' => $this->competition_category_id, ':disqualified' => 0, ':school_id' => $this->school_id, ':user_id' => $this->competitionCategorySchoolMentor->user_id));
    }

    public function getNumberOfBronzeAwards() {
        return CompetitionUser::model()->with('competitionCategorySchoolMentor')->count('t.`competition_id`=:competition_id and t.`competition_category_id`=:competition_category_id and t.`disqualified`=:disqualified and t.`school_id`=:school_id and competitionCategorySchoolMentor.user_id=:user_id and t.`award`=:award', array(':competition_id' => $this->competition_id, ':competition_category_id' => $this->competition_category_id, ':disqualified' => 0, ':school_id' => $this->school_id, ':user_id' => $this->competitionCategorySchoolMentor->user_id, ':award' => 5));
    }

    public function getSchoolName() {
        return $this->school->name;
    }

    public function checkData($data) {
        $timestamp_start = date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($data['timestamp_start'], 'medium', 'short')));
        $timestamp_stop = date('Y-m-d H:i:s', strtotime(Yii::app()->localtime->fromLocalDateTime($data['timestamp_stop'], 'medium', 'short')));
        $criteria = new CDbCriteria();
        // $criteria->select = '`users`.`username`, `profile`.`last_name`, `profile`.`first_name`';
        $criteria->with[] = 'competitionCategorySchoolMentor.user';
        $criteria->with[] = 'competitionCategorySchoolMentor.user.profile';
        $criteria->with[] = 'competitionCategorySchoolMentor.competitionCategorySchool';
        $criteria->with[] = 'competitionCategorySchoolMentor.competitionCategorySchool.competitionCategory';
        $criteria->condition = '`competitionCategorySchool`.`competition_id` = ' . $data['competition_id'] . ' and `competitionCategorySchool`.`competition_category_id` = ' . $data['competition_category_id'] . ' and (t.`start_time` BETWEEN \'' . $timestamp_start . '\' and \'' . $timestamp_stop . '\') and (CONVERT(SUBSTRING(t.`class`, 1, 1), SIGNED INTEGER) NOT BETWEEN competitionCategory.class_from AND competitionCategory.class_to)';
        $criteria->group = '`user`.`username`';

        return new CActiveDataProvider($this, array(
            'criteria' => $criteria,
            'pagination' => false
        ));
    }

    public static function canShowCompetitionResults($competition_id) {
        $superuser = Generic::isSuperAdmin();
        if (!$superuser) {
            // check if visible by competition settings
            $cache_key = 'CCompetition-mentor-results-timestamp-' . $competition_id;
            $cache = Yii::app()->cache->get($cache_key);
            if ($cache == null) {
                $competition = Competition::model()->findByPk($competition_id);
                if ($competition != null) {
                    $cache = $competition->timestamp_mentor_results == null ? '-' : $competition->timestamp_mentor_results;
                } else {
                    $cache = '-';
                }
                Yii::app()->cache->set($cache_key, $cache, 600);
            }
            if ($cache == '-') {
                return false;
            } else {
                $timestamp = strtotime($cache);
                if ($timestamp > time()) {
                    return false;
                }
            }
        }
        return true;
    }

    public function getCompetitionResults() {
        if (!self::canShowCompetitionResults($this->competition_id)) {
            return Yii::t('app', 'Competition results are not available yet.');
        }
        $points = 0;
        $wrong = array();
        $not = array();
        $startpoints = 0;
        $maxpoints = 0;
        foreach ($this->competitionUserQuestions as $competitionUserQuestion) {
            $cache_key = "CQAnswer-" . $competitionUserQuestion->competition_question_id . '-' . $this->competition_category_id;
            $cache = Yii::app()->cache->get($cache_key);
            if ($cache == null) {
                $right_answer = unserialize($competitionUserQuestion->competitionQuestion->question->verification_function);
                $correct_points = 1;
                $wrong_points = 0;
                $competitonQuestionDifficulty = CompetitionQuestionDifficulty::model()->with("competitionQuestionCategories")->find("competitionQuestionCategories.competition_question_id=:competition_question_id and competitionQuestionCategories.competition_category_id=:competition_category_id", array(":competition_question_id" => $competitionUserQuestion->competition_question_id, ":competition_category_id" => $this->competition_category_id));
                if ($competitonQuestionDifficulty != null) {
                    $correct_points = $competitonQuestionDifficulty->correct_answer_points;
                    $wrong_points = $competitonQuestionDifficulty->wrong_answer_points;
                }
                $cache = array(
                    'right_answer' => $right_answer,
                    'correct_points' => $correct_points,
                    'wrong_points' => $wrong_points
                );
                Yii::app()->cache->set($cache_key, serialize($cache), 60);
            } else {
                $cache = unserialize($cache);
            }
            $startpoints += abs($cache['wrong_points']);
            $maxpoints += $cache['correct_points'];
            if ($competitionUserQuestion->custom_answer != '' && $competitionUserQuestion->custom_answer != null) {
                if (in_array($competitionUserQuestion->custom_answer, $cache['right_answer'])) {
                    $points += $cache['correct_points'];
                } else {
                    $points += $cache['wrong_points'];
                    $wrong[] = CompetitionQuestion::getQuestionTitle($competitionUserQuestion->competition_question_id);
                }
            } else {
                $not[] = CompetitionQuestion::getQuestionTitle($competitionUserQuestion->competition_question_id);
            }
        }
        sort($wrong);
        sort($not);
        return ($startpoints + $points) . '/' . ($startpoints + $maxpoints) . (count($wrong) > 0 ? ' | napačni: ' . implode(', ', $wrong) : '') . (count($not) > 0 ? ' | neodgov.: ' . implode(',', $not) : '');
    }

    public function getCompetitionNumericResult($visible = false) {
        if (!$visible) {
            return '';
        }
        $points = 0;
        $wrong = array();
        $not = array();
        $startpoints = 0;
        $totalpoints = 0;
        foreach ($this->competitionUserQuestions as $competitionUserQuestion) {
            $cache_key = "CQAnswer-" . $competitionUserQuestion->competition_question_id . '-' . $this->competition_category_id;
            $cache = Yii::app()->cache->get($cache_key);
            if ($cache == null) {
                $right_answer = unserialize($competitionUserQuestion->competitionQuestion->question->verification_function);
                $correct_points = 1;
                $wrong_points = 0;
                $competitonQuestionDifficulty = CompetitionQuestionDifficulty::model()->with("competitionQuestionCategories")->find("competitionQuestionCategories.competition_question_id=:competition_question_id and competitionQuestionCategories.competition_category_id=:competition_category_id", array(":competition_question_id" => $competitionUserQuestion->competition_question_id, ":competition_category_id" => $this->competition_category_id));
                if ($competitonQuestionDifficulty != null) {
                    $correct_points = $competitonQuestionDifficulty->correct_answer_points;
                    $wrong_points = $competitonQuestionDifficulty->wrong_answer_points;
                }
                $cache = array(
                    'right_answer' => $right_answer,
                    'correct_points' => $correct_points,
                    'wrong_points' => $wrong_points
                );
                Yii::app()->cache->set($cache_key, serialize($cache), 60);
            } else {
                $cache = unserialize($cache);
            }
            $startpoints += abs($cache['wrong_points']);
            $totalpoints += abs($cache['correct_points']);
            if ($competitionUserQuestion->custom_answer != '' && $competitionUserQuestion->custom_answer != null) {
                if (in_array($competitionUserQuestion->custom_answer, $cache['right_answer'])) {
                    $points += $cache['correct_points'];
                } else {
                    $points += $cache['wrong_points'];
                }
            }
        }
        return array(
            'result' => $startpoints + $points,
            'startpoints' => $startpoints,
            'totalpoints' => $totalpoints + $startpoints
        );
    }

    public function getCompetitionName() {
        return $this->competition->name;
    }

    public function getMentorName() {
        if (isset($this->competition_category_school_mentor_id) && $this->competition_category_school_mentor_id != null) {
            $cache_key = 'competitionCategorySchoolMentorName#' . $this->competition_category_school_mentor_id;
            $cached = Yii::app()->cache->get($cache_key);
            if ($cached == null) {
                $cached = $this->competitionCategorySchoolMentor->user->profile->last_name . ' ' . $this->competitionCategorySchoolMentor->user->profile->first_name;
                Yii::app()->cache->set($cache_key, $cached, 600);
            }
            return $cached;
        }
        return Yii::t('app', 'ERROR! Missing mentor!');
    }

    public function getCompetitionCategoryName() {
        return $this->competitionCategory->name;
    }

    public function exportData($competition_id, $competition_category_id = 0) {
        // export headers (ID tekmovalca, ime, priimek, spol, šola, mentor, razred, kategorija, vprašanja... (v oklepaju pravilen odgovor), Število točk, Priznanje
        $list = array();
        $superuser = Generic::isSuperAdmin();
        if ($superuser) {
            $conditions = array(':competition_id' => $competition_id);
            if ($competition_category_id != 0) {
                $conditions[':competition_category_id'] = $competition_category_id;
            }
            $data = CompetitionUser::model()->with('school')->with('competitionCategorySchoolMentor.user.profile')->with('competitionCategory')->with('competitionUserQuestions.competitionQuestion.competitionQuestionCategories')->with('competitionUserQuestions')->findAll(
                    array(
                        'condition' => 't.competition_id=:competition_id ' . ($competition_category_id != 0 ? 'and t.competition_category_id=:competition_category_id' : '') . ' and t.competition_category_id=competitionQuestionCategories.competition_category_id',
                        'params' => $conditions,
                        'order' => 'school.name ASC, profile.last_name ASC, profile.first_name ASC, competitionCategory.name ASC, t.class ASC, t.last_name ASC, t.first_name ASC',
            ));
        } else {
            $cUser = CompetitionUser::model();
            $cUser->competition_id = $competition_id;
            $cUser->competition_category_id = $competition_category_id;
            $dataProvider = $cUser->search(true);
            $data = array();
            foreach ($dataProvider->getData() as $el) {
                $data[] = $el;
            }
        }
        $competition = Competition::model()->findByPk($competition_id);
        $duration = $competition->duration;
        $row_data = array();
        $questions = array();
        $cached_school_mentor_ids = array();
        $cached_school_mentor_emails = array();
        foreach ($data as $el) {
            $row = array();
            $row['id'] = $el->id;
            $row['first_name'] = $el->first_name;
            $row['last_name'] = $el->last_name;
            $row['gender'] = $el->gender == 0 ? 'M' : 'Ž';
            $row['class'] = $el->class;
            $row['competition'] = $el->competition->name;
            $row['school'] = $el->school->name;
            if (self::canShowAwardField($el->competition_id)) {
                $row['award'] = $el->GetAwardName($el->award);
            }
            if (self::canShowAdvancingToNextLevel($competition_id)) {
                $row['advancing_to_next_level'] = $el->advancing_to_next_level;
            }
            // čas tekmovanja
            if ($el->finish_time == null || $el->start_time == null) {
                $row['duration'] = $duration;
            } else {
                $row['duration'] = number_format(round((strtotime($el->finish_time) - strtotime($el->start_time)) / 60 * 100) / 100, 2, ",", ".");
            }
            if ($superuser) {
                $row['user_id'] = isset($el->competitionCategorySchoolMentor) ? $el->competitionCategorySchoolMentor->user_id : '/';
                if ($row['user_id'] != '/') {
                    if (!isset($cached_school_mentor_emails[$row['user_id']])) {
                        $mentorUser = User::model()->findByPk($row['user_id']);
                        if ($mentorUser != null) {
                            $cached_school_mentor_emails[$row['user_id']] = $mentorUser->email;
                            $row['mentor_email'] = $mentorUser->email;
                        } else {
                            $row['mentor_email'] = '/';
                        }
                    } else {
                        $row['mentor_email'] = $cached_school_mentor_emails[$row['user_id']];
                    }
                    $mentor_key = $row['user_id'] . '#' . $el->school_id;
                    if (isset($cached_school_mentor_ids[$mentor_key])) {
                        $row['mentor_id'] = $cached_school_mentor_ids[$mentor_key];
                    } else {
                        $mentor_get = SchoolMentor::model()->find('user_id=:user_id and school_id=:school_id', array(':user_id' => $row['user_id'], ':school_id' => $el->school_id));
                        if ($mentor_get != null) {
                            $cached_school_mentor_ids[$mentor_key] = 'M'.$mentor_get->id;
                        } else {
                            $cached_school_mentor_ids[$mentor_key] = '/';
                        }
                        $row['mentor_id'] = $cached_school_mentor_ids[$mentor_key];
                    }
                } else {
                    $row['mentor_id'] = '/';
                }
                $row['ip_start'] = $el->ip_start;
                $row['ip_stop'] = $el->ip_stop;
            }
            if (isset($el->competitionCategorySchoolMentor) && isset($el->competitionCategorySchoolMentor->user) && isset($el->competitionCategorySchoolMentor->user->profile)) {
                $row['mentor'] = $el->competitionCategorySchoolMentor->user->profile->last_name . ' ' . $el->competitionCategorySchoolMentor->user->profile->first_name;
            } else {
                $row['mentor'] = '/';
            }
            $row['category'] = $el->competitionCategory->name;
            $row['disqualified'] = $el->disqualified;
            $row['questions'] = array();
            if (self::canShowCompetitionResults($el->competition_id)) {
                foreach ($el->competitionUserQuestions as $competitionUserQuestion) {
                    $row['questions'][$competitionUserQuestion->competition_question_id] = $competitionUserQuestion->custom_answer;
                    if (!isset($questions[$competitionUserQuestion->competition_question_id])) {
                        $questionDifficulty = CompetitionQuestionDifficulty::model()->with("competitionQuestionCategories")->find("competitionQuestionCategories.competition_question_id=:competition_question_id and competitionQuestionCategories.competition_category_id=:competition_category_id", array(":competition_question_id" => $competitionUserQuestion->competition_question_id, ":competition_category_id" => $el->competition_category_id));
                        $question = $competitionUserQuestion->competitionQuestion->question;
                        $ver_func = unserialize($question->verification_function);
                        $questions[$competitionUserQuestion->competition_question_id] = array(
                            'competition_question_id' => $competitionUserQuestion->competition_question_id,
                            'question_title' => $question->title,
                            'question_answer' => isset($ver_func[0]) ? $ver_func[0] : '',
                            'question_difficutlty' => $questionDifficulty->name,
                            'question_difficutlty_positive' => round(10 * $questionDifficulty->correct_answer_points) / 10,
                            'question_difficutlty_negative' => round(10 * $questionDifficulty->wrong_answer_points) / 10
                        );
                    }
                }
            }
            $row_data[$row['id']] = $row;
        }
        $question_additional_data = $questions;
        // order questions names
        $this->orderBy($questions, 'order by question_title asc', true, false);
        $header = array(
            'ID', 'Tekmovanje', 'Šola', 'Mentor'
        );
        if ($superuser) {
            $header[] = 'Mentor Uporabnik ID';
            $header[] = 'Mentor ID';
            $header[] = 'Mentor e-pošta';
        }
        $header[] = 'Kategorija';
        $header[] = 'Razred';
        $header[] = 'Priimek';
        $header[] = 'Ime';
        $header[] = 'Spol';
        $header[] = 'Diskvalificiran';
        if (self::canShowCompetitionResults($competition_id)) {
            $question_map = array();
            foreach ($questions as $question) {
                $header[] = $question['question_title'] . ' (' . $question['question_difficutlty'] . ' (' . $question['question_difficutlty_positive'] . '|' . $question['question_difficutlty_negative'] . ')) - ' . $question['question_answer'];
                $question_map[] = $question['competition_question_id'];
            }
            $header[] = 'Število točk';
            $header[] = 'Maksimalno število točk';
        }
        $header[] = 'Čas tekmovanja v minutah';
        if (self::canShowAwardField($competition_id)) {
            $header[] = 'Priznanje';
        }
        if (self::canShowAdvancingToNextLevel($competition_id)) {
            $header[] = 'Napreduje na naslednji nivo';
        }
        if ($superuser) {
            $header[] = 'IP naslov začetek';
            $header[] = 'IP naslov konec';
        }
        $escape_header = array();
        foreach ($header as $h) {
            $escape_header[] = '"' . $h . '"';
        }
        $list[] = implode(';', $escape_header);
        foreach ($row_data as $row) {
            $cols = array($row['id'], $row['competition'], $row['school'], $row['mentor']);
            if ($superuser) {
                $cols[] = $row['user_id'];
                $cols[] = $row['mentor_id'];
                $cols[] = $row['mentor_email'];
            }
            $cols[] = $row['category'];
            $cols[] = $row['class'];
            $cols[] = $row['last_name'];
            $cols[] = $row['first_name'];
            $cols[] = $row['gender'];
            $cols[] = $row['disqualified'] == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no');
            $total_points = 0;
            $start_points = 0;
            $max_points = 0;
            if (self::canShowCompetitionResults($competition_id)) {
                foreach ($question_map as $q) {
                    $start_points += abs($question_additional_data[$q]['question_difficutlty_negative']);
                    $max_points += $question_additional_data[$q]['question_difficutlty_positive'];
                    if (isset($row['questions'][$q])) {
                        $points = 0;
                        if ($row['questions'][$q] != '' && $row['questions'][$q] != NULL) {
                            if ($row['questions'][$q] == $question_additional_data[$q]['question_answer']) {
                                $points = $question_additional_data[$q]['question_difficutlty_positive'];
                            } else {
                                $points = $question_additional_data[$q]['question_difficutlty_negative'];
                            }
                        }
                        if ($points != 0) {
                            $total_points += $points;
                            $cols[] = $row['questions'][$q] . '|' . $points;
                        } else {
                            $cols[] = '';
                        }
                    } else {
                        $cols[] = '';
                    }
                }
                $cols[] = $start_points + $total_points;
                $cols[] = $start_points + $max_points;
            }
            $cols[] = $row['duration'];
            if (self::canShowAwardField($competition_id)) {
                $cols[] = $row['award'];
            }
            if (self::canShowAdvancingToNextLevel($competition_id)) {
                $cols[] = $row['advancing_to_next_level'] == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no');
            }
            if ($superuser) {
                $cols[] = $row['ip_start'];
                $cols[] = $row['ip_stop'];
            }
            $escape_cols = array();
            foreach ($cols as $c) {
                $escape_cols[] = '"' . $c . '"';
            }
            $list[] = implode(';', $escape_cols);
        }

        $content = implode("\n", $list);
        //OUPUT HEADERS
        // ob_clean();
        header("Pragma: public");
        header("Expires: 0");
        header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
        header("Cache-Control: private", false);
        header("Content-Type: application/octet-stream");
        header("Content-Disposition: attachment; filename=\"export-competition-results-" . date('Y-m-d') . ".csv\";");
        header("Content-Transfer-Encoding: binary");
        /* try {
          $export = iconv('utf-8', 'windows-1250', $content);
          } catch(Exception $e) {
          $export = $content;
          }
          die(); */
        $export = $content;
        // header("Content-Length: " . strlen($export));
        echo $export;
        die();
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

    public function exportActiveMentors($competition_id) {
        $list = array();

        $criteria = new CDbCriteria();
        $criteria->with = array(
            'competitionUsers', 'competitionUsers.competitionCategorySchoolMentor.user', 'competitionUsers.competitionCategorySchoolMentor.user.profile',
            'competitionUsers.competitionCategorySchoolMentor.competitionCategorySchool.school'
        );
        $criteria->together = true;
        $criteria->condition = 't.id=:competition_id';
        $criteria->params = array(':competition_id' => $competition_id);
        $competition = Competition::model()->find($criteria);
        // $competition = Competition::model()->findByPk($competition_id); // unoptimized
        if ($competition != null) {
            if ($competition == null) {
                $competition = new Competition();
            }
            foreach ($competition->competitionUsers as $user) {
                if (isset($user->competitionCategorySchoolMentor->user)) {
                    $mentorInfo = $user->competitionCategorySchoolMentor->user;
                    $data = array(
                        'mentor_id' => $mentorInfo->id,
                        'username' => $mentorInfo->username,
                        'first_name' => $mentorInfo->profile->first_name,
                        'last_name' => $mentorInfo->profile->last_name,
                        'email' => $mentorInfo->email,
                        'school_name' => $user->competitionCategorySchoolMentor->competitionCategorySchool->school->name,
                            /* 'count_competitiors' => CompetitionUser::model()->with('competitionCategorySchoolMentor')->together()->count('competition_id=:competition_id and competitionCategorySchoolMentor.user_id=:user_id', array(':competition_id' => $competition_id, ':user_id' => $mentorInfo->id)) */
                    );
                    if (!isset($list[$data['username']])) {
                        $list[$data['username']] = $data;
                    } else {
                        if ($list[$data['username']]['school_name'] != $data['school_name']) {
                            $list[$data['username']]['school_name'] .= ', ' . $data['school_name'];
                        }
                    }
                }
            }
        }
        $headers = array('Šola', 'Priimek', 'Ime', 'E-poštni naslov', 'Uporabniško ime', 'Mentor ID' /* 'Število tekmovalcev' */);
        $lines = array();
        $lines[] = implode(';', $headers);
        $this->orderBy($list, 'order by school_name asc, last_name asc, first_name asc', true, false);
        foreach ($list as $el) {
            $lines[] = implode(';', array($el['school_name'], $el['last_name'], $el['first_name'], $el['email'], $el['username'], $el['mentor_id'] /* , $el['count_competitiors'] */));
        }

        $content = implode("\n", $lines);
        //OUPUT HEADERS
        header("Pragma: public");
        header("Expires: 0");
        header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
        header("Cache-Control: private", false);
        header("Content-Type: application/octet-stream");
        header("Content-Disposition: attachment; filename=\"export-active-mentors-" . date('Y-m-d') . ".csv\";");
        header("Content-Transfer-Encoding: binary");
        $export = iconv('utf-8', 'windows-1250', $content);
        header("Content-Length: " . strlen($export));
        echo $export;
        die();
    }

    public function importCompetitiors($competition_id, $competition_category_id, $content) {
        $lines = explode("\n", $content);
        $header = explode(';', $lines[0]);
        $competition_questions = CompetitionQuestionCategory::model()->with('competitionQuestion')->with('competitionQuestion.question')->findAll('competition_category_id=:competition_category_id and competitionQuestion.competition_id=:competition_id', array(':competition_category_id' => $competition_category_id, ':competition_id' => $competition_id));
        $questions_to_import = array();
        foreach ($competition_questions as $cq) {
            if ($cq == null) {
                $cq = new CompetitionQuestionCategory();
            }
            $questions_to_import[trim($cq->competitionQuestion->question->title)] = $cq->competition_question_id;
        }
        echo 'Question to import:<br />';
        pre_print($questions_to_import);
        // map fields
        $colQuestionMap = array();
        $found_c = array();
        for ($i = 0; $i < count($header); ++$i) {
            $col = explode('(', $header[$i]);
            $c = trim($col[0]);
            if (isset($questions_to_import[$c])) {
                $colQuestionMap[$i] = $questions_to_import[$c];
                $found_c[] = $c;
            }
        }
        if (count($colQuestionMap) != count($questions_to_import)) {
            echo 'Question to import and question in CSV does not match!';
            echo 'Question to import:<br />';
            pre_print($questions_to_import);
            echo 'Found questions: <br />';
            pre_print($found_c);
            echo 'CSV header line cols: <br />';
            pre_print($header);
            echo 'Question column mapping found:<br />';
            pre_print($colQuestionMap);
            die();
        } else {
            echo 'Question column exist, we can start importing.<br />';
        }
        // check for required columns
        $required_fields = array(
            'Priimek' => -1,
            'Ime' => -1,
            'Mentor' => -1,
            'Šola' => -1,
            'Spol' => -1,
            'Razred' => -1,
        );
        $required_keys = array_keys($required_fields);
        // not required fields
        $required_fields['ID1'] = -1;
        $required_fields['ID2'] = -1;
        $required_keys2 = array_keys($required_fields);
        for ($i = 0; $i < count($header); ++$i) {
            if (in_array(trim($header[$i]), $required_keys2)) {
                $required_fields[trim($header[$i])] = $i;
            }
        }
        $missing_fields = array();
        for ($i = 0; $i < count($required_keys); ++$i) {
            if ($required_fields[$required_keys[$i]] == -1) {
                $missing_fields[] = $required_keys[$i];
            }
        }
        if (count($missing_fields) > 0) {
            echo 'Some required fields are missing:<br />';
            pre_print($missing_fields);
            die();
        }
        $competition = Competition::model()->findByPk($competition_id);
        if ($competition == null) {
            echo 'Provided Competition does not exist!';
            die();
        }
        $competitionCategory = CompetitionCategory::model()->findByPk($competition_category_id);
        if ($competitionCategory == null) {
            echo 'Provided Competition Category does not exist!';
            die();
        }

        for ($i = 1; $i < count($lines); ++$i) {
            if (trim($lines[$i]) == '') {
                continue;
            }
            $cols = explode(';', $lines[$i]);
            $cu = new CompetitionUser();
            $cu->competition_category_id = $competition_category_id;
            $cu->competition_id = $competition_id;
            $cu->first_name = $cols[$required_fields['Ime']];
            $cu->last_name = $cols[$required_fields['Priimek']];
            $cu->gender = $cols[$required_fields['Spol']] == 'M' ? 0 : 1;
            $cu->class = $cols[$required_fields['Razred']];

            $sc = School::model()->find('name=:name', array(':name' => trim($cols[$required_fields['Šola']])));
            if ($sc == null) {
                echo 'Provided school not found in database! School name: ', $cols[$required_fields['Šola']], '<br />';
                die();
            }
            $cu->school_id = $sc->id;

            $scm = SchoolMentor::model()->with('user.profile')->find('school_id=:school_id and CONCAT_WS(\' \', `profile`.`last_name`, `profile`.`first_name`) LIKE :mentor', array(':school_id' => $sc->id, ':mentor' => trim($cols[$required_fields['Mentor']])));
            if ($scm == null) {
                echo 'Provided school mentor not found in database! School name: ', $cols[$required_fields['Šola']], ', School mentor: ', $cols[$required_fields['Mentor']], '<br />';
                die();
            }

            // ali je šola prijavljena na tekmovanje za to kategorijo
            $ccs = CompetitionCategorySchool::model()->find('competition_id=:competition_id and competition_category_id=:competition_category_id and school_id=:school_id', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id, ':school_id' => $sc->id));
            if ($ccs == null) {
                echo 'Provided school is not competing in this category! School name: ', $cols[$required_fields['Šola']], ', Competition: ', $competition->name, ', Competition category: ', $competitionCategory->name, '<br />';
                die();
            }

            // ali je mentor prijavljen na tej šoli za to tekmovalno kategorijo
            $ccsm = CompetitionCategorySchoolMentor::model()->find('competition_category_school_id=:competition_category_school_id and user_id=:user_id', array(':competition_category_school_id' => $ccs->id, ':user_id' => $scm->user_id));
            if ($ccsm == null) {
                echo 'Provided mentor is not competing on this school on this competition in this category! School mentor: ', $cols[$required_fields['Mentor']], ', School name: ', $cols[$required_fields['Šola']], ', Competition: ', $competition->name, ', Competition category: ', $competitionCategory->name, '<br />';
                die();
            }

            $cu->competition_category_school_mentor_id = $ccsm->id;
            $cu->start_time = null;
            $cu->finish_time = null;
            $cu->finished = 2;

            if (isset($cols[$required_fields['ID1']])) {
                $cut = CompetitionUser::model()->findByPk($cols[$required_fields['ID1']]);
                if ($cut != null) {
                    if ($cut == null) {
                        $cut = new CompetitionUser();
                    }
                    $cu->start_time = $cut->start_time;
                    $cu->finish_time = $cut->finish_time;
                    $cut->disqualified_reason = 'Prenos v pravilno kategorijo tekmovanja';
                    $cut->disqualified_request = 1;
                    $cut->disqualified = 1;
                    $cut->save();
                }
            }

            if (isset($cols[$required_fields['ID2']])) {
                $cut = CompetitionUser::model()->findByPk($cols[$required_fields['ID2']]);
                if ($cut != null) {
                    if ($cut == null) {
                        $cut = new CompetitionUser();
                    }
                    if ($cu->start_time == null) {
                        $cu->start_time = $cut->start_time;
                        $cu->finish_time = $cut->finish_time;
                    } else {
                        $time_diff1 = strtotime($cu->finish_time) - strtotime($cu->start_time);
                        $time_diff2 = strtotime($cut->finish_time) - strtotime($cut->start_time);
                        if ($time_diff2 > $time_diff1) {
                            $cu->start_time = $cut->start_time;
                            $cu->finish_time = $cut->finish_time;
                        }
                    }
                    $cut->disqualified_reason = 'Prenos v pravilno kategorijo tekmovanja';
                    $cut->disqualified_request = 1;
                    $cut->disqualified = 1;
                    $cut->save();
                }
            }

            // ali tekmovalec s temi podatki že obstaja
            $cuc = CompetitionUser::model()->find('competition_id=:competition_id and competition_category_id=:competition_category_id and competition_category_school_mentor_id=:competition_category_school_mentor_id and school_id=:school_id and first_name=:first_name and last_name=:last_name and gender=:gender and class=:class', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id, ':competition_category_school_mentor_id' => $cu->competition_category_school_mentor_id, ':school_id' => $cu->school_id, ':last_name' => $cu->last_name, ':first_name' => $cu->first_name, ':gender' => $cu->gender, ':class' => $cu->class));
            if ($cuc != null) {
                echo 'Competition User already exists, skipping...';
                continue;
            }
            $cu->save();
            // import answers
            $question_keys = array_keys($colQuestionMap);
            for ($k = 0; $k < count($question_keys); ++$k) {
                $cuq = new CompetitionUserQuestion();
                $cuq->competition_user_id = $cu->id;
                $cuq->competition_question_id = $colQuestionMap[$question_keys[$k]];
                $cuq->ordering = $k + 1;
                $cuq->random_seed = number_format(mt_rand(0, mt_getrandmax() - 1) / mt_getrandmax(), 9, '.', '');
                $cuq->last_change = $cu->finish_time;
                $custom_answer_ex = explode('|', $cols[$question_keys[$k]]);
                $custom_answer = trim($custom_answer_ex[0]);
                $cuq->custom_answer = $custom_answer;
                $cuq->save();
            }
            echo 'Successfully imported user with ID: ', $cu->id, '<br />';
        }
    }

    public function GetDisqualifiedOptions($empty = false) {
        $options = array(
            1 => Yii::t('app', 'no'),
            2 => Yii::t('app', 'yes'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All'));
        }
        return $options;
    }

    public function GetDisqualifiedName($value) {
        if ($value == 1) {
            return Yii::t('app', 'yes');
        } else {
            return Yii::t('app', 'no');
        }
    }

    public function GetAdvancingToNextLevelOptions($empty = false) {
        $options = array(
            1 => Yii::t('app', 'no'),
            2 => Yii::t('app', 'yes'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All'));
        }
        return $options;
    }

    public static function canShowAdvancingToNextLevel($competition_id) {
        $superuser = Generic::isSuperAdmin();
        if (!$superuser) {
            // check if visible by competition settings
            $cache_key = 'CCompetition-mentor-advancing-timestamp-' . $competition_id;
            $cache = Yii::app()->cache->get($cache_key);
            if ($cache == null) {
                $competition = Competition::model()->findByPk($competition_id);
                if ($competition != null) {
                    $cache = $competition->timestamp_mentor_advancing_to_next_level == null ? '-' : $competition->timestamp_mentor_advancing_to_next_level;
                } else {
                    $cache = '-';
                }
                Yii::app()->cache->set($cache_key, $cache, 600);
            }
            if ($cache == '-') {
                return false;
            } else {
                $timestamp = strtotime($cache);
                if ($timestamp > time()) {
                    return false;
                }
            }
        }
        return true;
    }

    public function GetAdvancingToNextLevelName($value) {
        if (!self::canShowAdvancingToNextLevel($this->competition_id)) {
            return Yii::t('app', 'Not known yet.');
        }
        if ($value == 1) {
            return Yii::t('app', 'yes');
        } else {
            return Yii::t('app', 'no');
        }
    }

    public function calculateCompetitionAwards($competition_id, $competition_category_id) {
        // reset awards to null to all competitiors
        CompetitionUser::model()->updateAll(array('award' => NULL), 'competition_id=:competition_id and competition_category_id=:competition_category_id', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id));
        $cus = CompetitionUser::model()->findAll('competition_id=:competition_id and competition_category_id=:competition_category_id and disqualified=:disqualified', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id, ':disqualified' => 0));
        $whole_competition = array();
        $competition_per_school = array();
        $totalpoints = 0;
        foreach ($cus as $cu) {
            if ($cu == null) {
                $cu = new CompetitionUser();
            }
            $result = $cu->getCompetitionNumericResult(true);
            if ($totalpoints == 0) {
                $totalpoints = (int) $result['totalpoints'];
            }
            $whole_competition[] = array(
                'id' => $cu->id,
                'result' => (int) $result['result']
            );
            if (!isset($competition_per_school[$cu->school_id])) {
                $competition_per_school[$cu->school_id] = array();
            }
            $competition_per_school[$cu->school_id][] = array(
                'id' => $cu->id,
                'result' => (int) $result['result']
            );
        }
        Generic::orderBy($whole_competition, 'order by result desc', false, true);
        // 1/5 najboljših na tekmovanju prejme bronasto priznanje
        $awarded_users = array();
        $petina = ceil(count($whole_competition) / 5);
        $last_result = 0;
        for ($i = 0; $i < $petina; ++$i) {
            $awarded_users[] = $whole_competition[$i]['id'];
            $last_result = $whole_competition[$i]['result'];
        }
        // add users with same result as the last one in petina
        for ($i = $petina; $i < count($whole_competition); ++$i) {
            if ($last_result == $whole_competition[$i]['result']) {
                $awarded_users[] = $whole_competition[$i]['id'];
            } else {
                break;
            }
        }
        // max 1/3 na šoli, če le dosežejo tekmovalci vsaj polovico vseh točk
        $totalpointshalf = round($totalpoints / 2);
        $awards_per_school = array();
        foreach ($competition_per_school as $school_id => $competitors) {
            $awards_per_school[$school_id] = 0;
            Generic::orderBy($competitors, 'order by result desc', false, true);
            echo "Competitors on school with ID: ", $school_id, "<br />";
            pre_print($competitors);
            $tretjina = ceil(count($competitors) / 3);
            $process_edge = true; // če je pred tretjino tekmovalec z manj kot polovico točk, ne gledamo več tekmovalcev ob robu tretjine
            $last_result = 0;
            for ($i = 0; $i < $tretjina; ++$i) {
                if ($competitors[$i]['result'] >= $totalpointshalf) {
                    if (!in_array($competitors[$i]['id'], $awarded_users)) {
                        $awarded_users[] = $competitors[$i]['id'];
                    }
                    $awards_per_school[$school_id] ++;
                    $last_result = $competitors[$i]['result'];
                } else {
                    $process_edge = false;
                }
            }
            if ($process_edge) {
                for ($i = $tretjina; $i < count($competitors); ++$i) {
                    if ($last_result == $competitors[$i]['result']) {
                        if (!in_array($competitors[$i]['id'], $awarded_users)) {
                            $awarded_users[] = $competitors[$i]['id'];
                        }
                        $awards_per_school[$school_id] ++;
                    } else {
                        break;
                    }
                }
            }
        }

        echo "Awards per school: <br />";
        pre_print($awards_per_school);

        // save awards to database
        for ($i = 0; $i < count($awarded_users); ++$i) {
            CompetitionUser::model()->updateAll(array('award' => 5), 'id=:id', array(':id' => $awarded_users[$i]));
        }

        return true;
    }

    public function calculateCompetitionAdvancingToNextLevel($competition_id, $competition_category_id, $number_of_points_needed_for_advancing_to_next_level = 0) {
        if ($number_of_points_needed_for_advancing_to_next_level == 0) {
            return false;
        }
        // reset advancing_to_next_level to null to all competitiors
        CompetitionUser::model()->updateAll(array('advancing_to_next_level' => 0), 'competition_id=:competition_id and competition_category_id=:competition_category_id', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id));
        $cus = CompetitionUser::model()->findAll('competition_id=:competition_id and competition_category_id=:competition_category_id and disqualified=:disqualified', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id, ':disqualified' => 0));
        foreach ($cus as $cu) {
            if ($cu == null) {
                $cu = new CompetitionUser();
            }
            $result = $cu->getCompetitionNumericResult(true);
            if (((int) $result['result']) >= $number_of_points_needed_for_advancing_to_next_level) {
                $cu->advancing_to_next_level = 1;
                $cu->save(true, array('advancing_to_next_level'));
            }
        }
        return true;
    }

    public function GetAwardOptions($empty = false) {
        $options = array(
            1 => Yii::t('app', 'Award for participation'),
            5 => Yii::t('app', 'Bronze award'),
            10 => Yii::t('app', 'Silver award'),
            15 => Yii::t('app', 'Gold award'),
        );
        if ($empty) {
            array_unshift($options, Yii::t('app', 'All awards'));
        }
        return $options;
    }

    public static function canShowAwardField($competition_id) {
        $superuser = Generic::isSuperAdmin();
        if (!$superuser) {
            // check if visible by competition settings
            $cache_key = 'CCompetition-mentor-awards-timestamp-' . $competition_id;
            $cache = Yii::app()->cache->get($cache_key);
            if ($cache == null) {
                $competition = Competition::model()->findByPk($competition_id);
                if ($competition != null) {
                    $cache = $competition->timestamp_mentor_awards == null ? '-' : $competition->timestamp_mentor_awards;
                } else {
                    $cache = '-';
                }
                Yii::app()->cache->set($cache_key, $cache, 600);
            }
            if ($cache == '-') {
                return false;
            } else {
                $timestamp = strtotime($cache);
                if ($timestamp > time()) {
                    return false;
                }
            }
        }
        return true;
    }

    public function GetAwardName($award) {
        $show = self::canShowAwardField($this->competition_id);
        if (!$show) {
            return Yii::t('app', 'Competition awards are not available yet.');
        }
        $options = array(
            1 => Yii::t('app', 'Award for participation'),
            5 => Yii::t('app', 'Bronze award'),
            10 => Yii::t('app', 'Silver award'),
            15 => Yii::t('app', 'Gold award'),
        );
        if (isset($options[$award])) {
            return $options[$award];
        }
        return '';
    }

}
