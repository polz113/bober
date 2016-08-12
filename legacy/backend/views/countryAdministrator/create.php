<?php
/* @var $this CountryAdministratorController */
/* @var $model CountryAdministrator */

$this->breadcrumbs = array(
	Yii::t('app', 'Country Administrators') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Country Administrators'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Country Administrator'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>