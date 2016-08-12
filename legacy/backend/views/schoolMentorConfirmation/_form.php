<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $model SchoolMentorConfirmation */
/* @var $form CActiveForm */
?>

<div class="form">

<?php 
$formid = 'school-mentor-confirmation-form';

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
		<?php echo $form->labelEx($model,'school_id'); ?>
		<?php echo $form->textField($model,'school_id'); ?>
		<?php echo $form->error($model, 'school_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'user_id'); ?>
		<?php echo $form->textField($model,'user_id'); ?>
		<?php echo $form->error($model, 'user_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'active'); ?>
		<?php echo $form->textField($model,'active'); ?>
		<?php echo $form->error($model, 'active'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'activated_by'); ?>
		<?php echo $form->textField($model,'activated_by'); ?>
		<?php echo $form->error($model, 'activated_by'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'activated_timestamp'); ?>
		<?php echo $form->textField($model,'activated_timestamp'); ?>
		<?php echo $form->error($model, 'activated_timestamp'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'coordinator'); ?>
		<?php echo $form->textField($model,'coordinator'); ?>
		<?php echo $form->error($model, 'coordinator'); ?>
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