
<?php
/* @var $this StartCompetitionController */
/* @var $dataProvider CActiveDataProvider */

?>

<h1><?php echo Yii::t('app', 'Start Competitions'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
    'dataProvider' => $dataProvider,
    'itemView' => '_view',
)); ?>