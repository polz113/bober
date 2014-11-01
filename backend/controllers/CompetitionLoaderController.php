<?php

class CompetitionLoaderController extends Controller {

    public function init() {
        if (Yii::app()->browser->getBrowser() == Browser::BROWSER_IE && Yii::app()->browser->getVersion() < 8) {
            die('Unsupported browser. Please use at least IE8');
        }
        Yii::app()->theme = "Bober";
        parent::init();
    }

    public function actionIndex() {
        $redirect = false;
        $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
        if ($competition_user_id == 0) {
            $redirect = true;
            header('Location: /index.php/StartCompetition');
            die();
        }
        $competitionUser = CompetitionUser::model()->findByPk($competition_user_id);
        if ($competitionUser != null) {
            if ($competitionUser == null) {
                $competitionUser = new CompetitionUser();
            }
            if ($competitionUser->start_time != null) {
                $duration = $competitionUser->competition->duration * 60;
                $starttime = strtotime($competitionUser->start_time);
                $endtime = $starttime + $duration;
                if ($competitionUser->finished == 1 || $competitionUser->finish_time != null) {
                    if ($competitionUser->finished == 1 && $competitionUser->finish_time == null) {
                        $competitionUser->finish_time = $endtime;
                        $competitionUser->save(true, array('finish_time'));
                    } else {
                        $competitionUser->finished = 1;
                        $competitionUser->save(true, array('finished'));
                    }
                    $redirect = true;
                } else {
                    if ($endtime < time()) {
                        $competitionUser->finished = 1;
                        $competitionUser->finish_time = $endtime;
                        $competitionUser->save(true, array('finished', 'finish_time'));
                        $redirect = true;
                    }
                }
            }
        } else {
            $redirect = true;
        }
        if ($redirect) {
            header('Location: /index.php/StartCompetition');
            die();
        }
        $this->render('index');
    }
    
    public function actionChangeLanguage() {
        $language = Yii::app()->getRequest()->getParam('lang', '');
        if ($language == '') {
            unset(Yii::app()->session['preferred_language']);
        }else{
            Yii::app()->session['preferred_language'] = $language;
        }
        header('Location: /index.php/CompetitionLoader');
        die();
    }

    // Uncomment the following methods and override them if needed
    /*
      public function filters()
      {
      // return the filter configuration for this controller, e.g.:
      return array(
      'inlineFilterName',
      array(
      'class'=>'path.to.FilterClass',
      'propertyName'=>'propertyValue',
      ),
      );
      }

      public function actions()
      {
      // return external action classes, e.g.:
      return array(
      'action1'=>'path.to.ActionClass',
      'action2'=>array(
      'class'=>'path.to.AnotherActionClass',
      'propertyName'=>'propertyValue',
      ),
      );
      }
     */
}
