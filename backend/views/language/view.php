<?php
/* @var $this LanguageController */
/* @var $model Language */

if (!$ajaxRendering)
{
    $this->breadcrumbs = array(
        Yii::t('app', 'languages')=>array('admin'),
        $model->name
    );

    $this->menu = array(
        array('label'=> Yii::t('app', 'manage_languages'), 'url' => array('admin')),
        array('label'=> Yii::t('app', 'create_language'), 'url' => array('create')),
        array('label'=> Yii::t('app', 'update_language'), 'url' => array('update', 'id' => $model->id)),
        array('label'=> Yii::t('app', 'delete_language'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id), 'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    );
    ?>

    <h1><?php echo Yii::t('app', 'language'); ?> "<?php echo $model->name; ?>"</h1>

<?php } ?>    

<?php echo $this->renderPartial('_form', array('model'=>$model, 'ajaxRendering' => false)); ?>

<script type="text/javascript">
    /* <![CDATA[ */
    $("#language-form :input, #language-formajax :input").attr('disabled', true);
    $("#language-form .hideWhenReadOnly, #language-formajax .hideWhenReadOnly").addClass('hidden');
    $("#language-form span.required, language-formajax span.required").addClass('hidden');    
    $("#language-form p.note, language-formajax p.note").addClass('hidden');
    /* ]]> */
</script>