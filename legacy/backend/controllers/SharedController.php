<?php

class SharedController extends Controller {

    public function actionIndex() {
        $user_id = isset(Yii::app()->user->id) ? Yii::app()->user->id : 0;
        $list = array();
        if ($user_id != 0) {
            $dir = dirname(__FILE__) . '/../../shared/' . $user_id . '/';
            if (is_dir($dir)) {
                $files = scandir($dir);
                for ($i = 0; $i < count($files); $i++) {
                    if (!in_array($files[$i], array('.', '..')) && is_file($dir . $files[$i])) {
                        $list[] = array('id' => $i, 'name' => $files[$i], 'key' => base64_encode($files[$i]), 'title' => Yii::t('app', 'Download'));
                    }
                }
            }
            // list mentor directories
            $mentors = SchoolMentor::model()->findAll('user_id=:user_id', array(':user_id' => $user_id));
            foreach ($mentors as $mentor) {
                $dir = dirname(__FILE__) . '/../../shared/M' . $mentor->id . '/';
                if (is_dir($dir)) {
                    $files = scandir($dir);
                    for ($i = 0; $i < count($files); $i++) {
                        if (!in_array($files[$i], array('.', '..')) && is_file($dir . $files[$i])) {
                            $list[] = array('id' => $i, 'name' => $files[$i], 'key' => base64_encode("M".$files[$i]), 'title' => Yii::t('app', 'Download'));
                        }
                    }
                }
            }
        }
        $this->render('index', array('list' => $list));
    }

    public function actionGet() {
        $key = Yii::app()->request->getParam('key', null);
        if ($key != null) {
            $key = base64_decode($key);
            $key = str_replace('/', '', $key);
            $user_id = isset(Yii::app()->user->id) ? Yii::app()->user->id : 0;
            $dir = dirname(__FILE__) . '/../../shared/' . $user_id . '/';
            if (is_dir($dir)) {
                if (file_exists($dir . '/' . $key)) {
                    header("Pragma: public");
                    header("Expires: 0");
                    header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
                    header("Cache-Control: private", false);
                    header("Content-Disposition: attachment; filename=\"" . $key . "\";");
                    header('Content-type: ' . CFileHelper::getMimeType($dir . '/' . $key));
                    header("Content-Transfer-Encoding: binary");
                    readfile($dir . '/' . $key);
                    die();
                }
            }

            // list mentor directories
            $mentors = SchoolMentor::model()->findAll('user_id=:user_id', array(':user_id' => $user_id));
            $key = mb_substr($key, 1, mb_strlen($key, 'UTF-8') - 1, 'UTF-8');
            foreach ($mentors as $mentor) {
                $dir = dirname(__FILE__) . '/../../shared/M' . $mentor->id . '/';
                if (is_dir($dir)) {
                    if (file_exists($dir . '/' . $key)) {
                        header("Pragma: public");
                        header("Expires: 0");
                        header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
                        header("Cache-Control: private", false);
                        header("Content-Disposition: attachment; filename=\"" . $key . "\";");
                        header('Content-type: ' . CFileHelper::getMimeType($dir . '/' . $key));
                        header("Content-Transfer-Encoding: binary");
                        readfile($dir . '/' . $key);
                        die();
                    }
                }
            }
        }
    }

}
