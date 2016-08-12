<?php
/* @var $this CountryController */
/* @var $model Country */

$this->breadcrumbs = array(
	Yii::t('app', 'Countries') => array('index'),
	$model->country => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Country'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Country'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Countries'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Country'); ?> "<?php echo $model->country; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>