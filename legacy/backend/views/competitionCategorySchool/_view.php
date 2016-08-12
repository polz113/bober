<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $data CompetitionCategorySchool */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_category_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_category_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('school_id')); ?>:</b>
	<?php echo CHtml::encode($data->school_id); ?>
	<br />


</div>