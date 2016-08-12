<?php
/* @var $this CustomerController */
/* @var $model PersonalInfo */

$this->breadcrumbs=array(
	'Customers'=>array('index'),
	'Customer ID (#'.$model->pesonal_info_id.')'=>array('view','id'=>$model->pesonal_info_id),
	'Update',
);

$this->menu=array(
	array('label'=>'<i class="icon-th-list"></i> List Customers', 'url'=>array('index')),
	array('label'=>'<i class="icon-plus-sign"></i> Create Customer', 'url'=>array('create')),
	array('label'=>'<i class="icon-user"></i> View Customer', 'url'=>array('view', 'id'=>$model->pesonal_info_id)),
	array('label'=>'<i class="icon-edit"></i> Manage Customers', 'url'=>array('admin')),
);
?>
<div class="page-header">
	<h1>Update Customer ID (#<?php echo $model->pesonal_info_id; ?>)</h1>
</div>

<?php echo $this->renderPartial('_form', array('model'=>$model)); ?>