<?php
/* @var $this SchoolMentorController */
/* @var $model SchoolMentor */

$this->breadcrumbs = array(
    Yii::t('app', 'School Mentors') => array('index'),
    $model->id,
);

$this->menu = array(
    array('label' => Yii::t('app', 'Create School Mentor'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Update School Mentor'), 'url' => array('update', 'id' => $model->id)),
    array('label' => Yii::t('app', 'Delete School Mentor'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id), 'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label' => Yii::t('app', 'Manage School Mentors'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Mentor'); ?> "<?php echo $model->id; ?>"</h1>

<?php
$this->widget('zii.widgets.CDetailView', array(
    'data' => $model,
    'attributes' => array(
        'id',
        array(
            'name' => 'school_id',
            'value' => $model->school->name,
        ),
        array(
            'name' => 'user_id',
            'value' => $model->user->profile->last_name . ' ' . $model->user->profile->first_name,
        ),
        array(
            'name' => 'active',
            'value' => $model->active == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no')
        ),
        array(
            'name' => 'activated_by',
            'value' => $model->activatedBy != null ? $model->activatedBy->profile->last_name . ' ' . $model->activatedBy->profile->first_name : '/',
        ),
        array(
            'name' => 'activated_timestamp',
            'value' => date('j. n. Y H:i:s', strtotime($model->activated_timestamp)),
        ),
        array(
            'name' => 'coordinator',
            'value' => $model->coordinator == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no')
        ),
    ),
));
?>
