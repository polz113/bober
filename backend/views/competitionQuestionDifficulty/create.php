<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $model CompetitionQuestionDifficulty */

$this->breadcrumbs = array(
	Yii::t('app', 'Question Difficulties') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Question Difficulties'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Question Difficulty'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>