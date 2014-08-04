<?php
/* @var $this SchoolMentorController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentors'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create School Mentor'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage School Mentors'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Mentors'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
