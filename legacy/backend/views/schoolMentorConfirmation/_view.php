<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $data SchoolMentorConfirmation */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('school_id')); ?>:</b>
	<?php echo CHtml::encode($data->school_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('user_id')); ?>:</b>
	<?php echo CHtml::encode($data->user_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('active')); ?>:</b>
	<?php echo CHtml::encode($data->active); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('activated_by')); ?>:</b>
	<?php echo CHtml::encode($data->activated_by); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('activated_timestamp')); ?>:</b>
	<?php echo CHtml::encode($data->activated_timestamp); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('coordinator')); ?>:</b>
	<?php echo CHtml::encode($data->coordinator); ?>
	<br />


</div>