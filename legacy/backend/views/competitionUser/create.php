<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Users') => array('admin'),
	Yii::t('app', 'create'),
);

$user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
$superuser = $user != null ? $user->superuser : 0;
$create_competition_user = false;
$export_active_mentors = false;
$export_user_data = false;
$check_data = false;
$import_data = false;
if ($superuser) {
    $create_competition_user = true;
    $export_active_mentors = true;
    $export_user_data = true;
    $check_data = true;
    $import_data = true;
}

$this->menu = array(
    array('label' => Yii::t('app', 'Manage Competition Users'), 'url' => array('admin')),
    array('label' => Yii::t('app', 'Create Competition User'), 'url' => array('create'), 'visible' => $create_competition_user),
    array('label' => Yii::t('app', 'Export Active Mentors'), 'url' => array('exportactivementor'), 'visible' => $export_active_mentors),
    array('label' => Yii::t('app', 'Export Competition User data'), 'url' => array('exportdata'), 'visible' => $export_user_data),
    array('label' => Yii::t('app', 'Check Competition User data'), 'url' => array('checkdata'), 'visible' => $check_data),
    array('label' => Yii::t('app', 'Import Competition User data'), 'url' => array('import'), 'visible' => $import_data),
);
?>

<h1><?php echo Yii::t('app', 'Create Competition User'); ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>