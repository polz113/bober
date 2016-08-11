<?php
/* @var $this CompetitionUserController */
/* @var $data CompetitionUser */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition->name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_category_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_category_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('user_id')); ?>:</b>
	<?php echo CHtml::encode($data->user_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_category_school_mentor_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_category_school_mentor_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('last_name')); ?>:</b>
	<?php echo CHtml::encode($data->last_name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('first_name')); ?>:</b>
	<?php echo CHtml::encode($data->first_name); ?>
	<br />

	<?php /*
	<b><?php echo CHtml::encode($data->getAttributeLabel('class')); ?>:</b>
	<?php echo CHtml::encode($data->class); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('school_id')); ?>:</b>
	<?php echo CHtml::encode($data->school_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('disqualified_request')); ?>:</b>
	<?php echo CHtml::encode($data->disqualified_request); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('disqualified_request_by')); ?>:</b>
	<?php echo CHtml::encode($data->disqualified_request_by); ?>
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

	<b><?php echo CHtml::encode($data->getAttributeLabel('advancing_to_next_level')); ?>:</b>
	<?php echo CHtml::encode($data->advancing_to_next_level); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('award')); ?>:</b>
	<?php echo CHtml::encode($data->award); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('start_time')); ?>:</b>
	<?php echo CHtml::encode($data->start_time); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('finish_time')); ?>:</b>
	<?php echo CHtml::encode($data->finish_time); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('finished')); ?>:</b>
	<?php echo CHtml::encode($data->finished); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('total_points_via_answers')); ?>:</b>
	<?php echo CHtml::encode($data->total_points_via_answers); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('total_points_via_time')); ?>:</b>
	<?php echo CHtml::encode($data->total_points_via_time); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('total_points_manual')); ?>:</b>
	<?php echo CHtml::encode($data->total_points_manual); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('total_points')); ?>:</b>
	<?php echo CHtml::encode($data->total_points); ?>
	<br />

	*/ ?>

</div>