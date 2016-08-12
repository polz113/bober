<?php
/* @var $this QuestionController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Questions'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Question'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Questions'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
