<?php
/* @var $this CountryAdministratorController */
/* @var $model CountryAdministrator */

$this->breadcrumbs=array(
	Yii::t('app', 'Country Administrators') => array('index'),
	$model->user->profile->last_name . ' ' . $model->user->profile->first_name,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Country Administrator'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Country Administrator'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Country Administrator'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Country Administrators'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Country Administrator'); ?> "<?php echo $model->user->profile->last_name . ' ' . $model->user->profile->first_name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		
		 array(
                    'name' => 'country_id',
                    'value' => $model->country->country
                ),
		array(
                    'name' => 'user_id',
                    'value' => $model->user->profile->last_name .' '. $model->user->profile->first_name
                )
	),
)); ?>
