<?php
/* @var $this CustomerController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs=array(
	'Customers',
);

$this->menu=array(
	array('label'=>'<i class="icon-plus-sign"></i> Create Customer', 'url'=>array('create')),
	array('label'=>'<i class="icon-edit"></i> Manage Customers', 'url'=>array('admin')),
);
?>

<div class="page-header">
	<h1>List Customers</h1>
</div>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider'=>$dataProvider,
	'itemsCssClass'=>'',
	'itemView'=>'_view',
	'sortableAttributes'=>array(
        'first_name'=>'First Name',
        'last_name'=>'Last Name',
    ),
)); ?>
