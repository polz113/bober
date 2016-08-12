<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $data CompetitionCategorySchoolMentor */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_category_school_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_category_school_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('user_id')); ?>:</b>
	<?php echo CHtml::encode($data->user_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('access_code')); ?>:</b>
	<?php echo CHtml::encode($data->access_code); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('disqualified')); ?>:</b>
	<?php echo CHtml::encode($data->disqualified); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('disqualified_by')); ?>:</b>
	<?php echo CHtml::encode($data->disqualified_by); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('disqualified_reason')); ?>:</b>
	<?php echo CHtml::encode($data->disqualified_reason); ?>
	<br />


</div>