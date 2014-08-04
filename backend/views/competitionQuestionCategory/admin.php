<?php
/* @var $this CompetitionQuestionCategoryController */
/* @var $model CompetitionQuestionCategory */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Question Categories') => array('admin'),
	Yii::t('app', 'manage'),
);

$this->menu = array(
	array('label'=> Yii::t('app', 'Create Competition Question Category'), 'url' => array('create')),
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

<h1><?php echo Yii::t('app', 'Manage Competition Question Categories');?></h1>

<?php echo CHtml::link(Yii::t('app', 'advanced_search'), '#', array('class' => 'search-button')); ?>
<div class="search-form" style="display:none">
<?php $this->renderPartial('_search', array('model' => $model)); ?>
</div><!-- search-form -->

<?php 

$superUserColumns = array();

/*
$superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; 
if ($superuser)
{
    $superUserColumns[] = array(
        'name' => 'company_search',
        'header' => Yii::t('app', 'company'), 
        'value' => '$data->company->name');
}
*/

$firstColumns = array(
/*
    array(
        'class'=>'CButtonColumn',
        'template' => '{active} {inactive}',
        'headerHtmlOptions' => array('style' => 'width: 20px'),
        'htmlOptions' => array('style' => 'width: 20px; text-align: center;'),
        'buttons' => array(
            'active' => array(
                'visible' => '$data->active == 1',
                'imageUrl' => Yii::app()->theme->baseUrl.'/img/active.png',
                'options' => array('class' => 'deactivate'),
                'label' => Yii::t('app', 'competitionQuestionCategory_activated_click_to_deactivate'),
                'url' => 'Yii::app()->createUrl("/competitionQuestionCategory/deactivate", array("id" => $data->id))'
            ),
            'inactive' => array(
                'visible' => '$data->active == 0',
                'imageUrl' => Yii::app()->theme->baseUrl.'/img/inactive.png',
                'options' => array('class' => 'activate'),
                'label' => Yii::t('app', 'competitionQuestionCategory_deactivated_click_to_activate'),
                'url' => 'Yii::app()->createUrl("/competitionQuestionCategory/activate", array("id" => $data->id))'
            ),

        )
    ),
*/
);

$lastColumns = array(
	//	'id',
                array(
                    'name' => 'competition_question_id',
                    'value' => '$data->GetCompetitionQuestionName()',
                ),
                array(
                    'name' => 'competition_category_search',
                    'header' => Yii::t('app','Competition Category'),
                    'value' => '$data->competitionCategory->name',
                ),
                array(
                    'name' => 'competition_question_difficulty_search',
                    'header' => Yii::t('app','Competition Question Difficulty'),
                    'value' => '$data->competitionQuestionDifficulty->name',
                ),
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
                )
            )
        )
    );

$columns = array_merge($firstColumns, $superUserColumns, $lastColumns);

$this->widget('zii.widgets.grid.CGridView', array(
	'id' => 'admin-grid',
	'dataProvider' => $model->search(),
	'filter' => $model,
	'columns' => $columns,
    'itemsCssClass' => 'table table-striped table-bordered table-condensed',
)); 
?>

<script type="text/javascript">
    /* <![CDATA[ */

    var gridUpdateFunction = function() {
        var th = this;

        $.fn.yiiGridView.update('admin-grid', {
                type: 'POST',
                url: $(this).attr('href'),
                success: function(data) {
                        $.fn.yiiGridView.update('admin-grid');
                },
                error: function(XHR) {
                }
        });
        
        return false;
    };
    
    // $('#admin-grid a.activate').live('click', gridUpdateFunction);
    // $('#admin-grid a.deactivate').live('click', gridUpdateFunction);

    $('#admin-grid .filters input').tooltip({
        'animation': true,
        'delay': { 'show': 1000, 'hide': 250 }, 
        'trigger': 'hover', 
        'title': '<?php echo Yii::t('app', 'comparsion_operator_description'); ?>'
    });
    
    /* ]]> */
</script>