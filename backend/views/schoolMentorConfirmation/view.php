<?php
/* @var $this SchoolMentorConfirmationController */
/* @var $model SchoolMentorConfirmation */

$this->breadcrumbs=array(
	Yii::t('app', 'School Mentor Confirmations') => array('index'),
	$model->id,
);

$this->menu=array(
    array('label'=>Yii::t('app', 'Create School Mentor Confirmation'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update School Mentor Confirmation'), 'url' => array('update', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Delete School Mentor Confirmation'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage School Mentor Confirmations'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'School Mentor Confirmation'); ?> "<?php echo $model->id; ?>"</h1>

<?php $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
		'id',
		'school_id',
		'user_id',
		'active',
		'activated_by',
		'activated_timestamp',
		'coordinator',
	),
)); ?>
