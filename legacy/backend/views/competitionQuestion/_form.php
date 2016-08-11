<?php
/* @var $this CompetitionQuestionController */
/* @var $model CompetitionQuestion */
/* @var $form CActiveForm */
?>

<div class="form">

<?php 
$formid = 'competition-question-form';

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
		<?php echo $form->labelEx($model,'competition_id'); ?>
		<?php $data = CompetitionQuestion::model()->GetCompetitionNameIdList();
                      echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));  ?>
		<?php echo $form->error($model, 'competition_id'); ?>
	</div>

        <div class="row">
                <?php echo $form->labelEx($model, 'question_id'); ?>
                <?php $data = QuestionResource::model()->GetQuestionTitleIdList();
                      echo CHtml::activeDropDownList($model, 'question_id', CHtml::listData($data, 'id', 'title'), array('empty' => Yii::t('app', 'choose'))); ?>
                <?php echo $form->error($model, 'question_id'); ?>
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