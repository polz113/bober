<?php
/* @var $this RegionController */
/* @var $model Region */

$this->breadcrumbs=array(
	Yii::t('app', 'Regions') => array('index'),
	$model->name,
);

$this->menu=array(
    array('label' => Yii::t('app', 'Create Region'), 'url' => array('create')),
    array('label' => Yii::t('app', 'Update Region'), 'url' => array('update', 'id' => $model->id)),
    array('label' => Yii::t('app', 'Delete Region'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model->id),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label' => Yii::t('app', 'Manage Regions'), 'url' => array('admin')),
);
?>

<h1><?php echo Yii::t('app', 'Region'); ?> "<?php echo $model->name; ?>"</h1>

<?php
$this->widget('zii.widgets.CDetailView', array(
    'data' => $model,
    'attributes' => array(
        //	'id',
        'name',
        array(
            'name' => Yii::t('app', 'country_id'),
            'value' => $model->country->country
        ),
    ),
));
?>
