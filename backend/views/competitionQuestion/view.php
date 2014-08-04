<?php
/* @var $this CompetitionQuestionController */
/* @var $model CompetitionQuestion */

$this->breadcrumbs=array(
	Yii::t('app', 'Competition Questions') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Question'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Competition Question'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Competition Question'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Competition Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Question'); ?> "<?php echo $model->id; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
	//	'id',
                array(
                    'name' => 'competition_id',
                    'value' => $model->competition->name,
                ),
                array(
                    'name' => 'question_id',
                    'value' => $model->question->title,
                ),
	),
)); ?>
