<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $model CompetitionQuestionCategory */

$this->breadcrumbs=array(
	Yii::t('app', 'Competition Question Categories') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition Question Category'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Competition Question Category'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Competition Question Category'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Competition Question Categories'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Question Category'); ?> "<?php echo $model->id; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
	//	'id',
                array(
                    'name' => 'competiton_question_id',
                    'value' => $model->competitionQuestion->competition->name . ' - ' . $model->competitionQuestion->question->title,
                ),
                array(
                    'name' => 'competiton_category_id',
                    'value' => $model->competitionCategory->name,
                ),
                array(
                    'name' => 'competition_question_difficulty_id',
                    'value' => $model->competitionQuestionDifficulty->name,
                ),
	),
)); ?>
