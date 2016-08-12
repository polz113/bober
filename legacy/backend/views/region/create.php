<?php
/* @var $this RegionController */
/* @var $model Region */

$this->breadcrumbs = array(
	Yii::t('app', 'Regions') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Regions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Region'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>