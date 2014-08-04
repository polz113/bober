<?php
/* @var $this MentorRegistrationController */
/* @var $model MentorRegistration */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'home-page-form';

    if (isset($ajaxRendering) && $ajaxRendering) {
        $formid .= 'ajax';
    }

    $form = $this->beginWidget('CActiveForm', array(
        'id' => 'HomePage',
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

  
    <div class="buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord = Yii::t('app', 'Competition'),
            'value' => $model->isNewRecord = Yii::t('app', 'Competition')
        ));
        ?>    </div>
    
    <div class="buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord = Yii::t('app', 'Training'),
            'value' => $model->isNewRecord = Yii::t('app', 'Training')
        ));
        ?>    </div>

    <?php $this->endWidget(); ?>

    <div id="language_select_black">
        <?php
        $languages = Language::model()->findAll();
        foreach ($languages as $language) {
            ?>
            <a href="/index.php/HomePage/changeLanguage/?lang=<?php echo $language->short; ?>"><?php echo $language->short; ?></a>&nbsp;
            <?php
        }
        ?>
    </div>
    <div class="clearfix"></div>

</div><!-- form -->

