<?php
/* @var $this SchoolMentorController */
/* @var $model SchoolMentor */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentors') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School Mentor'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View School Mentor'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage School Mentors'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update School Mentor'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>