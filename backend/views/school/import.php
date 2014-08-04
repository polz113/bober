<?php
$this->breadcrumbs = array(
    Yii::t('app', 'Schools') => array('admin'),
    Yii::t('app', 'Import schools'),
);

$user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
$superuser = $user != null ? $user->superuser : 0;
$create_competition_user = false;
$export_active_mentors = false;
$export_user_data = false;
$check_data = false;
$calculate_awards = false;
if ($superuser) {
    $create_competition_user = true;
    $export_active_mentors = true;
    $export_user_data = true;
    $check_data = true;
    $import_data = true;
    $calculate_awards = true;
}

$this->menu = array(
    array('label' => Yii::t('app', 'Manage Schools'), 'url' => array('admin')),
    array('label'=>Yii::t('app', 'Create School'), 'url' => array('create')),
);
?>

<h1><?php echo Yii::t('app', 'Import schools'); ?></h1>

<div class="form">

    <?php
    $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
    $superuser = $user != null ? $user->superuser : 0;
    $edit_all = false;
    if ($superuser == 1) {
        $edit_all = true;
    }
    $formid = 'school-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => '$formid',
        'enableAjaxValidation' => false,
        'htmlOptions' => array('enctype' => 'multipart/form-data')
    ));
    ?>

    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>

    <div class="row">
        <?php echo $form->labelEx($model, 'Data'); ?>
        <?php echo $form->fileField($model, 'uploadedData'); ?>
        <?php echo $form->error($model, 'data'); ?>
    </div>

    <div class="row buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => Yii::t('app', 'Import'),
            'value' => Yii::t('app', 'Import')
        ));
        ?>	</div>

    <?php $this->endWidget(); ?>

</div>