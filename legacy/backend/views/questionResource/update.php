<?php
/* @var $this QuestionResourceController */
/* @var $model QuestionResource */

$this->breadcrumbs = array(
	Yii::t('app', 'Question Resources') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question Resource'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Question Resource'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Question Resources'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Question Resource'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>