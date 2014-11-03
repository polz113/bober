
<?php
/* @var $this StartCompetitionController */
/* @var $model CompetitionUser */
?>

<h1><?php echo Yii::t('app', 'Start Competition'); ?> </h1>
<div class ="view">
    <div class="row" style="text-align: center;">
        <p><?php echo Yii::t('app', 'The duration of the competition'); ?>: <strong><?php echo $model->competition->duration; ?> <?php echo Yii::t('app', 'minutes'); ?></strong></p>
    </div>
    <div class="row" style="text-align: center;">
        <p><?php echo Yii::t('app', 'Competition Category'); ?>: <strong><?php echo $model->competitionCategory->name; ?></strong></p>
    </div>
    <?php
    if ($model->start_time != null) {
        $duration = $model->competition->duration * 60;
        $timeLeft = number_format(($duration - (time() - strtotime($model->start_time))) / 60.0, 2, '.', '');
        ?>
        <div class="row">
            <p><?php echo Yii::t('app', 'Time left for competition'); ?>: <?php echo $timeLeft ?> <?php echo Yii::t('app', 'minutes'); ?></p>
        </div>
        <?php
    }
    ?>
    <div class="buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => $model->isNewRecord = Yii::t('app', 'Start Competition'),
            'value' => $model->isNewRecord = Yii::t('app', 'Start Competition'),
            'onclick' => new CJavaScriptExpression('function() {window.location = "/index.php/CompetitionLoader";}')
        ));
        ?> 
    </div>
</div>

<?php /* $this->widget('zii.widgets.CDetailView', array(
  'data' => $model,
  'attributes' => array(
  'id',
  'competition_id',
  'competition_category_id',
  'user_id',
  'competition_category_school_mentor_id',
  'last_name',
  'first_name',
  'class',
  'school_id',
  'disqualified_request',
  'disqualified_request_by',
  'disqualified',
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
  ),
  )); */ ?>
