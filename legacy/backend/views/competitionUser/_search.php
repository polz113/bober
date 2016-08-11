<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
	<div class="row">
		<?php echo $form->label($model, 'id'); ?>
		<?php echo $form->textField($model,'id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competition_id'); ?>
		<?php echo $form->textField($model,'competition_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competition_category_id'); ?>
		<?php echo $form->textField($model,'competition_category_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'user_id'); ?>
		<?php echo $form->textField($model,'user_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competition_category_school_mentor_id'); ?>
		<?php echo $form->textField($model,'competition_category_school_mentor_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'last_name'); ?>
		<?php echo $form->textField($model,'last_name',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'first_name'); ?>
		<?php echo $form->textField($model,'first_name',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'class'); ?>
		<?php echo $form->textField($model,'class',array('size'=>20,'maxlength'=>20)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'school_id'); ?>
		<?php echo $form->textField($model,'school_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'disqualified_request'); ?>
		<?php echo $form->textField($model,'disqualified_request'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'disqualified_request_by'); ?>
		<?php echo $form->textField($model,'disqualified_request_by'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'disqualified'); ?>
		<?php echo $form->textField($model,'disqualified'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'disqualified_by'); ?>
		<?php echo $form->textField($model,'disqualified_by'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'disqualified_reason'); ?>
		<?php echo $form->textArea($model,'disqualified_reason',array('rows'=>6, 'cols'=>50)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'advancing_to_next_level'); ?>
		<?php echo $form->textField($model,'advancing_to_next_level'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'award'); ?>
		<?php echo $form->textField($model,'award'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'start_time'); ?>
		<?php echo $form->textField($model,'start_time'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'finish_time'); ?>
		<?php echo $form->textField($model,'finish_time'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'finished'); ?>
		<?php echo $form->textField($model,'finished'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'total_points_via_answers'); ?>
		<?php echo $form->textField($model,'total_points_via_answers',array('size'=>10,'maxlength'=>10)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'total_points_via_time'); ?>
		<?php echo $form->textField($model,'total_points_via_time',array('size'=>10,'maxlength'=>10)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'total_points_manual'); ?>
		<?php echo $form->textField($model,'total_points_manual',array('size'=>10,'maxlength'=>10)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'total_points'); ?>
		<?php echo $form->textField($model,'total_points',array('size'=>10,'maxlength'=>10)); ?>
	</div>

	<div class="row buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => Yii::t('app', 'search'),
            'value' => Yii::t('app', 'search')
        ));
        ?>	</div>

<?php $this->endWidget(); ?>

</div><!-- search-form -->