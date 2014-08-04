<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $model CompetitionQuestionDifficulty */

$this->breadcrumbs = array(
	Yii::t('app', 'Question Difficulties') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question Difficulty'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Question Difficulty'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Question Difficulties'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Question Difficulty'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>