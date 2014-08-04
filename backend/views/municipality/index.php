<?php
/* @var $this MunicipalityController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Municipalities'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Municipality'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Municipalities'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Municipalities'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
