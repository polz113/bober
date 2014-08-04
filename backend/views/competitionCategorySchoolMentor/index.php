<?php
/* @var $this CompetitionCategorySchoolMentorController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Register Competitors For Competition'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Register Competitors'), 'url' => array('create')),
    array('label' => Yii::t('app', 'All Competitors Registrations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competitors Registrations'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
