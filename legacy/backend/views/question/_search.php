<?php
/* @var $this QuestionController */
/* @var $model Question */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
	

	<div class="row">
		<?php echo $form->label($model, 'country_id'); ?>
		<?php echo $form->textField($model,'country_id'); ?>
	</div>
    
        <div class="row">
		<?php echo $form->label($model, 'identifier'); ?>
		<?php echo $form->textField($model,'identifier',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'type'); ?>
		<?php echo $form->textField($model,'type'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'title'); ?>
		<?php echo $form->textField($model,'title',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'text'); ?>
		<?php echo $form->textArea($model,'text',array('rows'=>6, 'cols'=>50)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'data'); ?>
		<?php echo $form->textArea($model,'data',array('rows'=>6, 'cols'=>50)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'version'); ?>
		<?php echo $form->textField($model,'version',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'verification_function_type'); ?>
		<?php echo $form->textField($model,'verification_function_type'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'verification_function'); ?>
		<?php echo $form->textArea($model,'verification_function',array('rows'=>6, 'cols'=>50)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'last_change_date'); ?>
		<?php echo $form->textField($model,'last_change_date'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'authors'); ?>
		<?php echo $form->textArea($model,'authors',array('rows'=>6, 'cols'=>50)); ?>
	</div>
    
        <div class="row">
		<?php echo $form->label($model, 'css'); ?>
		<?php echo $form->textArea($model,'css',array('rows'=>6, 'cols'=>50)); ?>
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