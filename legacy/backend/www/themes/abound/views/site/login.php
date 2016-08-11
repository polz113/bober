<?php
/* @var $this SiteController */
/* @var $model LoginForm */
/* @var $form CActiveForm  */

$this->breadcrumbs = array();
?>

<div style="width:305px; margin: auto; margin-top:75px">
    <?php
    $this->beginWidget('zii.widgets.CPortlet', array(
        'title' => Yii::t('app', 'login'),
    ));
    ?>
    <style type="text/css" scoped="scoped">
        div.errorMessage { display: block; }
        div.container-fluid { min-width: 400px; }
    </style>
    <div class="form" style="margin: 10px;">
        <?php
        $form = $this->beginWidget('CActiveForm', array(
            'id' => 'login-form',
            'enableClientValidation' => true,
            'clientOptions' => array(
                'validateOnSubmit' => true,
            ),
            'action' => '/index.php/site/index',
            'htmlOptions' => array('style' => 'margin-bottom: 10px')
        ));
        ?>

        <div class="row">
            <?php echo $form->labelEx($model, 'username'); ?>
            <?php echo $form->textField($model, 'username', array('style' => 'width: 260px')); ?>
<?php echo $form->error($model, 'username'); ?>
        </div>

        <div class="row">
            <?php echo $form->labelEx($model, 'password'); ?>
            <?php echo $form->passwordField($model, 'password', array('style' => 'width: 260px')); ?>
<?php echo $form->error($model, 'password'); ?>
        </div>

        <div class="row rememberMe">
            <?php echo $form->checkBox($model, 'rememberMe'); ?>
            <?php echo $form->label($model, 'rememberMe', array('style' => 'display: inline; vertical-align: middle')); ?>
<?php echo $form->error($model, 'rememberMe'); ?>
        </div>

        <div class="row buttons" style="padding-top: 10px; margin-bottom: 0px; text-align: center;">
<?php echo CHtml::submitButton(Yii::t('app', 'login'), array('class' => 'btn btn btn-primary', 'style' => 'margin: auto; margin-top: 10px;')); ?>
        </div>

<?php $this->endWidget(); ?>
    </div><!-- form -->

<?php $this->endWidget(); ?>


</div>