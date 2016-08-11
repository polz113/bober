<?php
/* @var $this CompetitionCategoryController */
/* @var $data CompetitionCategory */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('active')); ?>:</b>
	<?php echo CHtml::encode($data->active); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('name')); ?>:</b>
	<?php echo CHtml::encode($data->name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('level_of_education')); ?>:</b>
	<?php echo CHtml::encode($data->level_of_education); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('class_from')); ?>:</b>
	<?php echo CHtml::encode($data->class_from); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('class_to')); ?>:</b>
	<?php echo CHtml::encode($data->class_to); ?>
	<br />


</div>