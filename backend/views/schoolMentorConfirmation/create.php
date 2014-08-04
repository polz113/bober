<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $model SchoolMentorConfirmation */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentor Confirmations') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage School Mentor Confirmations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create School Mentor Confirmation'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>