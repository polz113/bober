<?php
/* @var $this SchoolController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Schools'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create School'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Schools'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Schools'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
