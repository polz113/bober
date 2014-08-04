<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $model CompetitionCategorySchoolMentor */

$this->breadcrumbs=array(
	Yii::t('app', 'Register Competitors For Competition') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Register Competitors'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Competitors Registration'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Competitors Registration'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'All Competitors Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competitors Registration'); ?> "<?php echo $model->competitionCategorySchool->competition->name . ' - ' . $model->competitionCategorySchool->school->name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		
		array(
                    'name' => 'competition_category_school_id',
                    'value' => $model->competitionCategorySchool->competition->name . ' - ' . $model->competitionCategorySchool->school->name,
                ),
		'user_id',
		'access_code',
		'disqualified',
		'disqualified_by',
		'disqualified_reason',
	),
)); ?>
