<?php
/* @var $this CompetitionCategoryController */
/* @var $model CompetitionCategory */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    
	<div class="row">
		<?php echo $form->labelEx($model,'active'); ?>
		<?php echo CustomCHtml::radioButtonSwitch('CompetitionCategory[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
		<?php echo $form->error($model, 'active'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'name'); ?>
		<?php echo $form->textField($model,'name',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'level_of_education'); ?>
		<?php echo CHtml::dropDownList('CompetitionCategory[level_of_education]',$model->level_of_education, $model->GetLevelsOfEducation(), array('empty' => Yii::t('app', 'choose'))); ?>
		<?php echo $form->error($model, 'level_of_education'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'class_from'); ?>
		<?php echo $form->textField($model,'class_from'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'class_to'); ?>
		<?php echo $form->textField($model,'class_to'); ?>
	</div>

        <div class="row">
		<?php echo $form->label($model, 'country_id'); ?>
		<?php $data = Country::model()->GetCountriesICanEdit();
                      echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));  ?>
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