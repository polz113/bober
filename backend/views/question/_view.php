<?php
/* @var $this QuestionController */
/* @var $data Question */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('country_id')); ?>:</b>
	<?php echo CHtml::encode($data->country_id); ?>
	<br />

        <b><?php echo CHtml::encode($data->getAttributeLabel('identifier')); ?>:</b>
	<?php echo CHtml::encode($data->identifier); ?>
	<br />
        
	<b><?php echo CHtml::encode($data->getAttributeLabel('type')); ?>:</b>
	<?php echo CHtml::encode($data->type); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('title')); ?>:</b>
	<?php echo CHtml::encode($data->title); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('text')); ?>:</b>
	<?php echo CHtml::encode($data->text); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('data')); ?>:</b>
	<?php echo CHtml::encode($data->data); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('version')); ?>:</b>
	<?php echo CHtml::encode($data->version); ?>
	<br />

	<?php /*
	<b><?php echo CHtml::encode($data->getAttributeLabel('verification_function_type')); ?>:</b>
	<?php echo CHtml::encode($data->verification_function_type); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('verification_function')); ?>:</b>
	<?php echo CHtml::encode($data->verification_function); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('last_change_date')); ?>:</b>
	<?php echo CHtml::encode($data->last_change_date); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('authors')); ?>:</b>
	<?php echo CHtml::encode($data->authors); ?>
	<br />

	*/ ?>

</div>