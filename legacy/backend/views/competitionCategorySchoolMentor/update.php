<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $model CompetitionCategorySchoolMentor */

$this->breadcrumbs = array(
	Yii::t('app', 'Register Competitors For Competition') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Register Competitors'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Competitors Registration'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'All Competitors Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competitors Registration'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>