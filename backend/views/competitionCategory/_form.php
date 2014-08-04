<?php
/* @var $this CompetitionCategoryController */
/* @var $model CompetitionCategory */
/* @var $form CActiveForm */
?>

<div class="form">

<?php 
$formid = 'competition-category-form';

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
		<?php echo $form->labelEx($model,'active'); ?>
		<?php echo CustomCHtml::radioButtonSwitch('CompetitionCategory[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
		<?php echo $form->error($model, 'active'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'name'); ?>
		<?php echo $form->textField($model,'name',array('size'=>60,'maxlength'=>255)); ?>
		<?php echo $form->error($model, 'name'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'level_of_education'); ?>
		<?php echo CHtml::dropDownList('CompetitionCategory[level_of_education]',$model->level_of_education, $model->GetLevelsOfEducation(), array('empty' => Yii::t('app', 'choose'))); ?>
		<?php echo $form->error($model, 'level_of_education'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'class_from'); ?>
		<?php echo $form->textField($model,'class_from'); ?>
		<?php echo $form->error($model, 'class_from'); ?>
	</div>

	<div class="row">
		<?php echo $form->labelEx($model,'class_to'); ?>
		<?php echo $form->textField($model,'class_to'); ?>
		<?php echo $form->error($model, 'class_to'); ?>
	</div>
        
        <div class="row">
		<?php echo $form->labelEx($model,'country_id'); ?>
		<?php $data = Country::model()->GetCountriesICanEdit();
                      echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));  ?>
		<?php echo $form->error($model, 'country_id'); ?>
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