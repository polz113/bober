<?php
/* @var $this SchoolController */
/* @var $model School */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'school-form';

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
        <?php echo $form->labelEx($model, 'school_category_id'); ?>
        <?php echo $form->textField($model, 'school_category_id'); ?>
        <?php echo $form->error($model, 'school_category_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'level_of_education'); ?>
        <?php echo CHtml::dropDownList('School[level_of_education]', $model->level_of_education, $model->GetLevelsOfEducation(), array('empty' => Yii::t('app', 'choose'))); ?>
        <?php echo $form->error($model, 'level_of_education'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'address'); ?>
        <?php echo $form->textField($model, 'address', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'address'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'post'); ?>
        <?php echo $form->textField($model, 'post', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'post'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'postal_code'); ?>
        <?php echo $form->textField($model, 'postal_code'); ?>
        <?php echo $form->error($model, 'postal_code'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'country_id'); ?>
        <?php
        $data = Country::model()->GetCountriesICanEdit();
        echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'country_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'region_id'); ?>
        <?php
        $data = Region::model()->GetRegionsICanEdit();
        echo CHtml::activeDropDownList($model, 'region_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'region_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'municipality_id'); ?>
        <?php
        $data = Municipality::model()->GetMunicipalityICanEdit();
        echo CHtml::activeDropDownList($model, 'municipality_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'municipality_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'tax_number'); ?>
        <?php echo $form->textField($model, 'tax_number', array('size' => 12, 'maxlength' => 12)); ?>
<?php echo $form->error($model, 'tax_number'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'identifier'); ?>
        <?php echo $form->textField($model, 'identifier', array('size' => 20, 'maxlength' => 20)); ?>
<?php echo $form->error($model, 'identifier'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'headmaster'); ?>
        <?php echo $form->textField($model, 'headmaster', array('size' => 60, 'maxlength' => 255)); ?>
<?php echo $form->error($model, 'headmaster'); ?>
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