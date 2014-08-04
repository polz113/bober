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
$nameColumn=$this->guessNameColumn($this->tableSchema->columns);
$label = $this->pluralize($this->class2name($this->modelClass));
echo "\$this->breadcrumbs = array(
	Yii::t('app', '$label') => array('index'),
	\$model->{$nameColumn} => array('view', 'id' => \$model->{$this->tableSchema->primaryKey}),
	Yii::t('app', 'update'),
);\n";
?>

$this->menu=array(
    array('label'=>Yii::t('app', 'Create <?php echo $this->class2name($this->modelClass); ?>'), 'url' => array('create')),
    array('label'=>Yii::t('app', 'View <?php echo $this->class2name($this->modelClass); ?>'), 'url' => array('view', 'id' => $model-><?php echo $this->tableSchema->primaryKey; ?>)),
    array('label'=>Yii::t('app', 'Manage <?php echo $this->pluralize($this->class2name($this->modelClass)); ?>'), 'url' => array('admin')),
);
?>

<h1><?php 

if ($nameColumn == $this->tableSchema->primaryKey)
{
    echo "<?php echo Yii::t('app', 'Update ".$this->class2name($this->modelClass)."'); ?> #<?php echo \$model->{$this->tableSchema->primaryKey}; ?>"; 
}
else
{
    echo "<?php echo Yii::t('app', 'Update ".$this->class2name($this->modelClass)."'); ?> \"<?php echo \$model->{$nameColumn}; ?>\""; 
}
?></h1>

<?php echo "<?php echo \$this->renderPartial('_form', array('model' => \$model)); ?>"; ?>