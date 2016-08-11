<?php

class CompetitionUserController extends Controller {

    /**
     * @var string the default layout for the views. Defaults to '//layouts/column2', meaning
     * using two-column layout. See 'protected/views/layouts/column2.php'.
     */
    public $layout = '//layouts/column2';

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
                'actions' => array('index', 'view', 'create', 'update', 'admin', 'delete', 'activate', 'deactivate', 'checkdata', 'exportdata', 'exportactivementor', 'updatefinishtime', 'loadCompetitionCategory', 'loadCompetitionCategoryMentors', 'import', 'calculateawards', 'calculateadvancingtonextlevel'),
                'users' => array('@'),
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
            $model = new CompetitionUser;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];

                if ($model->CanUpdate() && $model->save()) {
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
                    throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
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

    /**
     * Updates a particular model.
     * If update is successful, the browser will be redirected to the 'view' page.
     * @param integer $id the ID of the model to be updated
     */
    public function actionUpdate($id) {
        $model = $this->loadModel($id);

        // Uncomment the following line if AJAX validation is needed
        // $this->performAjaxValidation($model);

        if ($this->CanAccess('update') && $model->CanUpdate()) {

            if (isset($_POST['CompetitionUser'])) {
                $can_edit = false;
                if (Generic::isSuperAdmin()) {
                    $model->attributes = $_POST['CompetitionUser'];
                    $can_edit = true;
                } else {
                    if ($model->competitionCategorySchoolMentor != null && $model->competitionCategorySchoolMentor->user_id == Yii::app()->user->id) {
                        $can_edit = true;
                        // load only attributes
                        $allowed_data = array();
                        $allowed_keys = array('last_name', 'first_name', 'gender', 'class', 'disqualified_request', 'disqualified_reason');
                        foreach ($allowed_keys as $key) {
                            $allowed_data[$key] = isset($_POST['CompetitionUser'][$key]) ? $_POST['CompetitionUser'][$key] : '';
                        }
                        if ($allowed_data['disqualified_request'] == '1' && $model->disqualified_request == 0) {
                            $model->disqualified_request_by = Yii::app()->user->id;
                        }
                        $model->attributes = $allowed_data;
                    }
                }

                if ($can_edit && $model->save()) {
                    // if AJAX request , we should not redirect the browser
                    if (!Yii::app()->request->isAjaxRequest) {
                        $this->redirect(array('view', 'id' => $model->id));
                    }
                }
            }

            if (!Yii::app()->request->isAjaxRequest) {
                $this->render('update', array('model' => $model));

                // IF YOU NEED DIFFERENT RENDERING FOR AJAX AND NON-AJAX CALLS, 
                // USE THIS LINE AND DELETE THE LINE ABOVE
                // $this->render('update', array('model' => $model, 'ajaxRendering' => false));
            } else {
                throw new CHttpException(400, Yii::t('app', 'Bad request. The request cannot be fulfilled.'));

                // IF YOU NEED DIFFERENT RENDERING FOR AJAX AND NON-AJAX CALLS, 
                // USE THIS LINE AND DELETE THE LINE ABOVE
                // $this->renderPartial('update', array('model' => $model, 'ajaxRendering' => true));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    /**
     * Deletes a particular model.
     * If deletion is successful, the browser will be redirected to the 'admin' page.
     * @param integer $id the ID of the model to be deleted
     */
    public function actionDelete($id) {
        $model = $this->loadModel($id);

        if ($this->CanAccess('delete') && $model->CanDelete()) {
            $model->delete();

            // if AJAX request (triggered by deletion via admin grid view), we should not redirect the browser
            if (!Yii::app()->request->isAjaxRequest) {
                $this->redirect(isset($_POST['returnUrl']) ? $_POST['returnUrl'] : array('admin'));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    /**
     * Lists all models.
     */
    public function actionIndex() {
        $this->actionAdmin();
    }

    /**
     * Manages all models.
     */
    public function actionAdmin() {
        if ($this->CanAccess("admin")) {
            $model = new CompetitionUser('search');
            $model->unsetAttributes();  // clear any default values

            if (isset($_GET['CompetitionUser'])) {
                $model->attributes = $_GET['CompetitionUser'];
            }

            $this->render('admin', array('model' => $model));
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    public function actionActivate($id) {
        $model = $this->loadModel($id);

        if ($this->CanAccess('activate') && $model->CanUpdate()) {
            $model->active = 1;

            if ($model->save()) {
                if (!Yii::app()->request->isAjaxRequest) {
                    $this->redirect(Yii::app()->request->urlReferrer);
                }
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    public function actionDeactivate($id) {
        $model = $this->loadModel($id);

        if ($this->CanAccess('deactivate') && $model->CanUpdate()) {
            $model->active = 0;

            if ($model->save()) {
                if (!Yii::app()->request->isAjaxRequest) {
                    $this->redirect(Yii::app()->request->urlReferrer);
                }
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
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
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'competition-user-form') {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }

    /**
     * Determines whether access to specific action is allowed or not.
     * @param string $action the action to which the access is validated
     * @return boolean true if access to specific action is allowed; false otherwise
     */
    private function CanAccess($action = "") {
        $superuser = Generic::isSuperAdmin();
        if ($superuser) {
            return true;
        }

        if ($action == 'index') {
            return true;
        } else if ($action == 'admin') {
            return true;
        } else if ($action == 'create') {
            return false;
        } else if ($action == 'update') {
            return true;
        } else if ($action == 'delete') {
            return false;
        } else if ($action == 'view') {
            return true;
        } else if ($action == 'activate') {
            return false;
        } else if ($action == 'deactivate') {
            return false;
        } else if ($action == 'checkdata') {
            return false;
        } else if ($action == 'exportdata') {
            return true;
        }

        return false;
    }

    public function actionCheckdata() {
        if ($this->CanAccess('checkdata')) {
            $model = new CompetitionUser();
            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
            }
            $this->render('checkdata', array('model' => $model));
        }
    }

    public function actionExportdata() {
        if ($this->CanAccess('exportdata')) {
            $model = new CompetitionUser();
            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
                if (isset($_POST['CompetitionUser']['competition_id']) && isset($_POST['CompetitionUser']['competition_category_id'])) {
                    $model->exportData($_POST['CompetitionUser']['competition_id'], $_POST['CompetitionUser']['competition_category_id']);
                    die();
                }
            }
            $this->render('exportdata', array('model' => $model));
        }
    }

    public function actionExportactivementor() {
        if ($this->CanAccess('exportactivementor')) {
            $model = new CompetitionUser();
            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
                if (isset($_POST['CompetitionUser']['competition_id'])) {
                    $model->exportActiveMentors($_POST['CompetitionUser']['competition_id']);
                    die();
                }
            }
            $this->render('exportactivementor', array('model' => $model));
        }
    }

    public function actionUpdatefinishtime() {
        $users = CompetitionUser::model()->with('competition')->together()->findAll('finish_time IS NULL or finished=:finished', array(':finished' => 0));
        foreach ($users as $user) {
            if ($user->start_time != null) {
                $starttime = strtotime($user->start_time);
                $max_finish_time = $starttime + $user->competition->duration * 60;
                if ($user->finish_time == null) {
                    if (time() > $max_finish_time) {
                        $user->finish_time = date('Y-m-d H:i:s', $max_finish_time);
                    }
                }
                if (time() >= $max_finish_time) {
                    if ($user->finished == 0) {
                        $user->finished = 2; // system finished
                    }
                }
                $user->save();
            }
        }
    }

    public function actionLoadCompetitionCategory() {
        if ($this->CanAccess('loadCompetitionCategory')) {
            if (Yii::app()->request->isAjaxRequest) {
                $competition_id = Yii::app()->request->getParam('competition_id');
                $model_id = Yii::app()->request->getParam('model_id');
                if ($model_id != '') {
                    $model = CompetitionUser::model()->findByPk($model_id);
                } else {
                    $model = CompetitionUser::model();
                }
                if ($competition_id != '') {
                    $data = CompetitionCategory::model()->with('competitionQuestionCategories')->with('competitionQuestionCategories.competitionQuestion')->together()->findAll('competitionQuestion.competition_id=:competition_id', array(':competition_id' => $competition_id));
                    echo CJSON::encode(CHtml::listData($data, 'id', 'name'));
                }
            }
        }
    }

    public function actionLoadCompetitionCategoryMentors() {
        if ($this->CanAccess('loadCompetitionCategoryMentors')) {
            if (Yii::app()->request->isAjaxRequest) {
                $competition_id = Yii::app()->request->getParam('competition_id');
                $competition_category_id = Yii::app()->request->getParam('competition_category_id');
                $model_id = Yii::app()->request->getParam('model_id');
                if ($model_id != '') {
                    $model = CompetitionUser::model()->findByPk($model_id);
                } else {
                    $model = CompetitionUser::model();
                }
                if ($competition_id != '' && $competition_category_id != '') {
                    // $data = CompetitionCategorySchoolMentor::model()->with('competitionCategorySchool')->with()->together()->findAll('competitionCategorySchool.competition_id=:competition_id and competitionCategorySchool.competition_category_id=:competition_category_id', array(':competition_id' => $competition_id, ':competition_category_id' => $competition_category_id));
                    $data = array();
                    $provider = CompetitionCategorySchoolMentor::model()->search(true, $competition_id, $competition_category_id);
                    foreach ($provider->getData() as $mentor) {
                        $data[] = array(
                            'id' => $mentor->id,
                            'name' => $mentor->competitionCategorySchool->school->name . ' - ' . $mentor->user->profile->last_name . ' ' . $mentor->user->profile->last_name
                        );
                    }
                    $model->orderBy($data, 'order by name asc', true, false);
                    echo CJSON::encode(Chtml::listData($data, 'id', 'name'));
                }
            }
        }
    }

    public function actionImport() {
        if ($this->CanAccess('import')) {
            $model = new CompetitionUser;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
                if ($model->competition_id != 0 && $model->competition_category_id != 0) {
                    $csv = iconv('WINDOWS-1250', 'UTF-8', file_get_contents($_FILES['CompetitionUser']['tmp_name']['uploadedData']));
                    // pre_print($csv);
                    $model->importCompetitiors($model->competition_id, $model->competition_category_id, $csv);
                } else {
                    throw new CHttpException(403, Yii::t('app', 'Invalid competition'));
                }
            } else {
                $this->render('import', array('model' => $model));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

    public function actionCalculateAwards() {
        if ($this->CanAccess('calculateawards')) {
            $model = new CompetitionUser;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
                if ($model->competition_id != 0 && $model->competition_category_id != 0) {
                    $model->calculateCompetitionAwards($model->competition_id, $model->competition_category_id);
                } else {
                    throw new CHttpException(403, Yii::t('app', 'Invalid competition'));
                }
            } else {
                $this->render('calculateawards', array('model' => $model));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }
    
    public function actionCalculateAdvancingToNextLevel() {
        if ($this->CanAccess('calculateadvancingtonextlevel')) {
            $model = new CompetitionUser;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionUser'])) {
                $model->attributes = $_POST['CompetitionUser'];
                if ($model->competition_id != 0 && $model->competition_category_id != 0 && $model->number_of_points_needed_for_advancing_to_next_level != 0) {
                    $model->calculateCompetitionAdvancingToNextLevel($model->competition_id, $model->competition_category_id, $model->number_of_points_needed_for_advancing_to_next_level);
                } else {
                    throw new CHttpException(403, Yii::t('app', 'Invalid competition'));
                }
            } else {
                $this->render('calculateadvancingtonextlevel', array('model' => $model));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }

}
