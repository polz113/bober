<?php
/* @var $this RegionController */
/* @var $model Region */
/* @var $form CActiveForm */
?>

<div class="wide form">

<?php $form=$this->beginWidget('CActiveForm', array(
	'action'=>Yii::app()->createUrl($this->route),
	'method'=>'get',
)); ?>
    
    <?php $superuser = User::model()->find('id=:id', array(':id' => Yii::app()->user->id))->superuser; ?>
	<div class="row">
		<?php echo $form->label($model, 'name'); ?>
		<?php echo $form->textField($model,'name',array('size'=>60,'maxlength'=>255)); ?>
	</div>

	<div class="row">
		<?php echo $form->label($model, 'country_id'); ?>
		<?php $data = Country::model()->GetCountriesICanEdit();
                      echo CHtml::activeDropDownList($model, 'country_id', CHtml::listData($data, 'id', 'country'), array('empty' => Yii::t('app', 'choose')));  ?>
	</div>

	<div class="row buttons">
        <br /><?php
        $this->widget('zii.widgets.jui.CJuiButton', array(
            'name' => 'button',
            'caption' => Yii::t('app', 'search'),
            'value' => Yii::t('app', 'search')
        ));
        ?>	</div>

<?php $this->endWidget(); ?>

</div><!-- search-form -->