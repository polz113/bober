<?php

class MentorRegistrationController extends Controller {

    /**
     * @var string the default layout for the views. Defaults to '//layouts/column2', meaning
     * using two-column layout. See 'protected/views/layouts/column2.php'.
     */
    public $layout = '//layouts/column2';

    public function init() {

        if (Yii::app()->browser->getBrowser() == Browser::BROWSER_IE && Yii::app()->browser->getVersion() < 8) {
            die('Unsupported browser. Please use at least IE8');
        }
        Yii::app()->theme = "Bober";
        parent::init();
    }

    /**
     * @return array action filters
     */
    public function filters() {
        return array(
            'accessControl', // perform access control for CRUD operations
            'postOnly + delete', // we only allow deletion via POST request
        );
    }

    /**
     * Specifies the access control rules.
     * This method is used by the 'accessControl' filter.
     * @return array access control rules
     */
    public function accessRules() {
        return array(
            array('allow', // allow authenticated user to perform all available actions
                'actions' => array('index', 'view', 'create', 'changeLanguage', 'loadSchools'),
                'users' => array('*'),
            ),
            array('deny', // deny all users
                'users' => array('*'),
            ),
        );
    }

    /**
     * Displays a particular model.
     * @param integer $id the ID of the model to be displayed
     */
    public function actionView($id) {
        $model = $this->loadModel($id);

        if ($this->CanAccess('view') && $model->CanView()) {
            $this->render('view', array('model' => $model));
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    public static function encrypting($string = "") {
        $hash = Yii::app()->getModule('user')->hash;
        if ($hash == "md5")
            return md5($string);
        if ($hash == "sha1")
            return sha1($string);
        else
            return hash($hash, $string);
    }

    /**
     * Creates a new model.
     * If creation is successful, the browser will be redirected to the 'view' page.
     */
    public function actionCreate() {
        if ($this->CanAccess('create')) {
            $model = new User;
            $profile = new Profile;
            $schoolMentor = new SchoolMentor;

            if (isset($_POST['User'])) {
                $model->attributes = $_POST['User'];
                $model->activkey = $this->encrypting(microtime() . $model->password);
                $profile->attributes = $_POST['Profile'];
                $profile->user_id = 0;
                $profile->timezone = 'Europe/Ljubljana';
                $profile->user_role = 5;
                $model->country_id = $profile->country_id;
                $custom_error = false;
                $modelValidate = $model->validate();
                
                if ($model->password == '') {
                    $model->addError('password', Yii::t('app', 'Password can not be empty!'));
                    $custom_error = true;
                }
                $schoolMentorPost = Yii::app()->getRequest()->getPost('SchoolMentor', array());
                if(!isset($schoolMentorPost['school_id']) || (isset($schoolMentorPost['school_id']) && $schoolMentorPost['school_id'] == '') ){
                   $schoolMentor->addError('school_id', Yii::t('app', 'School must be choosen!'));
                   $custom_error = true;
                }
                if ($modelValidate && $profile->validate() && !$custom_error) {
                    $model->password = $this->encrypting($model->password);
                    if ($model->save()) {
                        $profile->user_id = $model->id;
                        if ($profile->save()) {
                            
                            $schoolMentor->user_id = $model->id;                
                            $schoolMentor->school_id = isset($schoolMentorPost['school_id']) ? $schoolMentorPost['school_id'] : null;
                            $schoolMentor->coordinator = isset($schoolMentorPost['coordinator']) ? $schoolMentorPost['coordinator'] : 0;
                            $schoolMentor->active = 0;
                            $schoolMentor->save();
                            $activation_url = $this->createAbsoluteUrl('/user/activation/activation', array("activkey" => $model->activkey, "email" => $model->email));
                            UserModule::sendMail($model->email, UserModule::t("You registered from {site_name}", array('{site_name}' => Yii::app()->name)), UserModule::t("Please activate you account go to {activation_url}", array('{activation_url}' => $activation_url)));
                        }
                    }
                    $this->redirect(array('view', 'id' => $model->id));
                } else {
                    $profile->validate();
                }
            } else {
                $model->country_id = 0;
                $profile->country_id = 0;
            }


            if (!Yii::app()->request->isAjaxRequest) {
                $this->render('create', array('model' => $model, 'profile' => $profile, 'school_mentor' => $schoolMentor));

                // IF YOU NEED DIFFERENT RENDERING FOR AJAX AND NON-AJAX CALLS, 
                // USE THIS LINE AND DELETE THE LINE ABOVE
                // $this->render('create', array('model' => $model, 'ajaxRendering' => false));
            } else {
                throw new CHttpException(400, Yii::t('app', 'Bad request. The request cannot be fulfilled.'));

                // IF YOU NEED DIFFERENT RENDERING FOR AJAX AND NON-AJAX CALLS, 
                // USE THIS LINE AND DELETE THE LINE ABOVE
                // $this->renderPartial('create', array('model' => $model, 'ajaxRendering' => true));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    private static function redirectToStart() {
        header('Location: /index.php/MentorRegistration');
        die();
    }

    /**
     * Lists all models.
     */
    public function actionIndex() {
        $this->actionCreate();
    }

    /**
     * Returns the data model based on the primary key given in the GET variable.
     * If the data model is not found, an HTTP exception will be raised.
     * @param integer the ID of the model to be loaded
     */
    public function loadModel($id) {
        $model = CompetitionUser::model()->findByPk($id);

        if ($model === null) {
            throw new CHttpException(404, Yii::t('app', 'The requested page does not exist.'));
        }

        return $model;
    }

    public function actionLoadSchools() {
        $userData = Yii::app()->getRequest()->getPost('Profile', array());
        $country_id = isset($userData['country_id']) ? $userData['country_id'] : 0;
        if ($country_id != 0) {
            $data = School::model()->findAll('country_id=:country_id', array(':country_id' => $country_id));

            $listData = array();
            foreach ($data as $models) {
                $value = $models['id'];
                $coordinator = SchoolMentor::model()->find('school_id=:school_id', array(':school_id' => $value));
                if ($coordinator != null || $coordinator != 0) {

                    $name = $coordinator->user->profile->first_name;
                    $lastName = $coordinator->user->profile->last_name;

                    $text = $models['name'] . ' ( ' . Yii::t('app', 'Coordinator') . ': ' . $name . ' ' . $lastName . ' )';
                } else {
                    $text = $models['name'];
                }
                $listData[$value] = $text;
            }

            $data = $listData;

            // $data = CHtml::listData($data,"id","name");
            echo CHtml::tag('option', array('value' => 'choose'), Yii::t('app', 'choose'), true);
            foreach ($data as $value => $name) {
                //CHtml::encode($name)
                echo CHtml::tag('option', array('value' => $value), $name, true);
            }
        } else {
            echo 'Invalid country';
        }
    }

    /**
     * Performs the AJAX validation.
     * @param CModel the model to be validated
     */
    protected function performAjaxValidation($model) {
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'mentor-registration-form') {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }

    public function actionChangeLanguage() {
        $language = Yii::app()->getRequest()->getParam('lang', '');
        if ($language == '') {
            unset(Yii::app()->session['preferred_language']);
        } else {
            Yii::app()->session['preferred_language'] = $language;
        }
        header('Location: /index.php/MentorRegistration');
        die();
    }

    /**
     * Determines whether access to specific action is allowed or not.
     * @param string $action the action to which the access is validated
     * @return boolean true if access to specific action is allowed; false otherwise
     */
    private function CanAccess($action = "") {
        if ($action == 'index') {
            
        } else if ($action == 'create') {
            
        } else if ($action == 'view') {
            
        }


        return true;
    }

}

?>
