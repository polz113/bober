<?php
$this->breadcrumbs=array(
	'Personal Infos'=>array('index'),
	$model->pesonal_info_id,
);

$this->menu=array(
	array('label'=>'List PersonalInfo','url'=>array('index')),
	array('label'=>'Create PersonalInfo','url'=>array('create')),
	array('label'=>'Update PersonalInfo','url'=>array('update','id'=>$model->pesonal_info_id)),
	array('label'=>'Delete PersonalInfo','url'=>'#','linkOptions'=>array('submit'=>array('delete','id'=>$model->pesonal_info_id),'confirm'=>'Are you sure you want to delete this item?')),
	array('label'=>'Manage PersonalInfo','url'=>array('admin')),
);
?>

<h1>View PersonalInfo #<?php echo $model->pesonal_info_id; ?></h1>

<?php $this->widget('bootstrap.widgets.TbDetailView',array(
	'data'=>$model,
	'attributes'=>array(
		'pesonal_info_id',
		'custom_id',
		'first_name',
		'last_name',
		'phone_home',
		'phone_work',
		'phone_mobile',
		'fax',
		'email_primary',
		'email_secondary',
		'address_1',
		'address_2',
		'address_3',
		'country',
		'gender',
		'marital_status',
		'dob',
		'date_joined',
		'date_left',
		'middle_name',
		'national_id',
		'passport_number',
		'drivers_license',
		'other_id',
		'other_id_2',
		'nationality',
		'ethnic_race',
		'smoker',
		'status',
	),
)); ?>
