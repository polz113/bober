<li class="span4">
    <div class="thumbnail">
      <img src="http://placehold.it/300x200" alt="">
      <h3>Thumbnail label</h3>
      <p>Thumbnail caption...</p>
    </div>

	<b><?php echo CHtml::encode($data->getAttributeLabel('pesonal_info_id')); ?>:</b>
	<?php echo CHtml::link(CHtml::encode($data->pesonal_info_id),array('view','id'=>$data->pesonal_info_id)); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('custom_id')); ?>:</b>
	<?php echo CHtml::encode($data->custom_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('first_name')); ?>:</b>
	<?php echo CHtml::encode($data->first_name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('last_name')); ?>:</b>
	<?php echo CHtml::encode($data->last_name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('phone_home')); ?>:</b>
	<?php echo CHtml::encode($data->phone_home); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('phone_work')); ?>:</b>
	<?php echo CHtml::encode($data->phone_work); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('phone_mobile')); ?>:</b>
	<?php echo CHtml::encode($data->phone_mobile); ?>
	<br />

	<?php /*
	<b><?php echo CHtml::encode($data->getAttributeLabel('fax')); ?>:</b>
	<?php echo CHtml::encode($data->fax); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('email_primary')); ?>:</b>
	<?php echo CHtml::encode($data->email_primary); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('email_secondary')); ?>:</b>
	<?php echo CHtml::encode($data->email_secondary); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('address_1')); ?>:</b>
	<?php echo CHtml::encode($data->address_1); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('address_2')); ?>:</b>
	<?php echo CHtml::encode($data->address_2); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('address_3')); ?>:</b>
	<?php echo CHtml::encode($data->address_3); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('country')); ?>:</b>
	<?php echo CHtml::encode($data->country); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('gender')); ?>:</b>
	<?php echo CHtml::encode($data->gender); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('marital_status')); ?>:</b>
	<?php echo CHtml::encode($data->marital_status); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('dob')); ?>:</b>
	<?php echo CHtml::encode($data->dob); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('date_joined')); ?>:</b>
	<?php echo CHtml::encode($data->date_joined); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('date_left')); ?>:</b>
	<?php echo CHtml::encode($data->date_left); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('middle_name')); ?>:</b>
	<?php echo CHtml::encode($data->middle_name); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('national_id')); ?>:</b>
	<?php echo CHtml::encode($data->national_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('passport_number')); ?>:</b>
	<?php echo CHtml::encode($data->passport_number); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('drivers_license')); ?>:</b>
	<?php echo CHtml::encode($data->drivers_license); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('other_id')); ?>:</b>
	<?php echo CHtml::encode($data->other_id); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('other_id_2')); ?>:</b>
	<?php echo CHtml::encode($data->other_id_2); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('nationality')); ?>:</b>
	<?php echo CHtml::encode($data->nationality); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('ethnic_race')); ?>:</b>
	<?php echo CHtml::encode($data->ethnic_race); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('smoker')); ?>:</b>
	<?php echo CHtml::encode($data->smoker); ?>
	<br />

	<b><?php echo CHtml::encode($data->getAttributeLabel('status')); ?>:</b>
	<?php echo CHtml::encode($data->status); ?>
	<br />

	*/ ?>

</li>