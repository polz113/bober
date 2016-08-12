<?php
/* @var $this CompetitionController */
/* @var $model Competition */

$this->breadcrumbs = array(
	Yii::t('app', 'Competitions') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Competition'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Competitions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competition'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>