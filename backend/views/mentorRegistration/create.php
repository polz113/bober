
<?php
/* @var $this StartCompetitionController */
/* @var $model StartCompetition */
?>

<h1><?php echo Yii::t('app', 'Mentor Registration'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model, 'profile' => $profile, 'school_mentor' => $school_mentor)); ?> 