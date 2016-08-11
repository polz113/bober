<?php
/* @var $this CompetitionCategoryController */
/* @var $model CompetitionCategory */

$this->breadcrumbs=array(
	Yii::t('app', 'Competition Categories') => array('index'),
	$model->name,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Competition Category'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Competition Category'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Competition Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Category'); ?> "<?php echo $model->name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
                array(
                    'name' => 'active',
                    'value' => $model->active == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no')
                ),
		'name',
                array(
                    'name' => 'level_of_education',
                    'value' => $model->GetLevelsOfEducationName($model->level_of_education)
                ),
		'class_from',
		'class_to',
                 array(
                    'name' => 'country_id',
                    'value' => $model->country->country
                ),
	),
)); ?>
