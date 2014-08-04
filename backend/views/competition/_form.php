<?php
/* @var $this CompetitionController */
/* @var $model Competition */
/* @var $form CActiveForm */


Yii::import('application.extensions.CJuiDateTimePicker.CJuiDateTimePicker');
?>

<div class="form">

    <?php
    $formid = 'competition-form';

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
        <?php echo $form->labelEx($model, 'name'); ?>
        <?php echo $form->textField($model, 'name', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'name'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'active'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('Competition[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'active'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'timestamp_start'); ?>
        <?php
        $model->timestamp_start = Yii::app()->localtime->toLocalDateTime($model->timestamp_start, 'medium');
        $this->widget('CJuiDateTimePicker', array(
            'model' => $model, //Model object
            'attribute' => 'timestamp_start', //attribute name
            'mode' => 'datetime', //use "time","date" or "datetime" (default)
            'options' => array(
                'dateFormat' => Yii::app()->localtime->getLocalDateFormat('js')
            ) // jquery plugin options
        ));
        ?>
        <?php echo $form->error($model, 'timestamp_start'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'timestamp_stop'); ?>
        <?php
        $model->timestamp_stop = Yii::app()->localtime->toLocalDateTime($model->timestamp_stop, 'medium');
        $this->widget('CJuiDateTimePicker', array(
            'model' => $model, //Model object
            'attribute' => 'timestamp_stop', //attribute name
            'mode' => 'datetime', //use "time","date" or "datetime" (default)
            'options' => array(
                'dateFormat' => Yii::app()->localtime->getLocalDateFormat('js')
            ) // jquery plugin options
        ));
        ?>
        <?php echo $form->error($model, 'timestamp_stop'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'type'); ?>
        <?php echo CHtml::dropDownList('Competition[type]', $model->type, $model->GetTypeOfCompetition(), array('empty' => Yii::t('app', 'choose'))); ?>
        <?php echo $form->error($model, 'type'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'public_access'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('Competition[public_access]', $model->public_access, array(2 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'public_access'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'duration'); ?>
        <?php echo $form->textField($model, 'duration'); ?>
        <?php echo $form->error($model, 'duration'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'timestamp_mentor_results'); ?>
        <?php
        $model->timestamp_mentor_results = $model->timestamp_mentor_results != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_results, 'medium') : '';
        $this->widget('CJuiDateTimePicker', array(
            'model' => $model, //Model object
            'attribute' => 'timestamp_mentor_results', //attribute name
            'mode' => 'datetime', //use "time","date" or "datetime" (default)
            'options' => array(
                'dateFormat' => Yii::app()->localtime->getLocalDateFormat('js')
            ) // jquery plugin options
        ));
        ?>
        <?php echo $form->error($model, 'timestamp_mentor_results'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'timestamp_mentor_awards'); ?>
        <?php
        $model->timestamp_mentor_awards = $model->timestamp_mentor_awards != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_awards, 'medium') : '';
        $this->widget('CJuiDateTimePicker', array(
            'model' => $model, //Model object
            'attribute' => 'timestamp_mentor_awards', //attribute name
            'mode' => 'datetime', //use "time","date" or "datetime" (default)
            'options' => array(
                'dateFormat' => Yii::app()->localtime->getLocalDateFormat('js')
            ) // jquery plugin options
        ));
        ?>
        <?php echo $form->error($model, 'timestamp_mentor_awards'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'timestamp_mentor_advancing_to_next_level'); ?>
        <?php
        $model->timestamp_mentor_advancing_to_next_level = $model->timestamp_mentor_advancing_to_next_level != null ? Yii::app()->localtime->toLocalDateTime($model->timestamp_mentor_advancing_to_next_level, 'medium') : '';
        $this->widget('CJuiDateTimePicker', array(
            'model' => $model, //Model object
            'attribute' => 'timestamp_mentor_advancing_to_next_level', //attribute name
            'mode' => 'datetime', //use "time","date" or "datetime" (default)
            'options' => array(
                'dateFormat' => Yii::app()->localtime->getLocalDateFormat('js')
            ) // jquery plugin options
        ));
        ?>
        <?php echo $form->error($model, 'timestamp_mentor_advancing_to_next_level'); ?>
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