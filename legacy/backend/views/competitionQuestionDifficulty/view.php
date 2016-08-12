<?php
/* @var $this CompetitionQuestionDifficultyController */
/* @var $model CompetitionQuestionDifficulty */

$this->breadcrumbs=array(
	Yii::t('app', 'Question Difficulties') => array('index'),
	$model->name,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question Difficulty'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Question Difficulty'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Question Difficulty'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Question Difficulties'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Question Difficulty'); ?> "<?php echo $model->name; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		array(
                    'name' => 'active',
                    'value' => $model->active == 1 ? Yii::t('app', 'yes') : Yii::t('app', 'no')
                ),
                array(
                    'name' => 'country_id',
                    'value' => $model->country->country
                ),
		'name',
		'correct_answer_points',
		'wrong_answer_points',
	),
)); ?>
