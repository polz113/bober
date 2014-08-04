<?php
/* @var $this RegionController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Regions'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Region'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Regions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Regions'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
