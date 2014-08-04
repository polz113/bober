<?php
/* @var $this QuestionController */
/* @var $model Question */

$this->breadcrumbs = array(
	Yii::t('app', 'Questions') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Import Question'); ?></h1>

<?php echo $this->renderPartial('_form_import', array('model' => $model)); ?>