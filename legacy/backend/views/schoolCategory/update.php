<?php
/* @var $this SchoolCategoryController */
/* @var $model SchoolCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'School Categories') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View School Category'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage School Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update School Category'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>