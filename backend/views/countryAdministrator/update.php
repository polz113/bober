<?php
/* @var $this CountryAdministratorController */
/* @var $model CountryAdministrator */

$this->breadcrumbs = array(
	Yii::t('app', 'Country Administrators') => array('index'),
	$model->country->country => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Country Administrator'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View Country Administrator'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Country Administrators'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Country Administrator'); ?> "<?php echo $model->user->profile->last_name . ' ' . $model->user->profile->first_name; ?>"</h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>