<?php

class CompetitionCategorySchoolMentorController extends Controller {

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
                'actions' => array('index', 'view', 'create', 'update', 'admin', 'delete', 'activate', 'deactivate'),
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
            $model = new CompetitionCategorySchoolMentor;

// Uncomment the following line if AJAX validation is needed
// $this->performAjaxValidation($model);

            if (isset($_POST['CompetitionCategorySchoolMentor'])) {
                $model->attributes = $_POST['CompetitionCategorySchoolMentor'];

                if ($model->CanUpdate()) {
                    $counter = 0;
                    $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
                    // $user_id = $user != null ? $user->id : 0;
                    // $model->user_id = $user_id; // hallo!! ?? to pa ne more delat
                    do {
                        do {
                            $length = 10;
                            $chars = array_merge(range(0, 9), range('a', 'z'), range('A', 'Z'));
                            shuffle($chars);
                            $model->access_code = implode(array_slice($chars, 0, $length));
                            $model->disqualifiedBy = $user;
                            $check = CompetitionCategorySchoolMentor::model()->find('access_code=:access_code', array(':access_code' => $model->access_code));
                        } while ($check != null);
                        $counter++;
                        $saved = $model->save();
                    } while (!$saved && $counter < 10);
                    if ($saved) {
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
                        throw new CHttpException(405, Yii::t('app', 'Error adding record.'));
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
            if (isset($_POST['CompetitionCategorySchoolMentor'])) {
                $model->attributes = $_POST['CompetitionCategorySchoolMentor'];

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
            $model = new CompetitionCategorySchoolMentor('search');
            $model->unsetAttributes();  // clear any default values

            if (isset($_GET['CompetitionCategorySchoolMentor'])) {
                $model->attributes = $_GET['CompetitionCategorySchoolMentor'];
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

    public function GetCompetitionSchool(){
        return $this->competitionCategorySchool->competition->name . ' - ' . $this->competitionCategorySchool->school->name;
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
        $model = CompetitionCategorySchoolMentor::model()->findByPk($id);

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
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'competition-category-school-mentor-form') {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }

    /**
     * Determines whether access to specific action is allowed or not.
     * @param string $action the action to which the access is validated
     * @return boolean true if access to specific action is allowed; false otherwise
     */

    private function CanAccess($action = "")
    {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $user_role = $user != null ? $user->profile->user_role : 0;
        $allowed = false;
        if($user_role >= 5){
            $allowed = true;
        }
        if ($action == 'index')
        {
        }
        else if ($action == 'admin')
        {
        }
        else if ($action == 'create')
        {
        }
        else if ($action == 'update')
        {
        }
        else if ($action == 'delete')
        {
        }
        else if ($action == 'view')
        {
        }
        else if ($action == 'activate')
        {
        }
        else if ($action == 'deactivate')
        {
        }

        return $allowed;
    }

}
