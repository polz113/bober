<?php
/* @var $this RegionController */
/* @var $model Region */

$this->breadcrumbs = array(
	Yii::t('app', 'Regions') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Region'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Region'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Regions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Region'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>