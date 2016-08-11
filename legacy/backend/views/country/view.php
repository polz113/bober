<?php
/* @var $this CountryController */
/* @var $model Country */

$this->breadcrumbs=array(
	Yii::t('app', 'Countries') => array('index'),
	$model->country,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Country'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Country'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Country'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Countries'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Country'); ?> "<?php echo $model->country; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		'country',
	),
)); ?>
