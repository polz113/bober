<?php

class StartCompetitionController extends Controller {

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
                'actions' => array('index', 'view', 'create', 'changeLanguage'),
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

    /**
     * Creates a new model.
     * If creation is successful, the browser will be redirected to the 'view' page.
     */
    public function actionCreate() {
        if ($this->CanAccess('create')) {
            // just statically set the preferred_language for now.
            Yii::app()->session['preferred_language'] = Yii::app()->params['preferred_language'];
            // Yii::app()->session['preferred_language'] = 'sl';
            $model = new CompetitionUser;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);
            if (isset($_POST['CompetitionUser'])) {
                unset(Yii::app()->session['errorMsg']);
                $model->attributes = $_POST['CompetitionUser'];
                $search = $model->checkAccessCode();
                $isOk = true;
                if (trim($model->first_name) == '') {
                    $model->addError('first_name', Yii::t('app', 'Missing first name!'));
                    $isOk = false;
                }
                if (trim($model->last_name) == '') {
                    $model->addError('last_name', Yii::t('app', 'Missing last name!'));
                    $isOk = false;
                }
                if (trim($model->class_numberic) == '') {
                    $model->addError('class', Yii::t('app', 'Missing class!'));
                    $isOk = false;
                }
                /*
                if (trim($model->class) == '') {
                    $model->addError('class', Yii::t('app', 'Missing class!'));
                    $isOk = false;
                }*/
                if ($search == '') {
                    $model->addError('access_code', Yii::t('app', 'Access code is wrong!'));
                    $isOk = false;
                }

                if (!in_array($model->gender, array(0, 1))) {
                    $model->addError('gender', Yii::t('app', 'Wrong gender!'));
                    $isOk = false;
                }


                if ($search != null && $isOk) {
                    if ($search->competitionCategorySchool->competitionCategory->class_from <= $model->class_numberic && $model->class_numberic <= $search->competitionCategorySchool->competitionCategory->class_to) {
                        // ok
                    } else {
                        $model->addError('access_code', Yii::t('app', 'Access code is invalid for this class!'));
                        $isOk = false;
                    }
                    $competition = $search->competitionCategorySchool->competition;
                    if (!$competition->active) {
                        $model->addError('access_code', Yii::t('app', 'Competition didn\'t start yet!'));
                        $isOk = false;
                    }
                    // check if competition did even start ?
                    /* Commented out so that people can test competiton */
                    if (strtotime($competition->timestamp_start) > time()) {
                        $model->addError('access_code', Yii::t('app', 'Competition didn\'t start yet!'));
                        $isOk = false;
                    }
                    // check if competition is already complete ?
                    if (strtotime($competition->timestamp_stop) < time()) {
                        $model->addError('access_code', Yii::t('app', 'Competition already finished!'));
                        $isOk = false;
                    }
                }

                if ($search != null && $isOk) {
                    $competitionUser = CompetitionUser::model()->find('first_name=:first_name and last_name=:last_name and class=:class and competition_id=:competition_id and competition_category_id=:competition_category_id and school_id=:school_id and competition_category_school_mentor_id=:competition_category_school_mentor_id', array(
                        ':first_name' => trim($model->first_name),
                        ':last_name' => trim($model->last_name),
                        ':class' => trim($model->class_numberic . '.' . trim($model->class)),
                        ':competition_id' => $search->competitionCategorySchool->competition_id,
                        ':competition_category_id' => $search->competitionCategorySchool->competition_category_id,
                        ':school_id' => $search->competitionCategorySchool->school_id,
                        ':competition_category_school_mentor_id' => $search->id
                    ));

                    if ($competitionUser != null && $isOk) {
                        if ($competitionUser->finished == 1 || $competitionUser->finish_time != null) {
                            Yii::app()->session['errorMsg'] = Yii::t('app', 'User already finished competition.');
                        } else {
                            Yii::app()->session['competition_user_id'] = $competitionUser->id;
                            $this->redirect(array('view', 'id' => $competitionUser->id));
                        }
                    } else {
                        $model->first_name = mb_convert_case(trim($model->first_name), MB_CASE_TITLE, 'UTF-8');
                        $model->last_name = mb_convert_case(trim($model->last_name), MB_CASE_TITLE, 'UTF-8');
                        $model->class = trim($model->class_numberic . '.' . trim($model->class));
                        $model->competition_id = $search->competitionCategorySchool->competition_id;
                        $model->competition_category_id = $search->competitionCategorySchool->competition_category_id;
                        $model->school_id = $search->competitionCategorySchool->school_id;
                        $model->ip_start = isset($_SERVER) && isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '/';
                        // to ID mentorje, tukaj naj v osnovi linkal z IDijem uporabnika, tekmovalca
                        // $model->user_id = $search->user_id;
                        $model->competition_category_school_mentor_id = $search->id;

                        if ($model->save()) {
                            Yii::app()->session['competition_user_id'] = $model->id;
                            // if AJAX request , we should not redirect the browser
                            if (!Yii::app()->request->isAjaxRequest) {
                                $this->redirect(array('view', 'id' => $model->id));
                            } else {
                                // UNCOMMENT THIS IF YOU WANT TO RETURN ID OF THE NEWLY CREATED 
                                // OBJECT (USEFUL WHEN CREATING NEW OBJECTS VIA AJAX AND INFO ABOUT
                                // THEN NEWLY CREATED OBJECT MUST BE SENT TO THE BROWSER)
                                // echo CJSON::encode(array('error' => '', 'id' => $model->id));
                                // die();
                            }
                        } else {
                            Yii::app()->session['errorMsg'] = Yii::t('app', 'Error registering user for competition.');
                            if (!Yii::app()->request->isAjaxRequest) {
                                
                            } else {
                                throw new CHttpException(400, Yii::t('app', 'Bad request. The request cannot be fulfilled.'));
                            }
                        }
                    }
                }
            }

            if (!Yii::app()->request->isAjaxRequest) {
                $this->render('create', array('model' => $model));

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
        header('Location: /index.php/StartCompetition');
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

    /**
     * Performs the AJAX validation.
     * @param CModel the model to be validated
     */
    protected function performAjaxValidation($model) {
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'start-competition-form') {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }

    public function actionChangeLanguage() {
        $language = Yii::app()->getRequest()->getParam('lang', '');
        if ($language == '') {
            // unset(Yii::app()->session['preferred_language']);
           Yii::app()->session['preferred_language'] = Yii::app()->params['language'];
        } else {
            Yii::app()->session['preferred_language'] = $language;
        }
        header('Location: /index.php/StartCompetition');
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
