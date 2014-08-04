<?php
/* @var $this SchoolCategoryController */
/* @var $model SchoolCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'School Categories') => array('admin'),
	Yii::t('app', 'create'),
);

$this->menu=array(
	array('label' => Yii::t('app', 'Manage School Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Create School Category'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>