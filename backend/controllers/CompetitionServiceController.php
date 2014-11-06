<?php

class CompetitionServiceController extends Controller {

    public function actionIndex() {
        $this->render('index');
    }

    public static function reponseJSON($object) {
        $json = json_encode($object);
        // self::logToFile(print_r(debug_backtrace(), true));
        // self::logToFile($json);
        $jsonp_callback = Yii::app()->getRequest()->getParam('callback', null);
        if ($jsonp_callback != null) {
            header('Content-type: application/javascript; charset=utf-8');
            echo $jsonp_callback, '(', $json, ');';
        } else {
            header('Content-Type: application/json; charset=utf-8');
            echo $json;
        }
        die();
    }

    public function actionGetQuestions() {
        $session = Yii::app()->session;
        $competition_user_id = $session['competition_user_id'] ? $session['competition_user_id'] : 0;
        if ($competition_user_id == 0) {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
        $competitionUser = CompetitionUser::model()->findByPk($competition_user_id);
        if ($competitionUser != null) {
            // we need to get that info somewhere
            /* $GetLanguageIds = QuestionResource::model()->with('question')->with('question.competitionQuestions')->findAll(array(
                'select' => 't.language_id',
                'distinct' => true,
                'condition' => 'competitionQuestions.competition_id=:competition_id',
                'params' => array(':competition_id' => $competitionUser->competition_id)
            ));
            $language_id = 1;
            if ($GetLanguageIds != null) {
                foreach ($GetLanguageIds as $record) {
                    $language_id = $record->language_id;
                    // echo 'Found Language ID: ', $record->language_id, '<br />';
                    // die();
                    break;
                }
            }
            $language = Language::model()->findByPk($language_id); 
            if ($language == null) {
                die('Language invalid');
            }
            $language_code = $language->short;*/
            // how about the session?
            if ($competitionUser->finished == 1 || $competitionUser->finish_time != null) {
                self::reponseJSON(array('success' => false, 'errorCode' => 999, 'error' => Yii::t('app', 'You have already finished competition.')));
            }
            if ($competitionUser->start_time != null) {
                $duration = $competitionUser->competition->duration * 60;
                $starttime = strtotime($competitionUser->start_time);
                $endtime = $starttime + $duration;
                if ($endtime < time()) {
                    $competitionUser->finished = 1;
                    $competitionUser->finish_time = $endtime;
                    $competitionUser->save(true, array('finished', 'finish_time'));
                    self::reponseJSON(array('success' => false, 'errorCode' => 999, 'error' => Yii::t('app', 'Your time is up. Questions won\'t be loaded!')));
                }
            }/*
            $count = CompetitionUserQuestion::model()->count('competition_user_id=:competition_user_id', array(':competition_user_id' => $competition_user_id));*/
            $language_code = $session['preferred_language'];
            // error_log("Lang:".$language_code);
            $language = Language::model()->findByAttributes(array('short'=>$language_code));
            $language_id = $language->id;
            if (!$competitionUser->questions_prepared) {
                $connection=Yii::app()->db;
                $transaction=$connection->beginTransaction();
                try
                {
                // error_log("Language code:".$language_code."id:".$language_id);
                // echo 'Adding new Competiton User Questions';
                // generate questions order for user
                    $criteria = new CDbCriteria();
                    $criteria->together = true;
                    $criteria->with = array('competitionQuestionCategories');
                    $criteria->condition = 't.competition_id=:competition_id and competitionQuestionCategories.competition_category_id=:competition_category_id';
                    $criteria->params = array(
                        ':competition_id' => $competitionUser->competition_id,
                        ':competition_category_id' => $competitionUser->competition_category_id
                    );
                    $criteria->order = 'RAND()';
                    $competitionQuestions = CompetitionQuestion::model()->findAll($criteria);
                    $order = 1;
                    foreach ($competitionQuestions as $competitionQuestion) {
                        $competitionUserQuestion = new CompetitionUserQuestion();
                        $competitionUserQuestion->competition_question_id = $competitionQuestion->id;
                        $competitionUserQuestion->competition_user_id = $competition_user_id;
                        $competitionUserQuestion->ordering = $order;
                        $random_seed = number_format(mt_rand(0, mt_getrandmax() - 1) / mt_getrandmax(), 9, '.', '');
                        $competitionUserQuestion->random_seed = $random_seed;
                        if (!$competitionUserQuestion->save()) {
                            var_dump($competitionUserQuestion->getErrors());
                            die();
                        }
                        $order++;
                    }
                    $competitionUser->questions_prepared = 1;
                    $competitionUser->save(true, array('questions_prepared'));
                    $transaction->commit();
                } 
                catch(Exception $e)
                {
                    error_log($e);
                    $transaction->rollback();
                }
            }
            // $count = CompetitionUserQuestion::model()->count('competition_user_id=:competition_user_id', array(':competition_user_id' => $competition_user_id));
            $competitionUserQuestions = CompetitionUserQuestion::model()->findAll(array('condition' => 'competition_user_id=:competition_user_id', 'params' => array(':competition_user_id' => $competition_user_id), 'order' => 'ordering ASC'));
            if ($competitionUserQuestions != null) {
                $questions = array();
                foreach ($competitionUserQuestions as $competitionUserQuestion) {
                    $question_id = $competitionUserQuestion->competitionQuestion->question_id;
                    $startup_file = QuestionResource::model()->find(
                            'question_id=:question_id and language_id=:language_id and type=:type and start_up=:start_up', array(
                        ':question_id' => $question_id,
                        ':language_id' => $language_id,
                        ':type' => 1,
                        ':start_up' => 1
                            )
                    );
                    if ($startup_file != null) {
                        $questions[] = array(
                            'id' => $question_id,
                            'title' => $competitionUserQuestion->competitionQuestion->question->title,
                            'country' => $competitionUserQuestion->competitionQuestion->question->country_of_origin,
                            'link' => $question_id . '/' . $language_code . '/' . $startup_file->path . $startup_file->filename,
                            'custom_answer' => ($competitionUserQuestion->custom_answer == null ? '' : $competitionUserQuestion->custom_answer),
                            'random_seed' => $competitionUserQuestion->random_seed,
                            'css' => $competitionUserQuestion->competitionQuestion->question->css
                        );
                    } else {
                        echo "Question: ", $question_id, "\n";
                        die('missing startup file for language id: '.$language_id.' question id: '.$question_id);
                    }
                }
                $response = array(
                    'success' => true,
                    'questions' => $questions,
                    'competition_title' => $competitionUser->competition->name,
                    'competition_length' => $competitionUser->competition->duration,
                    'seconds_to_end' => ($competitionUser->start_time == null ? -1 : $competitionUser->competition->duration * 60 - time() - strtotime($competitionUser->start_time))
                );
                self::reponseJSON($response);
            } else {
                self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'No questions defined for user.')));
            }
        } else {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
    }

    public function actionGetTimeToEndOfCompetition() {
        $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
        // demo
        if ($competition_user_id == 0) {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
        $competitionUser = CompetitionUser::model()->findByPk($competition_user_id);
        $fresh_start = false;
        if ($competitionUser != null) {
            if ($competitionUser == null) {
                $competitionUser = new CompetitionUser();
            }
            if ($competitionUser->start_time == null) {
                $fresh_start = true;
                $competitionUser->start_time = date('Y-m-d H:i:s');
                $competitionUser->save(true, array('start_time'));
            } else if ($competitionUser->finished == 1 || $competitionUser->finish_time != null) {
                self::reponseJSON(array('success' => false, 'errorCode' => 9, 'error' => Yii::t('app', 'User already finished competition.')));
            }
            $duration = $competitionUser->competition->duration * 60;
            $starttime = strtotime($competitionUser->start_time);
            $endtime = $starttime + $duration;
            if ($endtime < time()) {
                $competitionUser->finished = 1;
                $competitionUser->save(true, array('finished'));
                self::reponseJSON(array('success' => false, 'errorCode' => 9, 'error' => Yii::t('app', 'User time for solving competitions tasks is over.')));
            } else {
                $secondsToEnd = $endtime - time();
                self::reponseJSON(array('success' => true, 'seconds_to_end' => $secondsToEnd, 'fresh_start' => $fresh_start));
            }
        } else {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
    }

    public function actionSaveResponse() {
        $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
        if ($competition_user_id == 0) {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }

        $competitionUser = CompetitionUser::model()->findByPk($competition_user_id);
        if ($competitionUser != null) {
            if ($competitionUser == null) {
                $competitionUser = new CompetitionUser();
            }
            if ($competitionUser->finished == 1 || $competitionUser->finish_time != null) {
                self::reponseJSON(array('success' => false, 'errorCode' => 999, 'error' => Yii::t('app', 'You already finished competition. You cannot save answer anymore.')));
            }
            if ($competitionUser->start_time != null) {
                $duration = $competitionUser->competition->duration * 60;
                $starttime = strtotime($competitionUser->start_time);
                $endtime = $starttime + $duration;
                if ($endtime < time()) {
                    self::reponseJSON(array('success' => false, 'errorCode' => 999, 'error' => Yii::t('app', 'Time is up. Answer cannot be saved!')));
                }
            } else {
                self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User did not authenticate competition!')));
            }
        } else {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }

        $question_id = Yii::app()->getRequest()->getPost('q', 0);
        if ($question_id == 0) {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'Empty Question ID!')));
        }

        $answer = Yii::app()->getRequest()->getPost('a', '');

        $competition_user_question = CompetitionUserQuestion::model()->with('competitionQuestion')->find('competitionQuestion.question_id=:question_id and t.competition_user_id=:competition_user_id', array(':question_id' => $question_id, ':competition_user_id' => $competition_user_id));
        if ($competition_user_question != null) {
            if ($competition_user_question->custom_answer != $answer) {
                $competition_user_question->custom_answer = $answer;
                $competition_user_question->last_change = date('Y-m-d H:i:s');
                if ($competition_user_question->save(true, array('custom_answer', 'last_change'))) {
                    self::reponseJSON(array('success' => true));
                } else {
                    self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'Error saving question answer!')));
                }
            } else {
                self::reponseJSON(array('success' => true, 'same_in_db' => true, 'error' => Yii::t('app', 'Nothing changed!')));
            }
        } else {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'You submited answer for question you don\'t have!')));
        }
    }

    public function actionFinishCompetition() {
        $competition_user_id = isset(Yii::app()->session['competition_user_id']) ? Yii::app()->session['competition_user_id'] : 0;
        // demo
        if ($competition_user_id == 0) {
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
        $competitionUser = CompetitionUser::model()->findByPk($competition_user_id);
        if ($competitionUser != null) {
            if ($competitionUser == null) {
                $competitionUser = new CompetitionUser();
            }
            if ($competitionUser->start_time == null) {
                self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'You cannot finish competition that was never started.')));
            } else {
                if ($competitionUser->finished == 0) {
                    $competitionUser->finished = 1;
                    $duration = $competitionUser->competition->duration * 60;
                    $starttime = strtotime($competitionUser->start_time);
                    $endtime = $starttime + $duration;
                    if ($endtime < time()) {
                        $competitionUser->finish_time = date('Y-m-d H:i:s', $endtime);
                    } else {
                        $competitionUser->finish_time = date('Y-m-d H:i:s');
                    }
                    $competitionUser->ip_stop = isset($_SERVER) && isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '/';
                    if ($competitionUser->save(true, array('finished', 'finish_time', 'ip_stop'))) {
                        unset(Yii::app()->session['competition_user_id']);
                        self::reponseJSON(array('success' => true));
                    } else {
                        self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'Error saving competition finished state!')));
                    }
                } else {
                    unset(Yii::app()->session['competition_user_id']);
                    self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'You have already clicked Finish Competition!')));
                }
            }
        } else {
            unset(Yii::app()->session['competition_user_id']);
            self::reponseJSON(array('success' => false, 'error' => Yii::t('app', 'User is not authenticated.')));
        }
    }

}

?>
