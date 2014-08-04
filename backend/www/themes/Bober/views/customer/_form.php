<?php
/* @var $this CustomerController */
/* @var $model PersonalInfo */
/* @var $form CActiveForm */
?>
<?php
	$this->beginWidget('zii.widgets.CPortlet', array(
		'title'=>"Header Tag",
	));
	
?>
<div class="form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'id'=>'personal-info-form',
	'enableAjaxValidation'=>false,
)); ?>

	<p class="note">Fields with <span class="required">*</span> are required.</p>

	<?php echo $form->errorSummary($model); ?>

<div class="row-fluid">
  <div class="span6">
  	
    <div class="row">
		<?php echo $form->labelEx($model,'first_name'); ?>
		<?php echo $form->textField($model,'first_name',array('size'=>40,'maxlength'=>40)); ?>
		<?php echo $form->error($model,'first_name'); ?>
	</div>
    
    <div class="row">
		<?php echo $form->labelEx($model,'middle_name'); ?>
		<?php echo $form->textField($model,'middle_name',array('size'=>40,'maxlength'=>40)); ?>
		<?php echo $form->error($model,'middle_name'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'last_name'); ?>
		<?php echo $form->textField($model,'last_name',array('size'=>40,'maxlength'=>40)); ?>
		<?php echo $form->error($model,'last_name'); ?>
	</div>
    
    <div class="row">
		<?php echo $form->labelEx($model,'dob'); ?>
		<?php echo $form->textField($model,'dob'); ?>
		<?php echo $form->error($model,'dob'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'gender'); ?>
        <?php echo $form->dropDownList($model,'gender',array('Male'=>'Male','Female'=>'Female')); ?>
		<?php echo $form->error($model,'gender'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'marital_status'); ?>
        <?php echo $form->dropDownList($model,'marital_status',array('Single'=>'Single','Married'=>'Married','Divorced'=>'Divorced','Widowed'=>'Widowed')); ?>
		<?php echo $form->error($model,'marital_status'); ?>
	</div>
    
    <div class="row">
		<?php echo $form->labelEx($model,'smoker'); ?>
		<?php echo $form->checkBox($model,'smoker'); ?>
		<?php echo $form->error($model,'smoker'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'status'); ?>
		<?php echo $form->dropDownList($model,'status',array('Active'=>'Active','Inactive'=>'Inactive','Closed'=>'Closed')); ?>
		<?php echo $form->error($model,'status'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'date_joined'); ?>
		<?php echo $form->textField($model,'date_joined',array('disabled'=>'disabled')); ?>
		<?php echo $form->error($model,'date_joined'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'date_left'); ?>
		<?php echo $form->textField($model,'date_left'); ?>
		<?php echo $form->error($model,'date_left'); ?>
	</div>
    
  </div>
  
  <div class="span6">
  	<div class="row input-prepend">
		<?php echo $form->labelEx($model,'phone_home'); ?>
        <span class="add-on">+263</span>
		<?php echo $form->textField($model,'phone_home',array('size'=>30,'maxlength'=>30)); ?>
        <span class="help-inline">Inline help text</span>
		<?php echo $form->error($model,'phone_home'); ?>
	</div>

	<div class="row input-prepend">
		<?php echo $form->labelEx($model,'phone_work'); ?>
        <span class="add-on">+263</span>
		<?php echo $form->textField($model,'phone_work',array('size'=>30,'maxlength'=>30)); ?>
		<?php echo $form->error($model,'phone_work'); ?>
	</div>

	<div class="row input-prepend">
		<?php echo $form->labelEx($model,'phone_mobile'); ?>
        <span class="add-on">+263</span>
		<?php echo $form->textField($model,'phone_mobile',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'phone_mobile'); ?>
	</div>
    
    <div class="row input-prepend">
		<?php echo $form->labelEx($model,'fax'); ?>
        <span class="add-on">+263</span>
		<?php echo $form->textField($model,'fax',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'fax'); ?>
	</div>

	<div class="row input-append">
		<?php echo $form->labelEx($model,'email_primary'); ?>
		<?php echo $form->textField($model,'email_primary',array('size'=>50,'maxlength'=>50)); ?>
        <span class="add-on">@google.com</span>
		<?php echo $form->error($model,'email_primary'); ?>
	</div>

	<div class="row input-append">
		<?php echo $form->labelEx($model,'email_secondary'); ?>
		<?php echo $form->textField($model,'email_secondary',array('size'=>50,'maxlength'=>50)); ?>
        <span class="add-on">@hotmail.com</span>
		<?php echo $form->error($model,'email_secondary'); ?>
	</div>
    
    <div class="row">
		<?php echo $form->labelEx($model,'address_1'); ?>
		<?php echo $form->textField($model,'address_1',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'address_1'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'address_2'); ?>
		<?php echo $form->textField($model,'address_2',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'address_2'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'address_3'); ?>
		<?php echo $form->textField($model,'address_3',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'address_3'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'country'); ?>
		<?php echo $form->textField($model,'country',array('size'=>30,'maxlength'=>30)); ?>
		<?php echo $form->error($model,'country'); ?>
	</div>
    
  </div>
  
</div>
  <hr />
<div class="row-fluid">
  <div class="span6">
  	<div class="row">
		<?php echo $form->labelEx($model,'national_id'); ?>
		<?php echo $form->textField($model,'national_id',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'national_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'passport_number'); ?>
		<?php echo $form->textField($model,'passport_number',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'passport_number'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'drivers_license'); ?>
		<?php echo $form->textField($model,'drivers_license',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'drivers_license'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'other_id'); ?>
		<?php echo $form->textField($model,'other_id',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'other_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'other_id_2'); ?>
		<?php echo $form->textField($model,'other_id_2',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'other_id_2'); ?>
	</div>
</div>
<div class="span6">
	<div class="row">
		<?php echo $form->labelEx($model,'nationality'); ?>
		<?php echo $form->textField($model,'nationality',array('size'=>50,'maxlength'=>50)); ?>
		<?php echo $form->error($model,'nationality'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'ethnic_race'); ?>
		<?php echo $form->textField($model,'ethnic_race',array('size'=>20,'maxlength'=>20)); ?>
		<?php echo $form->error($model,'ethnic_race'); ?>
	</div>
  
  </div>
</div>
<hr />	
	<div class="row buttons">
		<?php echo CHtml::submitButton($model->isNewRecord ? 'Create' : 'Save',array('class'=>'btn btn-primary')); ?>
	</div>
<?php $this->endWidget();?>


</div><!-- form -->

<?php $this->endWidget(); ?> <!-- portlet -->