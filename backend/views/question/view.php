<?php
/* @var $this QuestionController */
/* @var $model Question */

$this->breadcrumbs=array(
	Yii::t('app', 'Questions') => array('index'),
	$model->title,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Question'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Question'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Questions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Question'); ?> "<?php echo $model->title; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		
		array(
                    'name' => 'country_id',
                    'value' => $model->country->country,
                ),
                'identifier',
		array(
                    'name' => 'type',
                    'value' => $model->GetQuestionTypeName($model->type) ,
                    
                ),
		'title',
		'text',
		'data',
		'version',
	//	'verification_function_type',
                array(
                    'name' => 'verification_function_type',
                    'value' => $model->GetVerificationFunctionTypeName($model->verification_function_type),
                ),
		'verification_function',
		'last_change_date',
		'authors',
                'css'
	),
)); ?>
