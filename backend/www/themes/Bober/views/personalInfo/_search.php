<?php $form=$this->beginWidget('bootstrap.widgets.TbActiveForm',array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>

	<?php echo $form->textFieldRow($model,'pesonal_info_id',array('class'=>'span5','maxlength'=>7)); ?>

	<?php echo $form->textFieldRow($model,'custom_id',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'first_name',array('class'=>'span5','maxlength'=>40)); ?>

	<?php echo $form->textFieldRow($model,'last_name',array('class'=>'span5','maxlength'=>40)); ?>

	<?php echo $form->textFieldRow($model,'phone_home',array('class'=>'span5','maxlength'=>30)); ?>

	<?php echo $form->textFieldRow($model,'phone_work',array('class'=>'span5','maxlength'=>30)); ?>

	<?php echo $form->textFieldRow($model,'phone_mobile',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'fax',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'email_primary',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'email_secondary',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'address_1',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'address_2',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'address_3',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'country',array('class'=>'span5','maxlength'=>30)); ?>

	<?php echo $form->textFieldRow($model,'gender',array('class'=>'span5','maxlength'=>10)); ?>

	<?php echo $form->textFieldRow($model,'marital_status',array('class'=>'span5','maxlength'=>20)); ?>

	<?php echo $form->textFieldRow($model,'dob',array('class'=>'span5')); ?>

	<?php echo $form->textFieldRow($model,'date_joined',array('class'=>'span5')); ?>

	<?php echo $form->textFieldRow($model,'date_left',array('class'=>'span5')); ?>

	<?php echo $form->textFieldRow($model,'middle_name',array('class'=>'span5','maxlength'=>40)); ?>

	<?php echo $form->textFieldRow($model,'national_id',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'passport_number',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'drivers_license',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'other_id',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'other_id_2',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'nationality',array('class'=>'span5','maxlength'=>50)); ?>

	<?php echo $form->textFieldRow($model,'ethnic_race',array('class'=>'span5','maxlength'=>20)); ?>

	<?php echo $form->textFieldRow($model,'smoker',array('class'=>'span5','maxlength'=>5)); ?>

	<?php echo $form->textFieldRow($model,'status',array('class'=>'span5','maxlength'=>20)); ?>

	<div class="form-actions">
		<?php $this->widget('bootstrap.widgets.TbButton', array(
		    'buttonType'=>'submit',
			'type'=>'primary',
			'label'=>'Search',
		)); ?>
	</div>

<?php $this->endWidget(); ?>
