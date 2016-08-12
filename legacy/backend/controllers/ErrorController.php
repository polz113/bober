<?php

class ErrorController extends Controller {
    
    public function init() {
        if (Yii::app()->browser->getBrowser() == Browser::BROWSER_IE && Yii::app()->browser->getVersion() < 8) {
            die('Unsupported browser. Please use at least IE8');
        }
        Yii::app()->theme = "Bober";
        parent::init();
    }

    public function actionError() {
        if ($error = Yii::app()->errorHandler->error) {
            // error happen, we are in production lets render some nice error
            if (Yii::app()->request->isAjaxRequest) {
                echo 'Sorry, error happened!';
            } else {
                $this->render('error', $error);
            }
        }
    }

}
