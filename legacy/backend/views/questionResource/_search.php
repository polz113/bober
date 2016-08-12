<?php
/* @var $this QuestionResourceController */
/* @var $model QuestionResource */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
	
	 <div class="row">
        <?php echo $form->labelEx($model, 'question_id'); ?>
        <?php $data = QuestionResource::model()->GetQuestionTitleIdList();
              echo CHtml::activeDropDownList($model, 'question_id', CHtml::listData($data, 'id', 'title'), array('empty' => Yii::t('app', 'choose'))); ?>
        <?php echo $form->error($model, 'question_id'); ?>
    </div>

	<div class="row">
		<?php echo $form->label($model, 'filename'); ?>
		<?php echo $form->textField($model,'filename',array('size'=>60,'maxlength'=>512)); ?>
	</div>
        
        <div class="row">
		<?php echo $form->label($model, 'type'); ?>
		<?php echo CHtml::dropDownList('QuestionResource[type]',$model->type, $model->GetResourceType(), array('empty' => Yii::t('app', 'choose'))); ?>
	</div>
    
	<div class="row">
		<?php echo $form->label($model, 'file_type'); ?>
		<?php echo $form->textField($model,'file_type',array('size'=>60,'maxlength'=>255)); ?>
	</div>
<!--
	<div class="row">
		<?php echo $form->label($model, 'data'); ?>
		<?php echo $form->textField($model,'data'); ?>
	</div>
        
        <div class="row">
		<?php echo $form->label($model, 'start_up'); ?>
		<?php echo $form->textField($model,'start_up'); ?>
	</div>

-->
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