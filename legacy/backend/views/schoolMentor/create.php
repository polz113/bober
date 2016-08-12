<?php
/* @var $this SchoolMentorController */
/* @var $model SchoolMentor */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentors') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage School Mentors'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create School Mentor'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>