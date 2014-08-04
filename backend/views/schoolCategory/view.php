<?php
/* @var $this SchoolCategoryController */
/* @var $model SchoolCategory */

$this->breadcrumbs=array(
	Yii::t('app', 'School Categories') => array('index'),
	$model->name,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update School Category'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete School Category'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage School Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Category'); ?> "<?php echo $model->name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		'id',
		'name',
		'active',
	),
)); ?>
