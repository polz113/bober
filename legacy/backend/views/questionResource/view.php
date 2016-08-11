<?php
/* @var $this QuestionResourceController */
/* @var $model QuestionResource */

$this->breadcrumbs=array(
	Yii::t('app', 'Question Resources') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Question Resource'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update Question Resource'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete Question Resource'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage Question Resources'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Question Resource'); ?> "<?php echo $model->id; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
	//	'id',
                array(
                    'name' => 'question_id',
                    'value' => $model->GetQuestionTitleId($model->question_id),
                ),
                array(
                    'name' => 'language_id',
                    'value' => $model->language->name,
                ),      
                array(
                    'name' => 'type',
                    'value' => $model->GetResourceTypeName($model->type),
                ),
		'filename',
		'file_type',
                array(
                    'name' => 'size',
                    'value' => $model->GetSize($model->data),
                ),
          //    'start_up',
	),
)); ?>
