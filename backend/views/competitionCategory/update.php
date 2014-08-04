<?php
/* @var $this CompetitionCategoryController */
/* @var $model CompetitionCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Categories') => array('index'),
	$model->name => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Competition Category'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Competition Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competition Category'); ?> "<?php echo $model->name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>