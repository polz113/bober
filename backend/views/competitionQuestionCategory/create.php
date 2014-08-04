<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $model CompetitionQuestionCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Question Categories') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Competition Question Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Competition Question Category'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>