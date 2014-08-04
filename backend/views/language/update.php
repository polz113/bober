<?php
/* @var $this LanguageController */
/* @var $model Language */

if (!$ajaxRendering)
{
    $this->breadcrumbs=array(
        Yii::t('app', 'languages') => array('admin'),
        $model->name => array('view','id' => $model->id),
        Yii::t('app', 'update'),
    );

    $this->menu=array(
        array('label'=> Yii::t('app', 'manage_languages'), 'url' => array('admin')),
        array('label'=> Yii::t('app', 'create_language'), 'url' => array('create')),
        array('label'=> Yii::t('app', 'delete_language'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id), 'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    );
    ?>

    <h1><?php echo Yii::t('app', 'update_language'); ?> "<?php echo $model->name; ?>"</h1>

<?php } ?>

<?php echo $this->renderPartial('_form', array('model'=>$model, 'ajaxRendering' => $ajaxRendering)); ?>