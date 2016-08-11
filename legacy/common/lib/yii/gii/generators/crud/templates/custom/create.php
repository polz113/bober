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
$label = $this->pluralize($this->class2name($this->modelClass));
echo "\$this->breadcrumbs = array(
	Yii::t('app', '$label') => array('admin'),
	Yii::t('app', 'create'),
);\n";
?>

$this->menu=array(
	array('label' => Yii::t('app', 'Manage <?php echo $this->pluralize($this->class2name($this->modelClass)); ?>'), 'url' => array('admin')),
);
?>

<h1><?php echo "<?php echo Yii::t('app', 'Create ".$this->class2name($this->modelClass)."'); ?>"; ?></h1>

<?php echo "<?php echo \$this->renderPartial('_form', array('model' => \$model)); ?>"; ?>
