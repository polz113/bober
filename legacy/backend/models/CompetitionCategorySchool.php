<?php

/**
 * This is the model class for table "competition_category_school".
 *
 * The followings are the available columns in table 'competition_category_school':
 * @property integer $id
 * @property integer $competition_id
 * @property integer $competition_category_id
 * @property integer $school_id
 *
 * The followings are the available model relations:
 * @property Competition $competition
 * @property CompetitionCategory $competitionCategory
 * @property School $school
 * @property CompetitionCategorySchoolMentor[] $competitionCategorySchoolMentors
 */
class CompetitionCategorySchool extends CActiveRecord
{

    public $competition_search;
    public $category_search;
    public $school_search;
    public $name;
    public $uploadedData;
    public $country_id;

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return CompetitionCategorySchool the static model class
     */
    public static function model($className = __CLASS__)
    {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName()
    {
        return 'competition_category_school';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules()
    {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('competition_id, competition_category_id, school_id', 'required'),
            array('competition_id, competition_category_id, school_id', 'numerical', 'integerOnly' => true),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, competition_id, competition_category_id, competition_search, school_search, category_search, school_id, uploadedData, country_id', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations()
    {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'competition' => array(self::BELONGS_TO, 'Competition', 'competition_id'),
            'competitionCategory' => array(self::BELONGS_TO, 'CompetitionCategory', 'competition_category_id'),
            'school' => array(self::BELONGS_TO, 'School', 'school_id'),
            'competitionCategorySchoolMentors' => array(self::HAS_MANY, 'CompetitionCategorySchoolMentor', 'competition_category_school_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels()
    {
        return array(
            'id' => Yii::t('app', 'id'),
            'competition_id' => Yii::t('app', 'Competition'),
            'competition_category_id' => Yii::t('app', 'Category'),
            'school_id' => Yii::t('app', 'School'),
            'country_id' => Yii::t('app', 'Country')
        );
    }

    public function getCanView()
    {
        return $this->CanView();
    }

    public function CanView()
    {
        $superuser = Generic::isSuperAdmin();
        $user_role = Generic::getUserRole();

        if ($superuser || $user_role >= 5) {
            return true;
        }
        return false;
    }

    public function getCanUpdate()
    {
        return $this->CanUpdate();
    }

    public function CanUpdate()
    {
        return $this->CanView();
    }

    public function getCanDelete()
    {
        return $this->CanDelete();
    }

    public function CanDelete()
    {
        return $this->CanView();
    }

    public function GetCompetitionNameIdList($get_only_competition_on_which_schools_you_are_mentor = false)
    {
        if ($get_only_competition_on_which_schools_you_are_mentor) {
            if (Generic::isSuperAdmin()) {
                $get_only_competition_on_which_schools_you_are_mentor = false;
            }
        }
        $list = array();
        if ($get_only_competition_on_which_schools_you_are_mentor) {
            $competitions = Competition::model()->with('competitionCategorySchools')->with('competitionCategorySchools.school')->with('competitionCategorySchools.school.schoolMentors')->findAll('schoolMentors.user_id=:user_id', array(':user_id' => Yii::app()->user->id));
            foreach ($competitions as $competition) {
                $competition['name'] = $competition->name;
                $list[] = $competition;
            }
        } else {
            $modelData = Competition::model()->search(true);
            foreach ($modelData->getData() as $competition) {
                $competition['name'] = $competition->name;
                $list[] = $competition;
            }
        }
        return $list;
    }

    public function GetCompetitionCategoryNameIdList()
    {
        $modelData = CompetitionCategory::model()->search(true);
        $list = array();
        foreach ($modelData->getData() as $competitionCategory) {
            $competitionCategory['name'] = $competitionCategory->name;
            $list[] = $competitionCategory;
        }
        return $list;
    }

    public function GetSchoolNameIdList($mentor_on_school_show_schools = false)
    {
        $modelData = School::model()->search(true, $mentor_on_school_show_schools);
        $list = array();
        foreach ($modelData->getData() as $school) {
            $school['name'] = $school->name;
            $list[] = $school;
        }
        return $list;
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false)
    {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('competition_id', $this->competition_id);
        $criteria->compare('competition_category_id', $this->competition_category_id);
        $criteria->compare('school_id', $this->school_id);
        $criteria->together = true;
        $criteria->with = array('competition', 'competitionCategory', 'school');
        $criteria->compare('`competition`.`name`', $this->competition_search, true);
        $criteria->compare('`competitionCategory`.`name`', $this->category_search, true);
        $criteria->compare('`school`.`name`', $this->school_search, true);

        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;

        if ($superuser == 1) {
            // ok
        } else {
            // $countryAministrator = CountryAdministrator::model()->findAll('user_id=:user_id', array(':user_id' => Yii::app()->user->id));
            $criteria->with[] = 'school.schoolMentors';
            $criteria->compare('`schoolMentors`.`user_id`', Yii::app()->user->id);
            $criteria->compare('`schoolMentors`.`coordinator`', 1);
            $criteria->together = true;
        }
        $criteria->order = '`competition`.`name` asc, `competitionCategory`.`name` asc, `school`.`name` asc';
        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }

        $options = array(
            'criteria' => $criteria,
            'sort' => array(
                'attributes' => array(
                    'competition_search' => array(
                        'asc' => 'competition.name',
                        'desc' => 'competition.name DESC'
                    ),
                    'category_search' => array(
                        'asc' => 'competitionCategory.name',
                        'desc' => 'competitionCategory.name DESC'
                    ),
                    'school_search' => array(
                        'asc' => 'school.name',
                        'desc' => 'school.name DESC'
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

    public static function encrypting($string = "")
    {
        $hash = Yii::app()->getModule('user')->hash;
        if ($hash == "md5")
            return md5($string);
        if ($hash == "sha1")
            return sha1($string);
        else
            return hash($hash, $string);
    }

    public function importMentorsWithCodes($competition_id, $country_id, $csv)
    {
        $country = Country::model()->findByPk($country_id);
        if ($country == null) {
            echo 'Country does not exist!';
            die();
        }
        header('Content-Type: text/html; charset=utf-8');
        if ($country->country == 'Srbija') { // popravek imen kategorij, ki se parsajo
            $cols = array(
                'E-poštni naslov' => 'email',
                'Telefon' => 'phone',
                'Ime' => 'name',
                'Priimek' => 'surname',
                'Država' => 'country',
                'Ime škole' => 'school',
                'Koordinator' => 'coordinator_on_school',
                'Uporabniško ime' => 'username',
                'Geslo' => 'password',
                'Dabarčić' => 'category_name_Dabarčić',
                'Mladi dabar' => 'category_name_Mladi dabar',
                'Dabar' => 'category_name_Dabar',
                'Stariji dabar' => 'category_name_Stariji dabar'
            );
        } else {
            $cols = array(
                'E-poštni naslov' => 'email',
                'Telefonska številka' => 'phone',
                'Ime' => 'name',
                'Priimek' => 'surname',
                'Država' => 'country',
                'Šola' => 'school',
                'Koordinator' => 'coordinator_on_school',
                'Uporabniško ime' => 'username',
                'Geslo' => 'password',
                'Bobrček' => 'category_name_Bobrček',
                'Mladi bober' => 'category_name_Mladi bober',
                'Bober' => 'category_name_Bober',
                'Stari bober' => 'category_name_Stari bober'
            );
        }

        $lines = explode("\n", trim($csv));
        $header_line = $lines[0];
        $header_cols = explode(';', trim($header_line));
        $keys = array_keys($cols);
        $cols_matrix = array();
        $index = 0;
        foreach ($header_cols as $h_cols) {
            $h_cols = trim($h_cols);
            if (in_array($h_cols, $keys)) {
                $cols_matrix[$index] = $cols[$h_cols];
                echo "Found:", $h_cols, "<br />";
            } else {
                echo "Not found:", $h_cols, "<br />";
            }
            $index++;
        }
        if (count($cols_matrix) != count($cols)) {
            echo 'One of required header columns is missing. Required columns: ', implode(', ', $keys), "<br />";
            echo 'Got cols: ', implode(', ', $header_cols), "<br />";
            echo 'Cols matrix: ', implode(', ', $cols_matrix), "<br />";
            die();
        }

        // pre_print($cols_matrix);

        $datas = array();
        for ($i = 1; $i < count($lines); ++$i) {
            $col = explode(';', trim($lines[$i]));
            $data = array();
            $index = 0;
            foreach ($col as $c) {
                $data[$cols_matrix[$index]] = trim($c);
                if (count(explode('category_name_', $cols_matrix[$index])) > 1 && in_array($data[$cols_matrix[$index]], array('srednja šola', 'osnovna šola', 'srednja šola)', 'osnovna šola)', 'Samo za srednje', 'Samo za osnovne'))) {
                    $data[$cols_matrix[$index]] = '';
                } else if ($cols_matrix[$index] == 'coordinator_on_school') {
                    if ($data[$cols_matrix[$index]] != '') {
                        $data['coordinator'] = true;
                    } else {
                        $data['coordinator'] = false;
                    }
                } else if ($cols_matrix[$index] == 'school') {
                    $school_name = trim($data['school']);
                    if ($school_name[0] == '"') {
                        $school_name = mb_substr($school_name, 1, mb_strlen($school_name, 'UTF-8') - 2, 'UTF-8');
                    }
                    $school_name = str_replace('""', '"', $school_name);

                    $school_check = School::model()->find('name=:name', array(':name' => $school_name));
                    if ($school_check != null) {
                        $data['school_id'] = $school_check->id;
                    } else {
                        echo 'Šola ne obstaja! Šola: ', $data['school'], '<br />';
                    }
                } else if ($cols_matrix[$index] == 'username') {
                    $data[$cols_matrix[$index]] = str_replace('.', '', $data[$cols_matrix[$index]]);
                    $data[$cols_matrix[$index]] = str_replace('á', 'a', $data[$cols_matrix[$index]]);
                }
                $index++;
            }
            if ($data['email'] == '' && $data['name'] == '') {
                continue;
            }
            if (count($data) != (count($keys) + 2)) {
                echo 'Record is invalid, it does not have all required fields. Skipping...<br />';
                echo count($data), ' vs. ', count($keys) + 2, '...<br />';
                pre_print($keys);
                pre_print($data);
                continue;
            }
            $datas[] = $data;
        }

        // pre_print($datas);
        // category matching to ids in database
        $category_matching = array();
        foreach ($cols_matrix as $mc) {
            $ex = explode('category_name_', $mc);
            if (count($ex) > 1) {
                $category_name = $ex[1];
                $competitionCategory = CompetitionCategory::model()->find('name=:name', array(':name' => $category_name));
                if ($competitionCategory == null) {
                    echo 'Competition category ', $category_name, ' not found in database!<br />';
                    die();
                } else {
                    $category_matching[$category_name] = $competitionCategory->id;
                }
            }
        }

        foreach ($datas as $data) {
            // check if user with this email already exists
            $check_email = User::model()->find('email=:email', array(':email' => $data['email']));
            $user_id = 0;
            if ($check_email != null) {
                echo 'User with email ', $data['email'], ' is already in system. Skipping importing user...<br />';
                $user_id = $check_email->id;
            }
            // check username
            $check_username = User::model()->find('username=:username', array(':username' => $data['username']));
            if ($check_username != null) {
                echo 'User with username ', $data['username'], ' is already in system. Skipping importing user...<br />';
                $user_id = $check_username->id;
            }

            // check if school exist
            if (!isset($data['school_id'])) {
                echo 'School ID not known! <br />';
                continue;
            }

            if ($user_id == 0) {
                $user = new User();
                $user->username = $data['username'];
                $user->password = $this->encrypting($data['password']);
                $user->email = $data['email'];
                $user->activkey = $this->encrypting(microtime() . $data['password']);
                $user->createtime = time();
                $user->superuser = 0;
                $user->status = 1;
                $user->create_at = date('Y-m-d H:i:s');
                if ($user->save()) {
                    $user_id = $user->id;
                    $profile = new Profile();
                    $profile->user_id = $user->id;
                    $profile->first_name = $data['name'];
                    $profile->last_name = $data['surname'];
                    $country = Country::model()->find('country=:country', array(':country' => $data['country']));
                    if ($country != null) {
                        $country_id = $country->id;
                    } else {
                        $country_id = 1;
                    }
                    $profile->country_id = $country_id;
                    $profile->language_id = 1;
                    $profile->user_role = 5;
                    $profile->timezone = 'Europe/Ljubljana';
                    $profile->phone_number = $data['phone'];
                    if (!$profile->save()) {
                        echo 'Error saving user profile!<br />';
                        pre_print($data);
                        die();
                    }
                } else {
                    echo 'Error saving user!<br />';
                    pre_print($user->errors);
                    pre_print($data);
                    die();
                }
            }

            if ($user_id != 0) {
                // add user as mentor to school
                $school_mentor_id = 0;
                $schoolMentor = SchoolMentor::model()->find('user_id=:user_id and school_id=:school_id', array(':user_id' => $user_id, ':school_id' => $data['school_id']));
                if ($schoolMentor == null) {
                    $schoolMentor = new SchoolMentor();
                    $schoolMentor->user_id = $user_id;
                    $schoolMentor->school_id = $data['school_id'];
                    if (isset($data['coordinator']) && $data['coordinator']) {
                        $schoolMentor->coordinator = 1;
                    }
                    $schoolMentor->active = 1;
                    $schoolMentor->activatedBy = 1;
                    $schoolMentor->activated_timestamp = date('Y-m-d H:i:s');
                    if ($schoolMentor->save()) {
                        $school_mentor_id = $schoolMentor->id;
                    } else {
                        echo 'Error adding user id ', $user_id, ' to be school mentor at school id ', $data['school_id'], '<br />';
                        die();
                    }
                } else {
                    $school_mentor_id = $schoolMentor->id;
                }
                // preveri ali je šola že prijavljena na tekmovanje s to kategorijo
                $competitionCategoryId = 0;
                foreach ($data as $key => $value) {
                    if (trim($value) == '') {
                        continue;
                    }
                    $ex = explode('category_name_', $key);
                    if (count($ex) > 1) {
                        $competitionCategoryId = $category_matching[$ex[1]];
                        $competitionCategorySchool = CompetitionCategorySchool::model()->find('competition_id=:cid and competition_category_id=:ccid and school_id=:school_id', array(':cid' => $competition_id, ':school_id' => $data['school_id'], ':ccid' => $competitionCategoryId));
                        if ($competitionCategorySchool == null) {
                            $competitionCategorySchool = new CompetitionCategorySchool();
                            $competitionCategorySchool->competition_id = $competition_id;
                            $competitionCategorySchool->competition_category_id = $competitionCategoryId;
                            $competitionCategorySchool->school_id = $data['school_id'];
                            if (!$competitionCategorySchool->save()) {
                                echo 'Error adding competiton category to school, school id: ', $data['school_id'], ', competiton_category_id: ', $competitionCategoryId, '<br />';
                                die();
                            }
                        }
                        // shranimo mentorja in njegovo tekmovalno kodo
                        $competitionCategorySchoolMentorCheck = CompetitionCategorySchoolMentor::model()->find('access_code=:access_code', array(':access_code' => $value));
                        if ($competitionCategorySchoolMentorCheck == null) {
                            $competitionCategorySchoolMentor = new CompetitionCategorySchoolMentor();
                            $competitionCategorySchoolMentor->user_id = $user_id;
                            $competitionCategorySchoolMentor->competition_category_school_id = $competitionCategorySchool->id;
                            $competitionCategorySchoolMentor->access_code = $value;
                            if (!$competitionCategorySchoolMentor->save()) {
                                echo 'Error adding access code for user!<br />';
                                pre_print($data);
                                die();
                            }
                        } else {
                            if ($competitionCategorySchoolMentorCheck->user_id == $user_id && $competitionCategorySchoolMentorCheck->competition_category_school_id == $competitionCategorySchool->id) {
                                // ok
                            } else {
                                echo 'Error adding access code! Access code already in use.<br />';
                                pre_print($data);
                                die();
                            }
                        }
                    }
                }
            }
        }
    }

    public function exportMentorsWithCodes($competition_id)
    {
        $data = array();
        $competition = Competition::model()->findByPk($competition_id);
        if ($competition != null) {
            if ($competition == null) {
                $competition = new Competition();
            }
            foreach ($competition->competitionCategorySchools as $competitionCategorySchool) {
                foreach ($competitionCategorySchool->competitionCategorySchoolMentors as $mentor) {
                    if ($mentor == null) {
                        $mentor = new CompetitionCategorySchoolMentor();
                    }

                    $email = $mentor->user->email;
                    $school = $mentor->competitionCategorySchool->school->name;
                    if (!isset($data[$email . $school])) {
                        $first_name = $mentor->user->profile->first_name;
                        $last_name = $mentor->user->profile->last_name;
                        $data[$email . $school] = array(
                            'email' => $email,
                            'username' => $mentor->user->username,
                            'first_name' => $first_name,
                            'last_name' => $last_name,
                            'school' => $school,
                            'coordinator' => SchoolMentor::model()->find("user_id=:user_id and school_id=:school_id and coordinator=:coordinator", array(':user_id' => $mentor->user_id, ':school_id' => $mentor->competitionCategorySchool->school_id, ':coordinator' => 1)) != null ? 'Da' : 'Ne',
                            'Bobrček' => '',
                            'Mladi bober' => '',
                            'Bober' => '',
                            'Stari bober' => '',
                        );
                    }
                    $category = $mentor->competitionCategorySchool->competitionCategory->name;
                    $access_code = $mentor->access_code;
                    $data[$email . $school][$category] = $access_code;
                }
            }

// data
            $lines = array();
            $lines[] = implode(';', array('E-poštni naslov', 'Uporabniško ime', 'Priimek', 'Ime', 'Šola', 'Koordinator', 'Bobrček', 'Mladi bober', 'Bober', 'Stari bober'));
            foreach ($data as $row) {
                $lines[] = implode(';', array($row['email'], $row['username'], $row['last_name'], $row['first_name'], $row['school'], $row['coordinator'], $row['Bobrček'], $row['Mladi bober'], $row['Bober'], $row['Stari bober']));
            }
            $content = implode("\n", $lines);
//OUPUT HEADERS
            header("Pragma: public");
            header("Expires: 0");
            header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
            header("Cache-Control: private", false);
            header("Content-Type: application/octet-stream");
            header("Content-Disposition: attachment; filename=\"export-mentor-with-codes-" . date('Y-m-d') . ".csv\";");
            header("Content-Transfer-Encoding: binary");
            $export = iconv('utf-8', 'windows-1250', $content);
            header("Content-Length: " . strlen($export));
            echo $export;
            die();
        }
    }

    public function importMentorsWithIdsAndCodes($competition_id, $country_id, $csv)
    {
        $country = Country::model()->findByPk($country_id);
        if ($country == null) {
            echo 'Country does not exist!';
            die();
        }

        $competition = Competition::model()->findByPk($competition_id);
        if ($competition == null) {
            echo 'Competition does not exist!';
            die();
        }

        header('Content-Type: text/html; charset=utf-8');
        if ($country->country == 'Srbija') { // popravek imen kategorij, ki se parsajo
            $cols = array(
                'Mentor ID' => 'mentor_id',
                'kategorija' => 'category_name',
                'koda' => 'access_code'
            );
        } else {
            $cols = array(
                'Mentor ID' => 'mentor_id',
                'kategorija' => 'category_name',
                'koda' => 'access_code'
            );
        }

        $lines = explode("\n", trim($csv));
        $header_line = $lines[0];
        $header_cols = explode(';', trim($header_line));
        $keys = array_keys($cols);
        $cols_matrix = array();
        $index = 0;
        foreach ($header_cols as $h_cols) {
            $h_cols = trim($h_cols);
            if (in_array($h_cols, $keys)) {
                $cols_matrix[$index] = $cols[$h_cols];
            }
            $index++;
        }
        if (count($cols_matrix) != count($cols)) {
            echo 'One of required header columns is missing. Required columns: ', implode(', ', $keys), "<br />";
            die();
        }

        // pre_print($cols_matrix);

        $datas = array();
        for ($i = 1; $i < count($lines); ++$i) {
            $col = explode(';', trim($lines[$i]));
            $data = array();
            $index = 0;
            foreach ($col as $c) {
                $data[$cols_matrix[$index]] = trim($c);
                $index++;
            }
            $datas[] = $data;
        }
        // pre_print($datas);
        $categoryCache = array();
        $imported = 0;
        foreach ($datas as $data) {
            if (isset($data['mentor_id']) && $data['mentor_id'] != '' && mb_substr($data['mentor_id'], 0, 1, 'UTF-8') == 'M') {
                $mentor_id = trim(ltrim($data['mentor_id'], "M"));
                $category_name = $data['category_name'];
                if (isset($categoryCache[$category_name])) {
                    $competition_category_id = $categoryCache[$category_name];
                } else {
                    $competitionCategory = CompetitionCategory::model()->find('country_id=:country_id and name=:name', array(':country_id' => $country_id, ':name' => $category_name));
                    if ($competitionCategory == null) {
                        echo 'Competition Category ', $category_name, ' cannot be found in database.';
                        die();
                    } else {
                        $categoryCache[$category_name] = $competitionCategory->id;
                        $competition_category_id = $categoryCache[$category_name];
                    }
                }
                $access_code = $data['access_code'];
                $schoolMentor = SchoolMentor::model()->findByPk($mentor_id);
                if ($schoolMentor == null) {
                    echo 'School mentor with ID: ', $mentor_id, ' could not be found!';
                    die();
                }

                // check if school already on competition in this category
                $competitionCategorySchool = CompetitionCategorySchool::model()->find(
                    'competition_id=:cid and competition_category_id=:ccid and school_id=:sid',
                    array(
                        ':cid' => $competition_id,
                        ':ccid' => $competition_category_id,
                        ':sid' => $schoolMentor->school_id
                    )
                );
                if ($competitionCategorySchool == null) {
                    $competitionCategorySchool = new CompetitionCategorySchool();
                    $competitionCategorySchool->competition_id = $competition_id;
                    $competitionCategorySchool->competition_category_id = $competition_category_id;
                    $competitionCategorySchool->school_id = $schoolMentor->school_id;
                    if (!$competitionCategorySchool->save()) {
                        echo 'Error saving competition category school!';
                        die();
                    }
                }

                // check if access code already in use
                $competitionCategorySchoolMentor = CompetitionCategorySchoolMentor::model()->find('access_code=:access_code', array(':access_code' => $access_code));
                if ($competitionCategorySchoolMentor != null) {
                    if ($competitionCategorySchoolMentor->user_id != $schoolMentor->user_id || $competitionCategorySchoolMentor->competition_category_school_id != $competitionCategorySchool->id) {
                        echo 'Cannot import access code: ', $access_code, ', because is already used by id: ', $competitionCategorySchoolMentor->id;
                        die();
                    }
                } else {
                    $competitionCategorySchoolMentor = new CompetitionCategorySchoolMentor();
                    $competitionCategorySchoolMentor->access_code = $access_code;
                    $competitionCategorySchoolMentor->competition_category_school_id = $competitionCategorySchool->id;
                    $competitionCategorySchoolMentor->user_id = $schoolMentor->user_id;
                    if (!$competitionCategorySchoolMentor->save()) {
                        echo 'Error saving CompetitionCategorySchoolMentor for access code: ', $access_code;
                        die();
                    } else {
                        $imported++;
                    }
                }
            } else {
                echo 'Error importing data: <br />';
                pre_print($data);
                die();
            }
        }
        echo '<br />Number of imported access codes: ', $imported;

    }

}
