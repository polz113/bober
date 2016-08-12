<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Question Categories'),
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Competition Question Category'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Manage Competition Question Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Question Categories'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
