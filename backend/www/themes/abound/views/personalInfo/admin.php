<?php
$this->breadcrumbs=array(
	'Personal Infos'=>array('index'),
	'Manage',
);

$this->menu=array(
	array('label'=>'List PersonalInfo','url'=>array('index')),
	array('label'=>'Create PersonalInfo','url'=>array('create')),
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

<h1>Manage Personal Infos</h1>

<p>
You may optionally enter a comparison operator (<b>&lt;</b>, <b>&lt;=</b>, <b>&gt;</b>, <b>&gt;=</b>, <b>&lt;&gt;</b>
or <b>=</b>) at the beginning of each of your search values to specify how the comparison should be done.
</p>

<?php echo CHtml::link('Advanced Search','#',array('class'=>'search-button btn')); ?>
<div class="search-form" style="display:none">
<?php $this->renderPartial('_search',array(
	'model'=>$model,
)); ?>
</div><!-- search-form -->

<?php $this->widget('bootstrap.widgets.TbGridView',array(
	'id'=>'personal-info-grid',
	'dataProvider'=>$model->search(),
	'filter'=>$model,
	'columns'=>array(
		'pesonal_info_id',
		'custom_id',
		'first_name',
		'last_name',
		'phone_home',
		'phone_work',
		/*
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
			'class'=>'bootstrap.widgets.TbButtonColumn',
		),
	),
)); ?>
