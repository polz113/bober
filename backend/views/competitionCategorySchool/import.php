<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */

$this->breadcrumbs = array(
    Yii::t('app', 'Register School For Competition') => array('admin'),
    Yii::t('app', 'create'),
);

$this->menu = array(
    array('label' => Yii::t('app', 'All School Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Register School'); ?></h1>

<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $model CompetitionCategorySchool */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'competition-category-school-form';

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
        <?php echo $form->label($model, 'competition_id'); ?>
        <?php
        $data = CompetitionCategorySchool::model()->GetCompetitionNameIdList();
        echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'competition_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->label($model, 'country_id'); ?>
        <?php
        $data = Country::model()->search(true);
        $list = array();
        foreach ($data->getData() as $country) {
            $list[] = $country;
        }
        echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($list, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'country_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'Data'); ?>
        <?php echo $form->fileField($model, 'uploadedData'); ?>
        <?php echo $form->error($model, 'data'); ?>
    </div>

    <div class="row buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => Yii::t('app', 'import'),
            'value' => Yii::t('app', 'import')
        ));
        ?>	</div>

    <?php $this->endWidget(); ?>

</div><!-- form -->