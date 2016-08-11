<?php
/* @var $this QuestionController */
/* @var $model Question */
/* @var $form CActiveForm */
?>

<div class="form">

<?php 
$formid = 'question-form';

if (isset($ajaxRendering) && $ajaxRendering)
{
    $formid .= 'ajax';
}    

$form=$this->beginWidget('CActiveForm', array(
	'id'=>'$formid',
	'enableAjaxValidation'=>false,
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    	<p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>
    
	<?php echo $form->errorSummary($model); ?>

	<div class="row">
		<?php echo $form->labelEx($model,'country_id'); ?>
		<?php $data = Country::model()->GetCountriesICanEdit();
                      echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));  ?>
		<?php echo $form->error($model, 'country_id'); ?>
	</div>
        
        <div class="row">
		<?php echo $form->labelEx($model,'identifier'); ?>
		<?php echo $form->textField($model,'identifier',array('size'=>60,'maxlength'=>255)); ?>
		<?php echo $form->error($model, 'identifier'); ?>
	</div>
    
	<div class="row">
		<?php echo $form->labelEx($model,'type'); ?>
                <?php echo CHtml::dropDownList('Question[type]', $model->type, $model->GetQuestionType());  ?>
		<?php echo $form->error($model, 'type'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'title'); ?>
		<?php echo $form->textField($model,'title',array('size'=>60,'maxlength'=>255)); ?>
		<?php echo $form->error($model, 'title'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'text'); ?>
		<?php echo $form->textArea($model,'text',array('rows'=>6, 'cols'=>50)); ?>
		<?php echo $form->error($model, 'text'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'data'); ?>
		<?php echo $form->textArea($model,'data',array('rows'=>6, 'cols'=>50)); ?>
		<?php echo $form->error($model, 'data'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'version'); ?>
		<?php echo $form->textField($model,'version',array('size'=>60,'maxlength'=>255)); ?>
		<?php echo $form->error($model, 'version'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'verification_function_type'); ?>
		<?php echo CHtml::dropDownList('Question[verification_function_type]', $model->verification_function_type, $model->GetVerificationFunctionType()); ?>
		<?php echo $form->error($model, 'verification_function_type'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'verification_function'); ?>
		<?php echo $form->textArea($model,'verification_function',array('rows'=>6, 'cols'=>50)); ?>
		<?php echo $form->error($model, 'verification_function'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'authors'); ?>
		<?php echo $form->textArea($model,'authors',array('rows'=>6, 'cols'=>50)); ?>
		<?php echo $form->error($model, 'authors'); ?>
	</div>
        
        <div class="row">
		<?php echo $form->labelEx($model,'css'); ?>
		<?php echo $form->textArea($model,'css',array('rows'=>6, 'cols'=>50)); ?>
		<?php echo $form->error($model, 'css'); ?>
	</div>

    
    <div class="row buttons">
		<br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord ? Yii::t('app', 'create') : Yii::t('app', 'save'),
            'value' => $model->isNewRecord ? Yii::t('app', 'create') : Yii::t('app', 'save')
        ));
        ?>	</div>
    
<?php $this->endWidget(); ?>

</div><!-- form -->