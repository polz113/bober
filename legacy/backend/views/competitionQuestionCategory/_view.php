<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $data CompetitionQuestionCategory */
?>

<div class="view">

	<b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_question_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_question_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competition_category_id')); ?>:</b>
	<?php echo CHtml::encode($data->competition_category_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('competiton_question_difficulty_id')); ?>:</b>
	<?php echo CHtml::encode($data->competiton_question_difficulty_id); ?>
	<br />


</div>