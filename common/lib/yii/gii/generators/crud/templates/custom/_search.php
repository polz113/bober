<?php
/**
 * The following variables are available in this template:
 * - $this: the CrudCode object
 */
?>
<?php echo "<?php\n"; ?>
/* @var $this <?php echo $this->getControllerClass(); ?> */
/* @var $model <?php echo $this->getModelClass(); ?> */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php echo "<?php \$form=\$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl(\$this->route),
	'method'=>'get',
)); ?>\n"; ?>
    
    <?php echo "<?php \$superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>"; ?>

<?php foreach($this->tableSchema->columns as $column): ?>
<?php
    if ($column == $this->tableSchema->primaryKey)
    {
        continue;
    }

	$field = $this->generateInputField($this->modelClass, $column);
	
    if(strpos($field, 'password') !== false)
    {
		continue;
    }
?>
	<div class="row">
		<?php echo "<?php echo \$form->label(\$model, '{$column->name}'); ?>\n"; ?>
		<?php echo "<?php echo ".$this->generateActiveField($this->modelClass, $column)."; ?>\n"; ?>
	</div>

<?php endforeach; ?>
	<div class="row buttons">
        <?php
        echo "<br /><?php
        \$this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => Yii::t('app', 'search'),
            'value' => Yii::t('app', 'search')
        ));
        ?>";
        ?>
	</div>

<?php echo "<?php \$this->endWidget(); ?>\n"; ?>

</div><!-- search-form -->