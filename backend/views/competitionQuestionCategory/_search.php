<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $model CompetitionQuestionCategory */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>

	<div class="row">
		<?php echo $form->label($model, 'competition_question_id'); ?>
		<?php $data = CompetitionQuestionCategory::model()->GetCompetitionQuestionIdList();
                 echo CHtml::activeDropDownList($model, 'competition_question_id', CHtml::listData($data, 'competition_id', 'id'), array('empty' => Yii::t('app', 'choose'))); ?>
		<?php echo $form->error($model, 'competition_question_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competition_category_id'); ?>
		<?php $data = CompetitionQuestionCategory::model()->GetCompetitionCategoryNameIdList();
                      echo CHtml::activeDropDownList($model, 'competition_category_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
                <?php echo $form->error($model, 'competition_category_id'); ?> 
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competiton_question_difficulty_id'); ?>
		<?php $data = CompetitionQuestionCategory::model()->GetCompetitionQuestionDifficultyNameIdList();
                      echo CHtml::activeDropDownList($model, 'competiton_question_difficulty_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
                <?php echo $form->error($model, 'competiton_question_difficulty_id'); ?> 
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