<?php
/* @var $this MentorRegistrationController */
/* @var $model MentorRegistration */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'mentor-registration-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => 'MentorRegistration',
        'enableAjaxValidation' => false,
    ));
    ?>
    <?php
    if (isset(Yii::app()->session['errorMsg'])) {
        ?>
        <div class="errors">
            <?php
            echo Yii::app()->session['errorMsg'];
            unset(Yii::app()->session['errorMsg']);
            ?>
        </div>
        <?php
    }
    ?>
    <p class="note"><?php echo Yii::t('app', 'fields_with'); ?> <span class="required">*</span> <?php echo Yii::t('app', 'are_required'); ?>.</p>

    <div class="row">
        <?php echo $form->label($model, 'username'); ?><br>
        <?php echo $form->textField($model, 'username', array('size' => 20, 'maxlength' => 20)); ?>
        <?php echo $form->error($model, 'username'); ?>
    </div>

    <div class="row">
        <?php echo $form->label($model, 'password'); ?><br>
        <?php echo $form->passwordField($model, 'password', array('size' => 30, 'maxlength' => 30, 'style' => 'width:204px;')); ?>
        <?php echo $form->error($model, 'password'); ?>
    </div>


    <div class="row">
        <?php echo $form->label($profile, 'first_name'); ?><br>
        <?php echo $form->textField($profile, 'first_name', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($profile, 'first_name'); ?>
    </div>


    <div class="row">
        <?php echo $form->label($profile, 'last_name'); ?><br>
        <?php echo $form->textField($profile, 'last_name', array('size' => 60, 'maxlength' => 255)); ?>
        <?php echo $form->error($profile, 'last_name'); ?>
    </div>

    <div class="row">
        <?php echo $form->label($model, 'email'); ?><br>
        <?php echo $form->textField($model, 'email', array('size' => 40, 'maxlength' => 40)); ?>
        <?php echo $form->error($model, 'email'); ?>
    </div>


    <div class="row">
        <?php echo $form->label($profile, 'phone_number'); ?><br>
        <?php echo $form->textField($profile, 'phone_number', array('size' => 20, 'maxlength' => 20)); ?>
        <?php echo $form->error($profile, 'phone_number'); ?>
    </div>
    
      <div class="row">
    <div id="drop_down_language">
		<?php echo $form->label($profile, 'language_id'); ?><br>
		<?php $data = Language::model()->GetLanguageList();
                      echo CHtml::activeDropDownList($profile, 'language_id', CHtml::listData($data, 'id', 'name'), array('id' => 'language_id', 'empty' => Yii::t('app', 'choose'), 'style' => 'width:204px;')); ?>
                <?php echo $form->error($profile, 'language_id'); ?> 
    </div>
    </div>

    <div class="row">
        <?php echo $form->label($profile, 'country_id'); ?><br>
        <?php
        $data = Country::model()->findAll();
        echo CHtml::activeDropDownList($profile, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose'), 'ajax' => array(
                'type' => 'POST', //request type
                'url' => CController::createUrl('mentorRegistration/loadSchools'), //url to call.
//Style: CController::createUrl('currentController/methodToCall')
                'update' => '#school_id', //selector to update
//'data'=>'js:javascript statement' 
//leave out the data key to pass all form values through
        ),'style' => 'width:204px;'));
        ?>
        <?php echo $form->error($profile, 'country_id'); ?>
    </div>
    <div class="row">
        <div id="drop_down_school">
            <?php echo $form->label($school_mentor, 'school_id'); ?><br>
            <?php
            $data = CompetitionCategorySchool::model()->GetSchoolNameIdList();
            echo CHtml::activeDropDownList($school_mentor, 'school_id', array(), array('id' => 'school_id', 'empty' => Yii::t('app', 'choose'), 'onChange' => 'schoolDropDownChanged();', 'style' => 'width:204px;'));
            ?>
            <?php echo $form->error($school_mentor, 'school_id'); ?> 
        </div>
    </div>

    <div class="row">
        <div id="coordinator_id">
            <?php echo $form->labelEx($school_mentor, 'Do you want to be coordinator?'); ?><br>
            <?php echo CustomCHtml::radioButtonSwitch('SchoolMentor[coordinator]', $school_mentor->coordinator, array(0 => Yii::t('app', 'no'), 1 => Yii::t('app', 'yes'))); ?>
<?php echo $form->error($school_mentor, 'coordinator'); ?>
        </div>
    </div>


    <div class="buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord = Yii::t('app', 'Register'),
            'value' => $model->isNewRecord = Yii::t('app', 'Register'),
            'htmlOptions'=>array(
                        'style'=>'height: 35px; font-size: 12px; width: 200px',
                )
           
        ));
        ?>    </div>

        <?php $this->endWidget(); ?>

    <div id="language_select_black">
        <?php
        $languages = Language::model()->findAll();
        foreach ($languages as $language) {
            ?>
            <a href="/index.php/MentorRegistration/changeLanguage/?lang=<?php echo $language->short; ?>"><?php echo $language->short; ?></a>&nbsp;
            <?php
        }
        ?>
    </div>
    <div class="clearfix"></div>

</div><!-- form -->

<script type="text/javascript">
    //<![CDATA[
    function schoolDropDownChanged() {
        jQuery(document).ready(function() {
            var school = jQuery("#drop_down_school :selected").text();
            var coordinator = "<?php echo Yii::t('app', 'Coordinator'); ?>";
            var split = school.split(coordinator);
            if (split.length > 1) {
                jQuery("#coordinator_id").hide();
            } else {
                jQuery("#coordinator_id").show();
            }
        });
    }
    jQuery(document).ready(function() {
        jQuery("#coordinator_id").hide();
    });
    //]]>
</script>