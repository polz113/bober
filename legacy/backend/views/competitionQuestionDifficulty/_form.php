<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $model CompetitionQuestionDifficulty */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'competition-question-difficulty-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => '$formid',
        'enableAjaxValidation' => false,
            ));
    ?>

    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>

    <div class="row">
        <?php echo $form->labelEx($model, 'active'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionQuestionDifficulty[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'active'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'country_id'); ?>
        <?php $data = Country::model()->GetCountriesICanEdit();
        echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'country_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'name'); ?>
        <?php echo $form->textField($model, 'name', array('size' => 60, 'maxlength' => 255)); ?>
<?php echo $form->error($model, 'name'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'correct_answer_points'); ?>
        <?php echo $form->textField($model, 'correct_answer_points', array('size' => 10, 'maxlength' => 10)); ?>
<?php echo $form->error($model, 'correct_answer_points'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'wrong_answer_points'); ?>
        <?php echo $form->textField($model, 'wrong_answer_points', array('size' => 10, 'maxlength' => 10)); ?>
<?php echo $form->error($model, 'wrong_answer_points'); ?>
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