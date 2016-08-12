<?php
/* @var $this CountryAdministratorController */
/* @var $model CountryAdministrator */
/* @var $form CActiveForm */
?>

<div class="form">

    <?php
    $formid = 'country-administrator-form';

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
        <?php echo $form->labelEx($model, 'country_id'); ?>
        <?php
        $data = Country::model()->findAll();
        echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'country_id'); ?>
    </div>

    <div class="row">
        <?php echo $form->labelEx($model, 'user_id'); ?>
        <?php
        $data = User::model()->with('profile')->findAll(array('condition' => 'profile.user_role>=:user_role', 'params' => array(':user_role' => 10), 'order' => 'profile.last_name ASC, profile.first_name ASC'));
        $user_list = array();
        foreach ($data as $dataUser) {
            $user_list[$dataUser->id] = $dataUser->profile->last_name .' '.$dataUser->profile->first_name;
        }
        echo CHtml::activeDropDownList($model, 'user_id', $user_list, array('empty' => Yii::t('app', 'choose')));
        ?>
<?php echo $form->error($model, 'user_id'); ?>
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