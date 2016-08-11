<?php
/* @var $this CustomerController */
/* @var $model PersonalInfo */

$this->breadcrumbs=array(
	'Customers'=>array('index'),
	'Customer ID (#'.$model->pesonal_info_id.')',
);

$this->menu=array(
	array('label'=>'<i class="icon-pencil"></i> Update Customers', 'url'=>array('update', 'id'=>$model->pesonal_info_id)),
	array('label'=>'<i class="icon-trash"></i> Delete Customer', 'url'=>'#', 'linkOptions'=>array('submit'=>array('delete','id'=>$model->pesonal_info_id),'confirm'=>'Are you sure you want to delete this customer?')),
	array('label'=>'<i class="icon-th-list"></i> List Customers', 'url'=>array('index')),
	array('label'=>'<i class="icon-plus-sign"></i> Create Customers', 'url'=>array('create')),
	array('label'=>'<i class="icon-edit"></i> Manage Customers', 'url'=>array('admin')),
);
?>
<div class="page-header">
	<h1>View Customer ID (#<?php echo $model->pesonal_info_id; ?>)</h1>
</div>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data'=>$model,
	'htmlOptions'=>array('class'=>'table table-striped table-bordered table-hover'),
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
