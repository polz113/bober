<?php
/* @var $this CompetitionQuestionController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Questions'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Competition Question'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Competition Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Questions'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
