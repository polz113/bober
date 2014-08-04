<?php
/* @var $this CompetitionCategorySchoolController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Category Schools'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Competition Category School'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Competition Category Schools'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Category Schools'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
