<?php
/* @var $this CompetitionController */
/* @var $model Competition */

$this->breadcrumbs = array(
	Yii::t('app', 'Competitions') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Competitions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Competition'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>