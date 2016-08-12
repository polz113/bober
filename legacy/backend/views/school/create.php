<?php
/* @var $this SchoolController */
/* @var $model School */

$this->breadcrumbs = array(
	Yii::t('app', 'Schools') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage Schools'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create School'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>