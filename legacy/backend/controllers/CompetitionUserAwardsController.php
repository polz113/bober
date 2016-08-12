<?php

class CompetitionUserAwardsController extends Controller {

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
                'actions' => array('index', 'admin'),
                'users' => array('@'),
            ),
            array('deny', // deny all users
                'users' => array('*'),
            ),
        );
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
            return false;
        }

        return false;
    }

}
