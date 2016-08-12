<?php
/* @var $this CompetitionController */
/* @var $model Competition */

$this->breadcrumbs = array(
    Yii::t('app', 'Competitions') => array('index'),
    $model->name,
);

$this->menu = array(
    array('label' => Yii::t('app', 'Create Competition'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Update Competition'), 'url' => array('update', 'id' => $model->id)),
    array('label' => Yii::t('app', 'Delete Competition'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id), 'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label' => Yii::t('app', 'Manage Competitions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition'); ?> "<?php echo $model->name; ?>"</h1>


<?php
$this->widget('zii.widgets.CDetailView', array(
    'data' => $model,
    'attributes' => array(
        //	'id',
        'name',

        array(
            'name' => 'active',
            'value' => $model->active == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'),
        ),
        array(
            'name' => 'timestamp_start',
            'value' => Yii::app()->localtime->toLocalDateTime($model->timestamp_start, 'medium')
        ),
        array(
            'name' => 'timestamp_stop',
            'value' => Yii::app()->localtime->toLocalDateTime($model->timestamp_stop, 'medium')
        ),
        array(
            'name' => 'type',
            //          'header' => Yii::t('app','type'),
            'value' => $model->GetTypeOfCompetitionName($model->type)
        ),
        array(
            'name' => 'public_access',
            'value' => $model->public_access == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no')
        ),
        'duration',
        array(
            'name' => 'timestamp_mentor_results',
            'value' => $model->timestamp_mentor_results != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_results, 'medium') : null
        ),
        array(
            'name' => 'timestamp_mentor_awards',
            'value' => $model->timestamp_mentor_awards != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_awards, 'medium') : null
        ),
        array(
            'name' => 'timestamp_mentor_advancing_to_next_level',
            'value' => $model->timestamp_mentor_advancing_to_next_level != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_advancing_to_next_level, 'medium') : null
        ),
    ),
));
?>
