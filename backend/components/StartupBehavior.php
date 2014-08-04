<?php

class StartupBehavior extends CBehavior {

    public function attach($owner) {
        $owner->attachEventHandler('onBeginRequest', array($this, 'beginRequest'));
    }

    public function beginRequest(CEvent $event) {
        if (isset(Yii::app()->session['preffered_language'])) {
            $language = Yii::app()->session['preffered_language'];
        }else{
            $language = Yii::app()->request->getPreferredLanguage();
        }
        if ($language == 'sl_si') {
            $language = 'sl';
        }
        // echo $language, "<br />";
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        // load locale / language / timezone
        if ($user != null && isset($user->profile->language_id)) {
            $languageObject = Language::model()->find('id=:id', array(':id' => $user->profile->language_id));
            if ($languageObject != null) {
                $language = $languageObject->short;
            }
        }
        $timezone = 'Europe/Ljubljana';
        if ($user != null && isset($user->profile->timezone) && $user->profile->timezone != '') {
            $timezone = $user->profile->timezone;
        }
        Yii::app()->language = $language;
        Yii::app()->localtime->Locale = $language;
        Yii::app()->localtime->TimeZone = $timezone;
        
        // routing default controller based on domain
        $sender = $event->sender;
        if ($_SERVER['HTTP_HOST'] == 'boberadmin.comcode.si' || $_SERVER['HTTP_HOST'] == 'backend.bober') {
            // default controller
        }else{ 
            // tekmovalni url
            $sender->defaultController = 'startCompetition';
        }
    }

}

?>