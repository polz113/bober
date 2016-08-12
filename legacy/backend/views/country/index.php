<?php
/* @var $this CountryController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Countries'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Country'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Countries'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Countries'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
