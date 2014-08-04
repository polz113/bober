<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $model CompetitionQuestionDifficulty */
/* @var $form CActiveForm */
?>

<div class="wide form">

    <?php
    $form = $this->beginWidget('CActiveForm', array(
        'action' => Yii::app()->createUrl($this->route),
        'method' => 'get',
            ));
    ?>

        <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>

    <div class="row">
        <?php echo $form->labelEx($model, 'active'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionQuestionDifficulty[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'active'); ?>
    </div>
    
    <div class="row">
        <?php echo $form->labelEx($model, 'country_id'); ?>
        <?php $data = Country::model()->findAll();
        echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'country_id'); ?>
    </div>

    <div class="row">
<?php echo $form->label($model, 'name'); ?>
<?php echo $form->textField($model, 'name', array('size' => 60, 'maxlength' => 255)); ?>
    </div>

    <div class="row">
<?php echo $form->label($model, 'correct_answer_points'); ?>
<?php echo $form->textField($model, 'correct_answer_points', array('size' => 10, 'maxlength' => 10)); ?>
    </div>

    <div class="row">
<?php echo $form->label($model, 'wrong_answer_points'); ?>
<?php echo $form->textField($model, 'wrong_answer_points', array('size' => 10, 'maxlength' => 10)); ?>
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