<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $model SchoolMentorConfirmation */
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
		<?php echo $form->label($model, 'school_id'); ?>
		<?php echo $form->textField($model,'school_search'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'user_id'); ?>
		<?php echo $form->textField($model,'user_search'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'active'); ?>
		<?php echo $form->textField($model,'active'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'activated_by'); ?>
		<?php echo $form->textField($model,'activated_by'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'activated_timestamp'); ?>
		<?php echo $form->textField($model,'activated_timestamp'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'coordinator'); ?>
		<?php echo $form->textField($model,'coordinator'); ?>
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