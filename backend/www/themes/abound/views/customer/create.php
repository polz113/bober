<?php
/* @var $this CustomerController */
/* @var $model PersonalInfo */

$this->breadcrumbs=array(
	'Customers'=>array('index'),
	'Create Customer',
);

$this->menu=array(
	array('label'=>'<i class="icon-th-list"></i> List Customers', 'url'=>array('index')),
	array('label'=>'<i class="icon-edit"></i> Manage Customers', 'url'=>array('admin')),
);
?>
<div class="page-header">
	<h1>Create Customer</h1>
</div>

<?php echo $this->renderPartial('_form', array('model'=>$model)); ?>