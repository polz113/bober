<?php
/* @var $this SchoolCategoryController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'School Categories'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create School Category'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage School Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Categories'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
