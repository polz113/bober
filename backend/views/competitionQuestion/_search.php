<?php
/* @var $this CompetitionQuestionController */
/* @var $model CompetitionQuestion */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>

	<div class="row">
		<?php echo $form->label($model, 'competition_id'); ?>
		<?php $data = CompetitionQuestion::model()->GetCompetitionNameIdList();
                      echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
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
            'caption' => Yii::t('app', 'search'),
            'value' => Yii::t('app', 'search')
        ));
        ?>	</div>

<?php $this->endWidget(); ?>

</div><!-- search-form -->