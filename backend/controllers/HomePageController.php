<?php

class HomePageController extends Controller {

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
            $model = new User;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);



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
        header('Location: /index.php/HomePage');
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

    
    
    public function GetSchoolCoordinatorList() {
       //Zlistat listo Šola (Koordinator: Ime Priimek ) return $this-> . ' ( Coordinator: ' . $this-> . ' )';
    }

    /**
     * Performs the AJAX validation.
     * @param CModel the model to be validated
     */
    protected function performAjaxValidation($model) {
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'home-page-form') {
            echo CActiveForm::validate($model);
            Yii::app()->end();
        }
    }

    public function actionChangeLanguage() {
        $language = Yii::app()->getRequest()->getParam('lang', '');
        if ($language == '') {
            unset(Yii::app()->session['preffered_language']);
        } else {
            Yii::app()->session['preffered_language'] = $language;
        }
        header('Location: /index.php/HomePage');
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