<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */

$this->breadcrumbs = array(
    Yii::t('app', 'Competition Users') => array('admin'),
    Yii::t('app', 'manage'),
);
$superuser = Generic::isSuperAdmin();
$create_competition_user = false;
$export_active_mentors = false;
$export_user_data = true;
$check_data = false;
$import_data = false;
$calculate_awards = false;
if ($superuser) {
    $create_competition_user = true;
    $export_active_mentors = true;
    $export_user_data = true;
    $check_data = true;
    $import_data = true;
    $calculate_awards = true;
}

$this->menu = array(
    array('label' => Yii::t('app', 'Manage Competition Users'), 'url' => array('admin')),
    array('label' => Yii::t('app', 'Create Competition User'), 'url' => array('create'), 'visible' => $create_competition_user),
    array('label' => Yii::t('app', 'Export Active Mentors'), 'url' => array('exportactivementor'), 'visible' => $export_active_mentors),
    array('label' => Yii::t('app', 'Export Competition User data'), 'url' => array('exportdata'), 'visible' => $export_user_data),
    array('label' => Yii::t('app', 'Check Competition User data'), 'url' => array('checkdata'), 'visible' => $check_data),
    array('label' => Yii::t('app', 'Import Competition User data'), 'url' => array('import'), 'visible' => $import_data),
    array('label' => Yii::t('app', 'Calculate awards for competitors'), 'url' => array('calculateawards'), 'visible' => $calculate_awards),
    array('label' => Yii::t('app', 'Calculate which competitors will advance to next level'), 'url' => array('calculateadvancingtonextlevel'), 'visible' => $calculate_awards),
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

<h1><?php echo Yii::t('app', 'Manage Competition Users'); ?></h1>
<?php /*
  <?php echo CHtml::link(Yii::t('app', 'advanced_search'), '#', array('class' => 'search-button')); ?>
  <div class="search-form" style="display:none">
  <?php $this->renderPartial('_search', array('model' => $model)); ?>
  </div><!-- search-form -->
 * 
 */
?>

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
          'label' => Yii::t('app', 'competitionUser_activated_click_to_deactivate'),
          'url' => 'Yii::app()->createUrl("/competitionUser/deactivate", array("id" => $data->id))'
          ),
          'inactive' => array(
          'visible' => '$data->active == 0',
          'imageUrl' => Yii::app()->theme->baseUrl.'/img/inactive.png',
          'options' => array('class' => 'activate'),
          'label' => Yii::t('app', 'competitionUser_deactivated_click_to_activate'),
          'url' => 'Yii::app()->createUrl("/competitionUser/activate", array("id" => $data->id))'
          ),

          )
          ),
         */
);

$lastColumns = array(
    'id', /*
      'competition_id',
      'competition_category_id',
      'user_id',
      'competition_category_school_mentor_id', */
    'last_name',
    'first_name',
    array(
        'name' => 'gender',
        'header' => Yii::t('app', 'Gender'),
        'value' => '$data->GetGenderName($data->gender)',
        'filter' => CHtml::dropDownList('CompetitionUser[gender]', $model->gender, $model->GetGender(true))
    ),
    'class',
    array(
        'name' => 'competition_name',
        'header' => Yii::t('app', 'Competition'),
        'value' => '$data->getCompetitionName()'
    ),
    array(
        'name' => 'competition_category_name',
        'header' => Yii::t('app', 'Competition Category'),
        'value' => '$data->getCompetitionCategoryName()'
    ),
    array(
        'name' => 'mentor_name',
        'header' => Yii::t('app', 'Mentor'),
        'value' => '$data->getMentorName()'
    ),
    /*
      'school_id', */
    array(
        'name' => 'disqualified_request',
        'value' => '$data->GetDisqualifiedName($data->disqualified_request)',
        'filter' => CHtml::dropDownList('CompetitionUser[disqualified_request]', $model->disqualified_request, $model->GetDisqualifiedOptions(true))
    ),
    /*
      'disqualified_request_by',
     */
    array(
        'name' => 'disqualified',
        'value' => '$data->GetDisqualifiedName($data->disqualified)',
        'filter' => CHtml::dropDownList('CompetitionUser[disqualified]', $model->disqualified, $model->GetDisqualifiedOptions(true))
    ),
    array(
        'name' => 'competition_results',
        'header' => Yii::t('app', 'Competition Results'),
        'value' => '$data->getCompetitionResults()',
        'filter' => false
    ),
    array(
        'name' => 'award',
        'value' => '$data->GetAwardName($data->award)',
        'filter' => CHtml::dropDownList('CompetitionUser[award]', $model->award, $model->GetAwardOptions(true)),
    ),
    array(
        'name' => 'advancing_to_next_level',
        'header' => Yii::t('app', 'Adv. to next level'),
        'value' => '$data->GetAdvancingToNextLevelName($data->advancing_to_next_level)',
        'filter' => CHtml::dropDownList('CompetitionUser[advancing_to_next_level]', $model->advancing_to_next_level, $model->GetAdvancingToNextLevelOptions(true))
    ),
    /*
      'disqualified_by',
      'disqualified_reason',
      'advancing_to_next_level',
      'award',
      'start_time',
      'finish_time',
      'finished',
      'total_points_via_answers',
      'total_points_via_time',
      'total_points_manual',
      'total_points',
     */
    array(
        'class' => 'CButtonColumn',
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
    /*
     $('#admin-grid .filters input').tooltip({
     'animation': true,
     'delay': {'show': 1000, 'hide': 250},
     'trigger': 'hover',
     'title': '<?php echo Yii::t('app', 'comparsion_operator_description'); ?>'
     });*/

    /* ]]> */
</script>