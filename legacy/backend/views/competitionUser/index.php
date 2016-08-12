<?php
/* @var $this CompetitionUserController */
/* @var $dataProvider CActiveDataProvider */

$this->breadcrumbs = array(
	Yii::t('app', 'Competition Users'),
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
    array('label' => Yii::t('app', 'Create Competition User'), 'url' => array('create'), 'visible' => $create_competition_user),
    array('label' => Yii::t('app', 'Manage Competition Users'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Competition Users'); ?></h1>

<?php $this->widget('zii.widgets.CListView', array(
	'dataProvider' => $dataProvider,
	'itemView' => '_view',
)); ?>
