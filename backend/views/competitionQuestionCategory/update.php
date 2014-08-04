<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $model CompetitionQuestionCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Question Categories') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Question Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Competition Question Category'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Competition Question Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competition Question Category'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>