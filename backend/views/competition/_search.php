<?php
/* @var $this CompetitionController */
/* @var $model Competition */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
	
	<div class="row">
		<?php echo $form->label($model, 'name'); ?>
		<?php echo $form->textField($model,'name',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'active'); ?>
		<?php echo CustomCHtml::radioButtonSwitch('Competition[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
		<?php echo $form->error($model, 'active'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'timestamp_start'); ?>
		<?php echo $form->textField($model,'timestamp_start'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'timestamp_stop'); ?>
		<?php echo $form->textField($model,'timestamp_stop'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'type'); ?>
		<?php echo CHtml::dropDownList('Competition[type]',$model->type, $model->GetTypeOfCompetition(), array('empty' => Yii::t('app', 'choose'))); ?>
		<?php echo $form->error($model, 'type'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'public_access'); ?>
		<?php echo CustomCHtml::radioButtonSwitch('Competition[public_access]', $model->public_access, array(2 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
		<?php echo $form->error($model, 'public_access'); ?>
	</div>
    
        <div class="row">
		<?php echo $form->label($model, 'duration'); ?>
		<?php echo $form->textField($model,'duration'); ?>
                <?php echo $form->error($model,'duration'); ?>
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