<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */

$this->breadcrumbs = array(
	Yii::t('app', 'Register School For Competition') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'All School Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Register School'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>