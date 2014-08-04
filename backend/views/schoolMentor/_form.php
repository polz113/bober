<?php
/* @var $this SchoolMentorController */
/* @var $model SchoolMentor */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $edit_all = true;
    $formid = 'school-mentor-form';

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
        <?php echo $form->label($model, 'school_id'); ?>
        <?php
        $data = CompetitionCategorySchool::model()->GetSchoolNameIdList();
        echo CHtml::activeDropDownList($model, 'school_id', CHtml::listData($data, 'id', 'name'), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'school_id'); ?> 
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'user_id'); ?>
        <?php
        $data = User::model()->with('profile')->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 5), 'order' => 'profile.last_name ASC, profile.first_name ASC'));
        $user_list = array();
        foreach ($data as $dataUser) {
            $user_list[$dataUser->id] = $dataUser->profile->last_name . ' ' . $dataUser->profile->first_name;
        }
        echo CHtml::activeDropDownList($model, 'user_id', $user_list, array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'user_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'active'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('SchoolMentor[active]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'active'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'activated_by'); ?>
        <?php
        $data = User::model()->with('profile')->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 5), 'order' => 'profile.last_name ASC, profile.first_name ASC'));
        $user_list = array();
        foreach ($data as $dataUser) {
            $user_list[$dataUser->id] = $dataUser->profile->last_name . ' ' . $dataUser->profile->first_name;
        }
        echo CHtml::activeDropDownList($model, 'activated_by', $user_list, array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'activated_by'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'activated_timestamp'); ?>
        <?php echo $form->textField($model, 'activated_timestamp'); ?>
        <?php echo $form->error($model, 'activated_timestamp'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'coordinator'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('SchoolMentor[coordinator]', $model->active, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'coordinator'); ?>
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