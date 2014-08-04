<?php
/* @var $this MunicipalityController */
/* @var $model Municipality */

$this->breadcrumbs = array(
	Yii::t('app', 'Municipalities') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Municipality'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Municipality'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Municipalities'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Municipality'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>