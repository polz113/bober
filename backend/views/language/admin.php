<?php
/* @var $this LanguageController */
/* @var $model Language */

$this->breadcrumbs=array(
	Yii::t('app', 'languages')=>array('admin'),
	Yii::t('app', 'manage'),
);

$this->menu=array(
	array('label'=> Yii::t('app', 'create_language'), 'url'=>array('create')),
);


Yii::app()->clientScript->registerScript('search', "
$('.search-button').click(function(){
	$('.search-form').toggle();
	return false;
});
$('.search-form form').submit(function(){
	$.fn.yiiGridView.update('admin-grid', {
		data: $(this).serialize()
	});
	return false;
});
");
?>


<h1><?php echo Yii::t('app', 'manage_languages') ?></h1>



<?php echo CHtml::link(Yii::t('app', 'advanced_search'),'#',array('class'=>'search-button')); ?>

<div class="search-form" style="display:none">
<?php $this->renderPartial('_search',array(
	'model'=>$model,
)); ?>
</div><!-- search-form -->

<?php $this->widget('zii.widgets.grid.CGridView', array(
	'id'=>'admin-grid',
	'dataProvider'=>$model->search(),
	'filter'=>$model,
    'itemsCssClass' => 'table table-striped table-bordered table-condensed',
	'columns'=>array(
		'name',
		'short',
		array(
			'class'=>'CButtonColumn',
            'buttons' => array(
                'view' => array(
                    'visible' => '$data->CanView'
                ),
                'update' => array(
                    'visible' => '$data->CanUpdate'
                ),
                'delete' => array(
                    'visible' => '$data->CanDelete'
                ),
            )
		),
	),
)); ?>
