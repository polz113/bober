<?php
/* @var $this CompetitionQuestionController */
/* @var $model CompetitionQuestion */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Questions') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Competition Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Competition Question'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>