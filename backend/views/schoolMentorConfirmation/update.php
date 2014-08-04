<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $model SchoolMentorConfirmation */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentor Confirmations') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School Mentor Confirmation'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View School Mentor Confirmation'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage School Mentor Confirmations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update School Mentor Confirmation'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>