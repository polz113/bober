<?php
/* @var $this SchoolController */
/* @var $model School */

$this->breadcrumbs = array(
	Yii::t('app', 'Schools') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View School'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Schools'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update School'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>