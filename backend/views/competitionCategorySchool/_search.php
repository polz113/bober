<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */
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
		<?php $data = CompetitionCategorySchool::model()->GetCompetitionNameIdList();
                      echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
                <?php echo $form->error($model, 'competition_id'); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'competition_category_id'); ?>
		<?php $data = CompetitionCategorySchool::model()->GetCompetitionCategoryNameIdList();
                      echo CHtml::activeDropDownList($model, 'competition_category_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
                <?php echo $form->error($model, 'competition_category_id'); ?> 
	</div>

	<div class="row">
		<?php echo $form->label($model, 'school_id'); ?>
		<?php echo $form->textField($model,'school_search'); ?>
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