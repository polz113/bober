<?php
/* @var $this StartCompetitionController */
/* @var $model StartCompetition */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'start-competition-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => 'StartCompetition',
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
        <?php echo $form->labelEx($model, 'first_name'); ?>
        <?php echo $form->textField($model, 'first_name', array('size' => 60, 'maxlength' => 255, 'autocomplete' => 'off')); ?>
        <?php echo $form->error($model, 'first_name'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'last_name'); ?>
        <?php echo $form->textField($model, 'last_name', array('size' => 60, 'maxlength' => 255, 'autocomplete' => 'off')); ?>
        <?php echo $form->error($model, 'last_name'); ?>
    </div>

    <div class="row">
        <div style="width: 154px; float: left;">
            <?php echo $form->labelEx($model, 'class'); ?>
        </div>
        <div style="width: 67px; float: left;">
            <?php
            $list = array();
            for ($i = 1; $i < 10; $i++) {
                $list[] = array(
                    'id' => $i,
                    'name' => $i . '.'
                );
            }
            echo CHtml::activeDropDownList($model, 'class_numberic', CHtml::listData($list, 'id', 'name'), array('empty' => Yii::t('app', 'choose'), 'style' => 'width: 63px;'));
            ?>
        </div>
        <div style="width: 125px; float: left;">
            <?php echo $form->textField($model, 'class', array('size' => 20, 'maxlength' => 20, 'autocomplete' => 'off', 'style' => 'width: 115px; padding-left: 5px;')); ?>
        </div>
        <div style="clear: both;"></div>
        <?php echo $form->error($model, 'class'); ?>
    </div>

    <div class="row" style="width: 420px; height: 19px;">
        <?php echo $form->labelEx($model, 'gender', array('id' => 'GenderLabel')); ?>
        <?php echo CustomCHtml::radioButtonSwitch('CompetitionUser[gender]', $model->gender, array(0 => Yii::t('app', 'Male'), 1 => Yii::t('app', 'Female')), array('labelOptions' => array("style" => "width:50px;"))); ?>
        <?php echo $form->error($model, 'gender'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'access_code'); ?>
        <?php echo $form->textField($model, 'access_code', array('autocomplete' => 'off')); ?>
        <?php echo $form->error($model, 'access_code'); ?>
    </div>

    <div class="row" style="text-align: center;">
        <?php echo Yii::t('app', 'Please check if you have the right access code for competing in your category.'); ?>
    </div>

    <div class="buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord = Yii::t('app', 'Start'),
            'value' => $model->isNewRecord = Yii::t('app', 'Start')
        ));
        ?>    </div>

	<?php
	
	/* Login as guest button */

	?>
    <?php $this->endWidget(); ?>



    <div id="language_select_black">
        <?php
        $languages = Language::model()->findAll();
        foreach ($languages as $language) {
            ?>
            <a href="/index.php/StartCompetition/changeLanguage/?lang=<?php echo $language->short; ?>"><?php echo $language->short; ?></a>&nbsp;
            <?php
        }
        ?>
    </div>
    <div class="clearfix"></div>

</div><!-- form -->
