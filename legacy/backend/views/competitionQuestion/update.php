<?php
/* @var $this CompetitionQuestionController */
/* @var $model CompetitionQuestion */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Questions') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Question'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Competition Question'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Competition Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competition Question'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>