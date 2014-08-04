<?php
/* @var $this QuestionResourceController */
/* @var $model QuestionResource */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'question-resource-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => '$formid',
        'enableAjaxValidation' => false,
        'htmlOptions' => array('enctype' => 'multipart/form-data'),
            ));
    ?>

    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>

    <div class="row">
        <?php echo $form->labelEx($model, 'question_id'); ?>
        <?php
        $data = QuestionResource::model()->GetQuestionTitleIdList();
        echo CHtml::activeDropDownList($model, 'question_id', CHtml::listData($data, 'id', 'title'), array('empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'question_id'); ?>
    </div>
    
    <div class="row">
        <?php echo $form->labelEx($model, 'path'); ?>
        <?php echo $form->textField($model, 'path', array('size' => 60, 'maxlength' => 250)); ?>
        <?php echo $form->error($model, 'path'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'filename'); ?>
        <?php echo $form->textField($model, 'filename', array('size' => 60, 'maxlength' => 250)); ?>
        <?php echo $form->error($model, 'filename'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'file_type'); ?>
        <?php echo $form->textField($model, 'file_type', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'file_type'); ?>
    </div>
    
    <div class="row">
        <?php echo $form->labelEx($model,'type'); ?>
        <?php echo CHtml::dropDownList('QuestionResource[type]', $model->type, $model->GetResourceType());  ?>
	<?php echo $form->error($model, 'type'); ?>
    </div>
    
    <div class="row">
        <?php echo $form->labelEx($model, 'language_id'); ?>
        <?php $data = QuestionResource::model()->GetLanguageIdList();
              echo CHtml::activeDropDownList($model, 'language_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose'))); ?>
        <?php echo $form->error($model, 'language_id'); ?>
    </div>
    
    <div class="row">
        <?php echo $form->labelEx($model, 'data'); ?>
        <?php echo $form->fileField($model, 'uploadedData'); ?>
        <?php echo $form->error($model, 'data'); ?>
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