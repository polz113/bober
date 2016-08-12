<?php
$this->breadcrumbs = array(
    Yii::t('app', 'Shared files') => array('index'),
);

$this->menu = array(
    array('label' => Yii::t('app', 'Manage shared files'), 'url' => array('index')),
);
?>

<h1><?php echo Yii::t('app', 'Manage shared files'); ?></h1>

<?php
$this->widget('zii.widgets.grid.CGridView', array(
    'id' => 'admin-grid',
    'dataProvider' => new CArrayDataProvider($list),
    'columns' => array(
        array(
            'name' => 'name',
            'header' => Yii::t('app', 'File name'),
            'value' => '$data["name"]',
            'filter' => false,
        ),
        array(
            'name' => 'title',
            'header' => Yii::t('app', 'Download'),
            'urlExpression'=>'array("/shared/get","key"=>$data["key"])',
            'class'=>'YDataLinkColumn',
            'filter' => false,
        ),
    ),
    'itemsCssClass' => 'table table-striped table-bordered table-condensed',
));
?>