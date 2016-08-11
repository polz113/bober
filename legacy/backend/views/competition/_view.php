<?php
/* @var $this CompetitionController */
/* @var $data Competition */
?>

<div class="view">

    <b><?php echo CHtml::encode($data->getAttributeLabel('id')); ?>:</b>
    <?php echo CHtml::link(CHtml::encode($data->id), array('view', 'id' => $data->id)); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('name')); ?>:</b>
    <?php echo CHtml::encode($data->name); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('active')); ?>:</b>
    <?php echo CHtml::encode($data->active); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('timestamp_start')); ?>:</b>
    <?php echo CHtml::encode($data->timestamp_start); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('timestamp_stop')); ?>:</b>
    <?php echo CHtml::encode($data->timestamp_stop); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('type')); ?>:</b>
    <?php echo CHtml::encode($data->type); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('public_access')); ?>:</b>
    <?php echo CHtml::encode($data->public_access); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('duration')); ?>:</b>
    <?php echo CHtml::encode($data->duration); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('timestamp_mentor_results')); ?>:</b>
    <?php echo CHtml::encode($data->timestamp_mentor_results); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('timestamp_mentor_awards')); ?>:</b>
    <?php echo CHtml::encode($data->timestamp_mentor_awards); ?>
    <br />

    <b><?php echo CHtml::encode($data->getAttributeLabel('timestamp_mentor_advancing_to_next_level')); ?>:</b>
    <?php echo CHtml::encode($data->timestamp_mentor_advancing_to_next_level); ?>
    <br />


</div>