<?php
/* @var $this QuestionController */
/* @var $model Question */

$this->breadcrumbs = array(
	Yii::t('app', 'Questions') => array('index'),
	$model->title => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Question'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Question'); ?> "<?php echo $model->title; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>