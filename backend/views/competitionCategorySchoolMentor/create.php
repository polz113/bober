<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $model CompetitionCategorySchoolMentor */

$this->breadcrumbs = array(
	Yii::t('app', 'Register Competitors For Competition') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'All Competitors Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Register Competitors'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>