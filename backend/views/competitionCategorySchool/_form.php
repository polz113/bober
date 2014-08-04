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
    ));
    ?>

    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>

    <div class="row">
        <?php echo $form->label($model, 'competition_id'); ?>
        <?php $data = CompetitionCategorySchool::model()->GetCompetitionNameIdList();
        echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'competition_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->label($model, 'competition_category_id'); ?>
        <?php $data = CompetitionCategorySchool::model()->GetCompetitionCategoryNameIdList();
        echo CHtml::activeDropDownList($model, 'competition_category_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'competition_category_id'); ?> 
    </div>

    <div class="row">
        <?php echo $form->label($model, 'school_id'); ?>
        <?php $data = CompetitionCategorySchool::model()->GetSchoolNameIdList();
        echo CHtml::activeDropDownList($model, 'school_id', CHtml::listData($data, 'id', 'name'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'school_id'); ?> 
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