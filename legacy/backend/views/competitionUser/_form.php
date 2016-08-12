<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
    $superuser = Generic::isSuperAdmin();
    $edit_all = false;
    if ($superuser) {
        $edit_all = true;
    }
    $formid = 'competition-user-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => '$formid',
        'enableAjaxValidation' => false,
    ));
    ?>

    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <?php echo $form->errorSummary($model); ?>

    <div class="row">
        <?php echo $form->label($model, 'competition_id'); ?>
        <?php
        $data = CompetitionCategorySchool::model()->GetCompetitionNameIdList();
        /*
          echo CHtml::activeDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
         */
        $dropdownOptions = array(
            'empty' => Yii::t('app', 'choose'),
            'onchange' => 'competitionChanged();',
            'disabled' => $edit_all ? '' : 'disabled'
        );
        echo CustomCHtml::advancedDropDownList($model, 'competition_id', CHtml::listData($data, 'id', 'name'), $dropdownOptions, array('visible' => false), array('visible' => false));
        ?>
        <?php echo $form->error($model, 'competition_id'); ?>
    </div>

    <div class="row">
        <?php
        echo $form->label($model, 'competition_category_id');

        if (isset($model->id)) {
            $data = CompetitionCategory::model()->with('competitionQuestionCategories')->with('competitionQuestionCategories.competitionQuestion')->together()->findAll('competitionQuestion.competition_id=:competition_id', array(':competition_id' => $model->competition_id));
        } else {
            $data = array();
        }

        $dropdownOptions = array(
            'empty' => Yii::t('app', 'choose'),
            'onchange' => 'competitionCategoryChanged();',
            'disabled' => $edit_all ? '' : 'disabled'
        );

        echo CustomCHtml::advancedDropDownList($model, 'competition_category_id', CHtml::listData($data, 'id', 'name'), $dropdownOptions, array('visible' => false), array('visible' => false));
        unset($data);
        echo $form->error($model, 'competition_category_id');
        ?>

        <?php
        /*
          echo $form->label($model, 'competition_category_id');
          $data = CompetitionCategorySchool::model()->GetCompetitionCategoryNameIdList();
          echo CHtml::activeDropDownList($model, 'competition_category_id', CHtml::listData($data, 'id', 'name'), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
          echo $form->error($model, 'competition_category_id'); */
        ?> 
    </div>
    <?php /*
      <div class="row">
      <?php echo $form->labelEx($model, 'user_id'); ?>
      <?php echo $form->textField($model, 'user_id'); ?>
      <?php echo $form->error($model, 'user_id'); ?>
      </div> */ ?>

    <div class="row">
        <div>
            <?php echo $form->labelEx($model, 'competition_category_school_mentor_id'); ?>
            <?php
            if (isset($model->id)) {
                $data = array();
                $provider = CompetitionCategorySchoolMentor::model()->search(true, $model->competition_id, $model->competition_category_id);
                foreach ($provider->getData() as $mentor) {
                    $data[] = array(
                        'id' => $mentor->id,
                        'name' => $mentor->competitionCategorySchool->school->name . ' - ' . $mentor->user->profile->last_name . ' ' . $mentor->user->profile->first_name
                    );
                }
                $model->orderBy($data, 'order by name asc', true, false);
            } else {
                $data = array();
            }

            // $data = CompetitionCategorySchoolMentor::model()->GetCompetitionCategorySchoolMentorNameIdList();
            echo CustomCHtml::advancedDropDownList($model, 'competition_category_school_mentor_id', CHtml::listData($data, 'id', 'name'), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose'), 'style' => 'width: 600px;'), array('visible' => false), array('visible' => false));
            ?>
            <?php echo $form->error($model, 'competition_category_school_mentor_id'); ?>
        </div>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'last_name'); ?>
        <?php echo $form->textField($model, 'last_name', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'last_name'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'first_name'); ?>
        <?php echo $form->textField($model, 'first_name', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($model, 'first_name'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'gender'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[gender]', $model->gender, array(0 => Yii::t('app', 'Male'), 1 => Yii::t('app', 'Female'))); ?>
        <?php echo $form->error($model, 'gender'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'class'); ?>
        <?php echo $form->textField($model, 'class', array('size' => 20, 'maxlength' => 20)); ?>
        <?php echo $form->error($model, 'class'); ?>
    </div>

    <div class="row">
        <?php echo $form->label($model, 'school_id'); ?>
        <?php
        $data = CompetitionCategorySchool::model()->GetSchoolNameIdList(true);
        echo CHtml::activeDropDownList($model, 'school_id', CHtml::listData($data, 'id', 'name'), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'school_id'); ?> 
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'disqualified_request'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[disqualified_request]', $model->disqualified_request, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
        <?php echo $form->error($model, 'disqualified_request'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'disqualified_reason'); ?>
        <?php echo $form->textArea($model, 'disqualified_reason', array('rows' => 6, 'cols' => 50)); ?>
        <?php echo $form->error($model, 'disqualified_reason'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'disqualified_request_by'); ?>
        <?php
        $data = User::model()->with('profile')->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 5), 'order' => 'profile.last_name ASC, profile.first_name ASC'));
        $user_list = array();
        foreach ($data as $dataUser) {
            $user_list[$dataUser->id] = $dataUser->profile->last_name . ' ' . $dataUser->profile->first_name;
        }
        echo CHtml::activeDropDownList($model, 'disqualified_request_by', $user_list, array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
        ?>
        <?php echo $form->error($model, 'disqualified_request_by'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'disqualified'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[disqualified]', $model->disqualified, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes')), array('disabled' => $edit_all ? '' : 'disabled')); ?>
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
        <?php echo $form->labelEx($model, 'start_time'); ?>
        <?php
        $model->start_time = date('j. n. Y H:i:s', strtotime($model->start_time));
        ?>
        <?php echo $form->textField($model, 'start_time', array('disabled' => $edit_all ? '' : 'disabled')); ?>
        <?php echo $form->error($model, 'start_time'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'finish_time'); ?>
        <?php
        $model->finish_time = date('j. n. Y H:i:s', strtotime($model->finish_time));
        ?>
        <?php echo $form->textField($model, 'finish_time', array('disabled' => $edit_all ? '' : 'disabled')); ?>
        <?php echo $form->error($model, 'finish_time'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'finished'); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[finished]', $model->finished, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'), 2 => Yii::t('app', 'System Yes')), array('disabled' => $edit_all ? '' : 'disabled')); ?>
        <?php echo $form->error($model, 'finished'); ?>
    </div>

    <?php
    if (CompetitionUser::canShowCompetitionResults($model->competition_id)) {
        ?>
        <div class="row">
            <?php echo CHtml::label(Yii::t('app', 'Competition Results'), 'CompetitionResults'); ?>
            <?php echo CHtml::textArea('CompetitionResults', $model->getCompetitionResults(), array('rows' => 3, 'cols' => 100, 'readonly' => true, 'style' => 'width: 500px;')); ?>
        </div>
        <?php
    }
    ?>

    <?php
    if (CompetitionUser::canShowAwardField($model->competition_id)) {
        ?>
        <div class="row">
            <?php echo $form->labelEx($model, 'award'); ?>
            <?php
            echo CHtml::activeDropDownList($model, 'award', $model->GetAwardOptions(), array('disabled' => $edit_all ? '' : 'disabled', 'empty' => Yii::t('app', 'choose')));
            ?>
            <?php echo $form->error($model, 'award'); ?>
        </div>
        <?php
    }
    ?>

    <?php
    if (CompetitionUser::canShowAdvancingToNextLevel($model->competition_id)) {
        ?>
        <div class="row">
            <?php echo $form->labelEx($model, 'advancing_to_next_level'); ?>
            <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[advancing_to_next_level]', $model->advancing_to_next_level, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes')), array('disabled' => $edit_all ? '' : 'disabled')); ?>
            <?php echo $form->error($model, 'advancing_to_next_level'); ?>
        </div>
        <?php
    }
    ?>

    <?php
    /*
      <div class="row">
      <?php echo $form->labelEx($model, 'total_points_via_answers'); ?>
      <?php echo $form->textField($model, 'total_points_via_answers', array('size' => 10, 'maxlength' => 10)); ?>
      <?php echo $form->error($model, 'total_points_via_answers'); ?>
      </div>

      <div class="row">
      <?php echo $form->labelEx($model, 'total_points_via_time'); ?>
      <?php echo $form->textField($model, 'total_points_via_time', array('size' => 10, 'maxlength' => 10)); ?>
      <?php echo $form->error($model, 'total_points_via_time'); ?>
      </div>

      <div class="row">
      <?php echo $form->labelEx($model, 'total_points_manual'); ?>
      <?php echo $form->textField($model, 'total_points_manual', array('size' => 10, 'maxlength' => 10)); ?>
      <?php echo $form->error($model, 'total_points_manual'); ?>
      </div>

      <div class="row">
      <?php echo $form->labelEx($model, 'total_points'); ?>
      <?php echo $form->textField($model, 'total_points', array('size' => 10, 'maxlength' => 10)); ?>
      <?php echo $form->error($model, 'total_points'); ?>
      </div>
     * 
     */
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

