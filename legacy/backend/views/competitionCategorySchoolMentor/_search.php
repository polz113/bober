<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $model CompetitionCategorySchoolMentor */
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
<?php echo $form->label($model, 'competition_category_school_id'); ?>
<?php echo $form->textField($model, 'competition_school_search'); ?>
    </div>

    <div class="row">
<?php echo $form->label($model, 'user_id'); ?>
<?php echo $form->textField($model, 'user_search'); ?>
    </div>

    <div class="row">
    <?php echo $form->label($model, 'access_code'); ?>
    <?php echo $form->textField($model, 'access_code', array('size' => 20, 'maxlength' => 20)); ?>
    </div>
    <?php
    $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
    if ($user != null && $user->profile->user_role > 5) {
        ?>

        <div class="row">
    <?php echo $form->label($model, 'disqualified'); ?>
    <?php echo $form->textField($model, 'disqualified'); ?>
        </div>

        <div class="row">
    <?php echo $form->label($model, 'disqualified_by'); ?>
    <?php echo $form->textField($model, 'disqualified_by'); ?>
        </div>

        <div class="row">
        <?php echo $form->label($model, 'disqualified_reason'); ?>
        <?php echo $form->textArea($model, 'disqualified_reason', array('rows' => 6, 'cols' => 50)); ?>
        </div>
        <?php
    }
    ?>
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