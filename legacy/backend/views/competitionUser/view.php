<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */

$this->breadcrumbs = array(
    Yii::t('app', 'Competition Users') => array('index'),
    $model->id,
);

$user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
$superuser = $user != null ? $user->superuser : 0;
$create_competition_user = false;
$delete_competition_user = false;
if ($superuser == 1) {
    $create_competition_user = true;
    $delete_competition_user = true;
}

$this->menu = array(
    array('label' => Yii::t('app', 'Create Competition User'), 'url' => array('create'), 'visible' => $create_competition_user),
    array('label' => Yii::t('app', 'Update Competition User'), 'url' => array('update', 'id' => $model->id)),
    array('label' => Yii::t('app', 'Delete Competition User'), 'url' => '#', 'visible' => $delete_competition_user, 'linkOptions' => array('submit' => array('delete', 'id' => $model->id), 'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label' => Yii::t('app', 'Manage Competition Users'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition User'); ?> "<?php echo $model->id; ?>"</h1>

<?php
$this->widget('zii.widgets.CDetailView', array(
    'data' => $model,
    'attributes' => array(
        'id',
        array(
            'name' => 'competition_id',
            'value' => $model->competition->name,
        ),
        array(
            'name' => 'competition_category_id',
            'value' => $model->competitionCategory->name,
        ),
        array(
            'name' => 'competition_category_school_mentor_id',
            'value' => $model->competitionCategorySchoolMentor->user->profile->last_name . ' ' . $model->competitionCategorySchoolMentor->user->profile->first_name,
        ),
        'last_name',
        'first_name',
        array(
            'name' => 'gender',
            'value' => $model->gender == 0 ? Yii::t('app', 'Male') : Yii::t('app', 'Female'),
        ),
        'class',
        array(
            'name' => 'school_id',
            'value' => $model->school->name,
        ),
        array(
            'name' => 'disqualified_request',
            'value' => $model->disqualified_request == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'),
        ),
        'disqualified_reason',
        array(
            'name' => 'disqualified_request_by',
            'value' => $model->disqualified_request_by != null ? $model->disqualifiedRequestBy->profile->last_name . ' ' . $model->disqualifiedRequestBy->profile->first_name : '/',
        ),
        array(
            'name' => 'disqualified',
            'value' => $model->disqualified == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'),
        ),
        array(
            'name' => 'disqualified_by',
            'value' => $model->disqualified_by != null ? $model->disqualifiedBy->profile->last_name . ' ' . $model->disqualifiedBy->profile->first_name : '/',
        ),
        array(
            'name' => 'start_time',
            'value' => date('j. n. Y H:i:s', strtotime($model->start_time)),
        ),
        array(
            'name' => 'finish_time',
            'value' => date('j. n. Y H:i:s', strtotime($model->finish_time)),
        ),
        array(
            'name' => 'finished',
            'value' => $model->finished == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'),
        ),
        array(
            'name' => 'competition_results',
            'value' => $model->getCompetitionResults(),
            'visible' => CompetitionUser::canShowCompetitionResults($model->competition_id)
        ),
        array(
            'name' => 'award',
            'value' => $model->GetAwardName($model->award),
            'visible' => CompetitionUser::canShowAwardField($model->competition_id)
        ),
        array(
            'name' => 'advancing_to_next_level',
            'value' => $model->advancing_to_next_level == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'),
            'visible' => CompetitionUser::canShowAdvancingToNextLevel($model->competition_id)
        ),
    ),
));
?>
