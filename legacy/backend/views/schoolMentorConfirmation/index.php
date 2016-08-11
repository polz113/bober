<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'School Mentor Confirmations'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create School Mentor Confirmation'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage School Mentor Confirmations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Mentor Confirmations'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
