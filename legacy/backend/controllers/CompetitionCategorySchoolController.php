<?php

class CompetitionCategorySchoolController extends Controller {

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
                'actions' => array('index', 'view', 'create', 'update', 'admin', 'delete', 'activate', 'deactivate', 'import', 'export', 'importnextlevel'),
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
            $model = new CompetitionCategorySchool;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionCategorySchool'])) {
                $model->attributes = $_POST['CompetitionCategorySchool'];
                // check if unique
                $check = CompetitionCategorySchool::model()->find('competition_id=:competition_id and school_id=:school_id and competition_category_id=:competition_category_id', array(
                    ':competition_category_id' => $model->competition_category_id,
                    ':school_id' => $model->school_id,
                    ':competition_id' => $model->competition_id
                ));
                if ($check == null) {
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
                }else{
                    throw new CHttpException(403, Yii::t('app', 'This school in this category on this competition is already signed up.'));
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
            if (isset($_POST['CompetitionCategorySchool'])) {
                $model->attributes = $_POST['CompetitionCategorySchool'];

                if ($model->save()) {
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
            $model = new CompetitionCategorySchool('search');
            $model->unsetAttributes();  // clear any default values

            if (isset($_GET['CompetitionCategorySchool'])) {
                $model->attributes = $_GET['CompetitionCategorySchool'];
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

    public function actionImport() {
        if ($this->CanAccess('import')) {
            $model = new CompetitionCategorySchool;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionCategorySchool'])) {
                $model->attributes = $_POST['CompetitionCategorySchool'];
                // pre_print($model->competition_id);
                $model->country_id = $_POST['CompetitionCategorySchool']['country_id'];
                // pre_print($_FILES['CompetitionCategorySchool']);
                // die();
                // pre_print($model->country_id);
                // pre_print($_POST);
                if ($model->competition_id != 0 && $model->country_id != 0) {
                    $csv = iconv('WINDOWS-1250', 'UTF-8', file_get_contents($_FILES['CompetitionCategorySchool']['tmp_name']['uploadedData']));
                    // pre_print($csv);
                    $model->importMentorsWithCodes($model->competition_id, $model->country_id, $csv);
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

    public function actionImportNextLevel() {
        if ($this->CanAccess('import')) {
            $model = new CompetitionCategorySchool;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionCategorySchool'])) {
                $model->attributes = $_POST['CompetitionCategorySchool'];
                // pre_print($model->competition_id);
                $model->country_id = $_POST['CompetitionCategorySchool']['country_id'];
                // pre_print($_FILES['CompetitionCategorySchool']);
                // die();
                // pre_print($model->country_id);
                // pre_print($_POST);
                if ($model->competition_id != 0 && $model->country_id != 0) {
                    $csv = iconv('WINDOWS-1250', 'UTF-8', file_get_contents($_FILES['CompetitionCategorySchool']['tmp_name']['uploadedData']));
                    // pre_print($csv);
                    $model->importMentorsWithIdsAndCodes($model->competition_id, $model->country_id, $csv);
                } else {
                    throw new CHttpException(403, Yii::t('app', 'Invalid competition'));
                }
            } else {
                $this->render('importnextlevel', array('model' => $model));
            }
        } else {
            throw new CHttpException(405, Yii::t('app', 'You do not have permissions to access this page.'));
        }
    }
    
    public function actionExport() {
        if ($this->CanAccess('export')) {
            $model = new CompetitionCategorySchool;
             if (isset($_POST['CompetitionCategorySchool'])) {
                $model->attributes = $_POST['CompetitionCategorySchool'];
                $model->exportMentorsWithCodes($model->competition_id);
             } else {
                 $this->render('export', array('model' => $model));
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
        $model = CompetitionCategorySchool::model()->findByPk($id);

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
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'competition-category-school-form') {
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
        $user_role = Generic::getUserRole();
        $allowed = false;
        if ($user_role >= 5) {
            $allowed = true;
        }
        if ($action == 'index') {
            
        } else if ($action == 'admin') {
            
        } else if ($action == 'create') {
            
        } else if ($action == 'update') {
            
        } else if ($action == 'delete') {
            
        } else if ($action == 'view') {
            
        } else if ($action == 'activate') {
            
        } else if ($action == 'deactivate') {
            
        } else if ($action == 'import') {
            if (!$superuser) {
                $allowed = false;
            }
        }else if ($action == 'export') {
            if (!$superuser) {
                $allowed = false;
            }
        }

        return $allowed;
    }

}