<script type="text/javascript">
//<![CDATA[
    function competitionChanged() {
        refreshCompetitionCategory();
    }

    function competitionCategoryChanged() {
        refreshCompetitionCategoryMentors();
    }

    function refreshCompetitionCategory()
    {
        var data = {};
        if (jQuery('#CompetitionUser_competition_id').length > 0) {
            data.competition_id = $('#CompetitionUser_competition_id')[0].value;
        } else {
            data.competition_id = -1;
        }
        if (data.competition_id && data.competition_id !== -1 && data.competition_id != "") {
<?php
echo CHtml::ajax(array(
    'url' => CController::createUrl('competitionUser/loadCompetitionCategory'),
    'data' => array(
        'competition_id' => 'js:data.competition_id',
    ),
    'type' => 'post',
    'dataType' => 'json',
    'success' => "function(retval) {
        loadDropdown('CompetitionUser_competition_category_id', retval, data.id);
        if (data.onCompleted)
        {
            data.onCompleted();
        }
    }"
));
?>
        }
    }

    function refreshCompetitionCategoryMentors() {
        var data = {};
        if (jQuery('#CompetitionUser_competition_id').length > 0) {
            data.competition_id = $('#CompetitionUser_competition_id')[0].value;
        } else {
            data.competition_id = -1;
        }
        if (jQuery('#CompetitionUser_competition_category_id').length > 0) {
            data.competition_category_id = $('#CompetitionUser_competition_category_id')[0].value;
        } else {
            data.competition_category_id = -1;
        }
        if (data.competition_id && data.competition_id !== -1 && data.competition_id != "" && data.competition_category_id && data.competition_category_id !== -1 && data.competition_category_id != "") {
<?php
echo CHtml::ajax(array(
    'url' => CController::createUrl('competitionUser/loadCompetitionCategoryMentors'),
    'data' => array(
        'competition_id' => 'js:data.competition_id',
        'competition_category_id' => 'js:data.competition_category_id',
    ),
    'type' => 'post',
    'dataType' => 'json',
    'success' => "function(retval) {
        loadDropdown('CompetitionUser_competition_category_school_mentor_id', retval, data.id);
        if (data.onCompleted)
        {
            data.onCompleted();
        }
    }"
));
?>
        }
    }
    //]]>
</script>