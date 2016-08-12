<?php
/* @var $this CompetitionCategoryController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Categories'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Competition Category'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Competition Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Categories'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
