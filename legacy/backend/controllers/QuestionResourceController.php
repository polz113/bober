<?php

class QuestionResourceController extends Controller {

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
                'actions' => array('index', 'view', 'create', 'update', 'admin', 'delete', 'activate', 'deactivate', 'adminget'),
                'users' => array('@'),
            ),
            array('allow', 'actions' => array('get'), 'users' => array('*')),
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
            $model = new QuestionResource;

            // Uncomment the following line if AJAX validation is needed
            // $this->performAjaxValidation($model);

            if (isset($_POST['QuestionResource'])) {
                $model->attributes = $_POST['QuestionResource'];

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
            if (isset($_POST['QuestionResource'])) {
                $model->attributes = $_POST['QuestionResource'];

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
            $model = new QuestionResource('search');
            $model->unsetAttributes();  // clear any default values

            if (isset($_GET['QuestionResource'])) {
                $model->attributes = $_GET['QuestionResource'];
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
        $model = QuestionResource::model()->findByPk($id);

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
        if (isset($_POST['ajax']) && $_POST['ajax'] === 'question-resource-form') {
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
        if ($action == 'get') {
            $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
            // demo
            if ($competition_user_id != 0) {
                return true;
            }
        } else if ($action == 'index') {
            
        } else if ($action == 'admin') {
            
        } else if ($action == 'create') {
            
        } else if ($action == 'update') {
            
        } else if ($action == 'delete') {
            
        } else if ($action == 'view') {
            
        } else if ($action == 'activate') {
            
        } else if ($action == 'deactivate') {
            
        } else if ($action == 'adminget') {
            $superuser = Generic::isSuperAdmin();
            if ($superuser) {
                return true;
            }
        }
        $user_role = Generic::getUserRole();
        $allowed = false;

        if ($user_role >= 10) {
            $allowed = true;
        }

        return $allowed;
    }

    public function actionGet() {
        $starttime = microtime(true);
        if ($this->CanAccess('get')) {
            $keys = array_keys($_GET);
            if (count($keys) == 0) {
                die();
            }
            $question_id = $keys[0];

            $superuser = Generic::isSuperAdmin();
            $user_role = Generic::getUserRole();
            $allow = false;
            if ($superuser || $user_role >= 10) {
                $allow = true;
            }
            $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
            Yii::app()->session->close();

            $criteria = new CDbCriteria();
            $criteria->limit = 1;
            $criteria->join = 'INNER JOIN competition_question on t.competition_question_id = competition_question.id';
            $criteria->condition = 't.competition_user_id = :competition_user_id AND competition_question.question_id = :question_id';
            $criteria->params = array(':question_id'=>$question_id, ':competition_user_id' => $competition_user_id);
            
            $competition_user_question = CompetitionUserQuestion::model()->find($criteria);
            //$competition_user_question = CompetitionUserQuestion::model()->with('competitionQuestion')->find('competitionQuestion.question_id=:question_id and t.competition_user_id=:competition_user_id', array(':question_id' => $question_id, ':competition_user_id' => $competition_user_id));
            if ($competition_user_question != null) {
                $allow = true;
            }
            if ($allow) {
                $path = '';
                foreach ($_GET as $key => $value) {
                    $path .= $key . '/';
                    if ($value != '') {
                        $path .= $value . '/';
                    }
                }
                $path = trim(mb_substr($path, mb_strpos($path, '/', 0, 'UTF-8') + 1, mb_strlen($path, 'UTF-8'), 'UTF-8'), '/');
                $filename = trim(mb_substr($path, mb_strrpos($path, '/', 0, 'UTF-8'), mb_strlen($path, 'UTF-8'), 'UTF-8'), '/');
                $language_code = mb_substr($path, 0, mb_strpos($path, '/', 0, 'UTF-8'), 'UTF-8');
                $path = ltrim(mb_substr($path, mb_strpos($path, '/', 0, 'UTF-8'), mb_strrpos($path, '/', 0, 'UTF-8') - mb_strpos($path, '/', 0, 'UTF-8'), 'UTF-8'), '/');
                if ($path != '') {
                    $path .= '/';
                }
                /*
                  echo "<pre>";
                  echo "Question ID: ";
                  print_r($question_id);
                  echo "\n";
                  echo "Language code: ";
                  print_r($language_code);
                  echo "\n";
                  var_dump($path);
                  echo "\n";
                  print_r($filename);
                  echo "</pre>";
                  die(); */
                $cache_id = 'bober-' . $question_id . '-' . $language_code . '-' . $path . '-' . $filename;
                $questionResourceArray = Yii::app()->cache->get($cache_id);
                if ($questionResourceArray === false) {
                    $questionResource = QuestionResource::model()->with('language')->find('question_id=:question_id and language.short=:language_code and path=:path and filename=:filename', array(':question_id' => $question_id, ':filename' => $filename, ':path' => $path, ':language_code' => $language_code));
                    if ($questionResource == null) {
                        $questionResource = new QuestionResource();
                        die();
                    }
                    $questionResourceArray = array(
                        'data' => $questionResource->data,
                        'file_type' => $questionResource->file_type,
                        'length' => strlen($questionResource->data)
                    );
                    if ($questionResourceArray['length'] > 1000000) {
                        // cannot go to memcache
                    } else {
                        Yii::app()->cache->set($cache_id, $questionResourceArray, 1800);
                    }
                }
                if (isset($questionResourceArray['length'])) {
                    header('Pragma: public');
                    header('Expires: 0');
                    header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
                    header('Content-Transfer-Encoding: binary');
                    header('Content-length: ' . $questionResourceArray['length']);
                    header('Content-Type: ' . $questionResourceArray['file_type']);
                    header('X-Content-Type-Options: nosniff');
                    header('X-Frame-Options: SAMEORIGIN');
                    header('Connection: close');
                    echo $questionResourceArray['data'];
                }
                die();
            } else {
                die();
            }
        } else {
            die();
        }
    }

    public function actionAdminGet() { // adminget/<id>/show
        $starttime = microtime(true);
        $questionResourceArray = array();
        if ($this->CanAccess('adminget')) {
            $keys = array_keys($_GET);
            if (count($keys) == 0) {
                die();
            }
            $question_resource_id = $keys[0];
            $questionResource = QuestionResource::model()->findByPk($question_resource_id);
            if ($questionResource == null) {
                $questionResource = new QuestionResource();
                die();
            }
            $questionResourceArray = array(
                'data' => $questionResource->data,
                'file_type' => $questionResource->file_type,
                'length' => strlen($questionResource->data)
            );
        }
        if (isset($questionResourceArray['length'])) {
            header('Pragma: public');
            header('Expires: 0');
            header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
            header('Content-Transfer-Encoding: binary');
            header('Content-length: ' . $questionResourceArray['length']);
            header('Content-Type: ' . $questionResourceArray['file_type']);
            header('X-Content-Type-Options: nosniff');
            header('X-Frame-Options: SAMEORIGIN');
            header('Connection: close');
            echo $questionResourceArray['data'];
        }
        die();
    }

}

?>
