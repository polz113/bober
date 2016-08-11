<?php
/* @var $this SchoolController */
/* @var $model School */

$this->breadcrumbs=array(
	Yii::t('app', 'Schools') => array('index'),
	$model->name,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update School'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete School'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Schools'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School'); ?> "<?php echo $model->name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
	
		'name',
		array(
                    'name' => 'school_category_id',
                    'value' => $model->schoolCategory->name,
                ),
                array(
                    'name' => 'level_of_education',
                    'value' => $model->GetLevelsOfEducationName($model->level_of_education),
                ),
		'address',
		'post',
		'postal_code',
		array(
                    'name' => 'municipality_id',
                    'value' => $model->municipality->name
                ),
		array(
                    'name' => 'region_id',
                    'value' => $model->region->name
                ),
		array(
                    'name' => 'country_id',
                    'value' => $model->country->country
                ),
		'tax_number',
		'identifier',
		'headmaster',
	),
)); ?>
