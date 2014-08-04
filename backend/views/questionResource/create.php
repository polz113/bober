<?php
/* @var $this QuestionResourceController */
/* @var $model QuestionResource */

$this->breadcrumbs = array(
	Yii::t('app', 'Question Resources') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Question Resources'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create Question Resource'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>