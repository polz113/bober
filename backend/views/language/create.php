<?php
/* @var $this LanguageController */
/* @var $model Language */

if (!$ajaxRendering)
{
    $this->breadcrumbs=array(
        Yii::t('app', 'languages')=>array('admin'),
        Yii::t('app', 'create'),
    );

    $this->menu=array(
        array('label'=> Yii::t('app', 'manage_languages'), 'url'=>array('admin')),
    );
    ?>

    <h1><?php echo Yii::t('app', 'create_language') ?></h1>

<?php } ?>

<?php echo $this->renderPartial('_form', array('model'=>$model, 'ajaxRendering' => $ajaxRendering)); ?>