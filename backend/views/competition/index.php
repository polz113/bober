<?php
/* @var $this CompetitionController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competitions'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Competition'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Competitions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competitions'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
