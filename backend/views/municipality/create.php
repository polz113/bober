<?php
/* @var $this MunicipalityController */
/* @var $model Municipality */

$this->breadcrumbs = array(
	Yii::t('app', 'Municipalities') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Municipalities'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Municipality'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>