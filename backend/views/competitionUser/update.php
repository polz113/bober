<?php
/* @var $this CompetitionUserController */
/* @var $model CompetitionUser */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Users') => array('index'),
	$model->id => array('view', 'id' => $model->id),
	Yii::t('app', 'update'),
);

$user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
$superuser = $user != null ? $user->superuser : 0;
$create_competition_user = false;
$delete_competition_user = false;
if ($superuser == 1) {
    $create_competition_user = true;
    $delete_competition_user = true;
}

$this->menu=array(
    array('label'=>Yii::t('app', 'Create Competition User'), 'url' => array('create'), 'visible' => $create_competition_user),
    array('label'=>Yii::t('app', 'View Competition User'), 'url' => array('view', 'id' => $model->id)),
    array('label'=>Yii::t('app', 'Manage Competition Users'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Update Competition User'); ?> #<?php echo $model->id; ?></h1>

<?php echo $this->renderPartial('_form', array('model' => $model)); ?>