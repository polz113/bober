<?php
/* @var $this CountryController */
/* @var $model Country */

$this->breadcrumbs = array(
	Yii::t('app', 'Countries') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Countries'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Country'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>