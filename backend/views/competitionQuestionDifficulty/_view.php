<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $data CompetitionQuestionDifficulty */
?>

<div class="view">

	

	<b><?php echo CHtml::encode($data->getAttributeLabel('active')); ?>:</b>
	<?php echo $data->active == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no'); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('name')); ?>:</b>
	<?php echo CHtml::encode($data->name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('correct_answer_points')); ?>:</b>
	<?php echo CHtml::encode($data->correct_answer_points); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('wrong_answer_points')); ?>:</b>
	<?php echo CHtml::encode($data->wrong_answer_points); ?>
	<br />


</div>