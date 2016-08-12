<?php
$this->breadcrumbs=array(
	'Personal Infos'=>array('index'),
	$model->pesonal_info_id=>array('view','id'=>$model->pesonal_info_id),
	'Update',
);

$this->menu=array(
	array('label'=>'List PersonalInfo','url'=>array('index')),
	array('label'=>'Create PersonalInfo','url'=>array('create')),
	array('label'=>'View PersonalInfo','url'=>array('view','id'=>$model->pesonal_info_id)),
	array('label'=>'Manage PersonalInfo','url'=>array('admin')),
);
?>

<h1>Update PersonalInfo <?php echo $model->pesonal_info_id; ?></h1>

<?php echo $this->renderPartial('_form',array('model'=>$model)); ?>