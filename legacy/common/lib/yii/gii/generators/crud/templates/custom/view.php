<?php
/**
 * The following variables are available in this template:
 * - $this: the CrudCode object
 */
?>
<?php echo "<?php\n"; ?>
/* @var $this <?php echo $this->getControllerClass(); ?> */
/* @var $model <?php echo $this->getModelClass(); ?> */

<?php
$nameColumn = $this->guessNameColumn($this->tableSchema->columns);
$label = $this->pluralize($this->class2name($this->modelClass));
echo "\$this->breadcrumbs=array(
	Yii::t('app', '$label') => array('index'),
	\$model->{$nameColumn},
);\n";
?>

$this->menu=array(
    array('label'=>Yii::t('app', 'Create <?php echo $this->class2name($this->modelClass); ?>'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'Update <?php echo $this->class2name($this->modelClass); ?>'), 'url' => array('update', 'id' => $model-><?php echo $this->tableSchema->primaryKey; ?>)),
    array('label'=>Yii::t('app', 'Delete <?php echo $this->class2name($this->modelClass); ?>'), 'url' => '#', 'linkOptions' => array('submit' => array('delete', 'id' => $model-><?php echo $this->tableSchema->primaryKey; ?>),'confirm' => Yii::t('app', 'are_you_sure_you_want_to_delete_this_item'))),
    array('label'=>Yii::t('app' ,'Manage <?php echo $this->pluralize($this->class2name($this->modelClass)); ?>'), 'url' => array('admin')),
);
?>

<h1><?php echo "<?php echo Yii::t('app', '".$this->class2name($this->modelClass)."'); ?> \"<?php echo \$model->{$nameColumn}; ?>\""; ?></h1>

<?php echo "<?php"; ?> $this->widget('zii.widgets.CDetailView', array(
	'data' => $model,
	'attributes' => array(
<?php
foreach($this->tableSchema->columns as $column)
	echo "\t\t'".$column->name."',\n";
?>
	),
)); ?>
