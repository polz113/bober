<?php
/* @var $this SchoolController */
/* @var $model School */
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
		<?php echo $form->label($model, 'school_category_id'); ?>
		<?php echo $form->textField($model,'school_category_search'); ?>
	</div>
    
        <div class="row">
		<?php echo $form->labelEx($model,'level_of_education'); ?>
		<?php echo CHtml::dropDownList('CompetitionCategory[level_of_education]',$model->level_of_education, $model->GetLevelsOfEducation(), array('empty' => Yii::t('app', 'choose'))); ?>
		<?php echo $form->error($model, 'level_of_education'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'address'); ?>
		<?php echo $form->textField($model,'address',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'post'); ?>
		<?php echo $form->textField($model,'post',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'postal_code'); ?>
		<?php echo $form->textField($model,'postal_code'); ?>
	</div>

	

	<div class="row">
		<?php echo $form->label($model, 'region_id'); ?>
		<?php echo $form->textField($model,'region_search'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'country_id'); ?>
		<?php echo $form->textField($model,'country_search'); ?>
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