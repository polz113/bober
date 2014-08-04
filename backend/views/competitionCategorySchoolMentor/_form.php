<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $model CompetitionCategorySchoolMentor */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'competition-category-school-mentor-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => '$formid',
        'enableAjaxValidation' => false,
    ));
    $edit_all = true;
    ?>

    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>



    <div class="row">
        <?php echo $form->label($model, 'competition_category_school_id'); ?>
        <?php
        $data = CompetitionCategorySchoolMentor::model()->GetCompetitionCategorySchoolNameIdList();
        echo CHtml::activeDropDownList($model, 'competition_category_school_id', CHtml::listData($data, 'id', 'name'), array('style' => 'width: 400px;', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'competition_category_school_id'); ?>
    </div>

    <?php
    $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
    if ($user != null && $user->profile->user_role > 5) {
        ?>
        <div class="row">
            <?php echo $form->labelEx($model, 'user_id'); ?>
            <?php
            $data = SchoolMentor::model()->with('user.profile')->with('school')->together()->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 5), 'order' => 'profile.last_name ASC, profile.first_name ASC, school.name ASC'));
            $user_list = array();
            $schools_per_user = array();
            foreach ($data as $dataUser) {
                if (!isset($user_list[$dataUser->user->id])) {
                    $user_list[$dataUser->user->id] = $dataUser->user->profile->last_name . ' ' . $dataUser->user->profile->first_name;
                }
                if (!isset($schools_per_user[$dataUser->user->id])) {
                    $schools_per_user[$dataUser->user->id] = array();
                }
                $schools_per_user[$dataUser->user->id][] = $dataUser->school->name;
            }
            foreach ($user_list as $mentor_user_id => $userData) {
                if (isset($schools_per_user[$mentor_user_id])) {
                    if (count($schools_per_user[$mentor_user_id]) > 0) {
                        $user_list[$mentor_user_id] .= ' ('.implode(', ', $schools_per_user[$mentor_user_id]).')';
                    }
                }
            }
            echo CHtml::activeDropDownList($model, 'user_id', $user_list, array('empty' => Yii::t('app', 'choose')));
            ?>
            <?php echo $form->error($model, 'user_id'); ?>
        </div>

        <div class="row">
            <?php echo $form->labelEx($model, 'disqualified'); ?>
            <?php echo CustomCHtml::radioButtonSwitch('CompetitionCategorySchoolMentor[disqualified]', $model->disqualified, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes')), array('disabled' => $edit_all ? '' : 'disabled')); ?>
            <?php echo $form->error($model, 'disqualified'); ?>
        </div>

        <div class="row">
            <?php echo $form->labelEx($model, 'disqualified_by'); ?>
            <?php
            $data = User::model()->with('profile')->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 10), 'order' => 'profile.last_name ASC, profile.first_name ASC'));
            $user_list = array();
            foreach ($data as $dataUser) {
                $user_list[$dataUser->id] = $dataUser->profile->last_name . ' ' . $dataUser->profile->first_name;
            }
            echo CHtml::activeDropDownList($model, 'disqualified_by', $user_list, array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
            ?>
            <?php echo $form->error($model, 'disqualified_by'); ?>
        </div>

        <div class="row">
            <?php echo $form->labelEx($model, 'disqualified_reason'); ?>
            <?php echo $form->textArea($model, 'disqualified_reason', array('rows' => 6, 'cols' => 50)); ?>
            <?php echo $form->error($model, 'disqualified_reason'); ?>
        </div>

        <?php
    }
    ?>

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
