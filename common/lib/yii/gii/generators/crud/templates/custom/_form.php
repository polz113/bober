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

<div class="form">

<?php 



echo "<?php 
\$formid = '".$this->class2id($this->modelClass)."-form';

if (isset(\$ajaxRendering) && \$ajaxRendering)
{
    \$formid .= 'ajax';
}    

\$form=\$this->beginWidget('CActiveForm', array(
	'id'=>'\$formid',
	'enableAjaxValidation'=>false,
)); ?>\n"; ?>
    
    <?php echo "<?php \$superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>"; ?>

    <?php // if (!$ajaxRendering) { ?>
	<p class="note"><?php echo "<?php echo Yii::t('app', 'fields_with'); ?>"; ?> <span class="required">*</span> <?php echo "<?php echo Yii::t('app', 'are_required'); ?>"; ?>.</p>
    <?php //} ?>

	<?php echo "<?php echo \$form->errorSummary(\$model); ?>\n"; ?>

<?php
foreach($this->tableSchema->columns as $column)
{
	if($column->autoIncrement)
		continue;
?>
	<div class="row">
		<?php echo "<?php echo ".$this->generateActiveLabel($this->modelClass, $column)."; ?>\n"; ?>
		<?php echo "<?php echo ".$this->generateActiveField($this->modelClass, $column)."; ?>\n"; ?>
		<?php echo "<?php echo \$form->error(\$model, '{$column->name}'); ?>\n"; ?>
	</div>

<?php
}
?>
    <?php //if (!$ajaxRendering) { ?>

    <div class="row buttons">
		<?php 
        echo "<br /><?php
        \$this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => \$model->isNewRecord ? Yii::t('app', 'create') : Yii::t('app', 'save'),
            'value' => \$model->isNewRecord ? Yii::t('app', 'create') : Yii::t('app', 'save')
        ));
        ?>";
        // echo "<?php echo CHtml::submitButton(\$model->isNewRecord ? Yii::t('app', 'create') : Yii::t('app', 'save'));
        ?>
	</div>
    <?php //} ?>

<?php echo "<?php \$this->endWidget(); ?>\n"; ?>

</div><!-- form -->