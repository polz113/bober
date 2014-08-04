<?php
/* @var $this CompetitionCategoryController */
/* @var $model CompetitionCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Categories') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Competition Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Competition Category'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>