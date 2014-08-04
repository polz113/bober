<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */

$this->breadcrumbs=array(
	Yii::t('app', 'Register School For Competition') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Register School'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Registration'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Registration'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'All School Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Registration'); ?> "<?php echo $model->id; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		
		 array(
                    'name' => 'competition_id',
                    'value' => $model->competition->name
                ),
		array(
                    'name' => 'competition_category_id',
                    'value' => $model->competitionCategory->name
                ),
		array(
                    'name' => 'school_id',
                    'value' => $model->school->name
                ),
	),
)); ?>
