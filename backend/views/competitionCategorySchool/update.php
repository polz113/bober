<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */

$this->breadcrumbs = array(
	Yii::t('app', 'Register School For Competition') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Register School'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Registration'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'All School Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Registration'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>