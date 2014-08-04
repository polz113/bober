<?php
/* @var $this CustomerController */
/* @var $model PersonalInfo */

$this->breadcrumbs=array(
	'Customers'=>array('index'),
	'Manage Customers',
);

$this->menu=array(
	array('label'=>'<i class="icon-th-list"></i>  List Customers', 'url'=>array('index')),
	array('label'=>'<i class="icon-plus-sign"></i> Create Customer', 'url'=>array('create')),
);

Yii::app()->clientScript->registerScript('search', "
$('.search-button').click(function(){
	$('.search-form').toggle();
	return false;
});
$('.search-form form').submit(function(){
	$.fn.yiiGridView.update('personal-info-grid', {
		data: $(this).serialize()
	});
	return false;
});
");
?>

<div class="page-header">
	<h1>Manage Customers</h1>
</div>

<p>
You may optionally enter a comparison operator (<b>&lt;</b>, <b>&lt;=</b>, <b>&gt;</b>, <b>&gt;=</b>, <b>&lt;&gt;</b>
or <b>=</b>) at the beginning of each of your search values to specify how the comparison should be done.
</p>

<?php echo CHtml::link('Advanced Search','#',array('class'=>'search-button')); ?>
<div class="search-form" style="display:none">
<?php $this->renderPartial('_search',array(
	'model'=>$model,
)); ?>
</div><!-- search-form -->

<?php $this->widget('zii.widgets.grid.CGridView', array(
	'id'=>'personal-info-grid',
	'itemsCssClass'=>'table table-striped table-bordered table-hover',
	'dataProvider'=>$model->search(),
	'filter'=>$model,
	'columns'=>array(
		
		'first_name',
		'last_name',
		
		
		'status',
		/*
		'dob',
		'gender',
		'nationality',
		'ethnic_race',
		'phone_home',
		'phone_work',
		'pesonal_info_id',
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
		*/
		array(
			'class'=>'CButtonColumn',
		),
	),
)); ?>
