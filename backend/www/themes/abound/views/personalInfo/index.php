<?php
$this->breadcrumbs=array(
	'Personal Infos',
);

$this->menu=array(
	array('label'=>'Create PersonalInfo','url'=>array('create')),
	array('label'=>'Manage PersonalInfo','url'=>array('admin')),
);
?>

<h1>Personal Info</h1>

<ul class="thumbnails clearfix">
  <?php $this->widget('bootstrap.widgets.TbListView',array(
	'dataProvider'=>$dataProvider,
	'itemView'=>'_view',
)); ?>

</ul>


