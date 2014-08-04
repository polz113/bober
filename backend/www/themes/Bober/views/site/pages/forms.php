<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name . ' - Forms';
$this->breadcrumbs=array(
	'Forms',
);
?>

<div class="page-header">
	<h1>Forms</h1>
</div>

<div class="row-fluid">
  <div class="span6">
  
<?php
	$this->beginWidget('zii.widgets.CPortlet', array(
		'title'=>"Text fields",
	));
	
?>
<?php
echo(CHtml::beginForm());

echo(CHtml::label('Normal field', 'name'));
echo(CHtml::textField('name'));

echo(CHtml::label('Password input', 'name'));
echo(CHtml::passwordField('name'));

echo(CHtml::label('With placeholder', 'name'));
echo(CHtml::textField('name', 'this is placeholder text'));

echo(CHtml::label('Read only field', 'name'));
echo(CHtml::textField('name','',array('readonly'=>'readonly')));

echo(CHtml::label('Disabled field', 'name'));
echo(CHtml::textField('name','',array('disabled'=>'disabled')));

echo(CHtml::label('Max lenght', 'name'));
echo(CHtml::textField('name','Max length is 10',array('maxlength'=>'10')));
	
echo '<div class="input-prepend">';
echo(CHtml::label('Prepended text', 'name'));
echo '<span class="add-on">$</span>';
echo(CHtml::textField('name'));
echo '</div>';

echo '<div class="input-append">';
echo(CHtml::label('Append text', 'name'));
echo(CHtml::textField('name'));
echo '<span class="add-on">.00</span>';
echo '</div>';

echo(CHtml::endForm());
?>

<?php $this->endWidget();?>

    </div>
    <div class="span6">
    <?php
	$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Text fields",
		));
		
	?>
    <?php
    echo(CHtml::label('List box', 'name'));
	echo(CHtml::listBox('name','',array('1'=>'One','2'=>'Two','3'=>'Three','4'=>'Four','5'=>'Five')));
	
	echo(CHtml::label('Text Area', 'name'));
	echo(CHtml::textArea('name'));
	
	echo(CHtml::label('File field', 'name'));
	echo(CHtml::fileField('name','',array('class'=>'btn')));
	
	echo(CHtml::label('Radio button', 'name'));
	echo(CHtml::radioButton('name'));
	
	echo '<br><br>';
	
	echo(CHtml::label('Check box', 'name'));
	echo(CHtml::checkBox('name'));

	?>
    <?php $this->endWidget();?>
    </div>
</div>

<div class="row-fluid">
  	<div class="span12">
    <?php
	$this->beginWidget('zii.widgets.CPortlet', array(
		'title'=>"Control sizing - Block level inputs",
	));
	
	?>
    <p>
    Make any <code>&lt;input&gt;</code> or <code>&lt;textarea&gt;</code> element behave like a block level element.
    </p>
    <?php
	echo(CHtml::textField('name','.input-block-level',array('class'=>'input-block-level')));
	echo(CHtml::textArea('name','.input-block-level',array('class'=>'input-block-level','rows'=>'6')));
	?>
    
    <?php $this->endWidget();?>
    </div>
</div>

<div class="row-fluid">
  	<div class="span12">
    <?php
	$this->beginWidget('zii.widgets.CPortlet', array(
		'title'=>"Control sizing - Relative sizing",
	));
	
	?>
    <p>Use relative sizing classes like <code>.input-large</code> or match your inputs to the grid column sizes using <code>.span*</code> classes.</p>
    <?php
	echo(CHtml::textField('name','.input-mini',array('class'=>'input-mini')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.input-small',array('class'=>'input-small')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.input-medium',array('class'=>'input-medium')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.input-large',array('class'=>'input-large')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.input-xlarge',array('class'=>'input-xlarge')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.input-xxlarge',array('class'=>'input-xxlarge')));
	?>
    
    <?php $this->endWidget();?>
    </div>
</div>
<div class="row-fluid">

    <?php
	$this->beginWidget('zii.widgets.CPortlet', array(
		'title'=>"Control sizing - Grid sizing",
	));
	
	?>
    <p>Use <code>.span1</code> to <code>.span12</code> for inputs that match the same sizes of the grid columns.</p>
    
    <?php
	echo(CHtml::textField('name','.span1',array('class'=>'span1')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span2',array('class'=>'span2')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span3',array('class'=>'span3')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span4',array('class'=>'span4')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span5',array('class'=>'span5')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span6',array('class'=>'span6')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span7',array('class'=>'span7')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span8',array('class'=>'span8')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span9',array('class'=>'span9')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span10',array('class'=>'span10')));
	?>
    <br /><?php
	echo(CHtml::textField('name','.span11',array('class'=>'span11')));
	?>
    <br />
	<?php
	echo(CHtml::textField('name','.span12',array('class'=>'span12')));
	?>
    
  <p>For multiple grid inputs per line, <strong>use the <code>.controls-row</code> modifier class for proper spacing</strong>. It floats the inputs to collapse white-space, sets the proper margins, and the clears the float.</p>

    
<div class="controls-row">
    <?php
	echo(CHtml::textField('name','.span5',array('class'=>'span5')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span4',array('class'=>'span4'))); 
	echo(CHtml::textField('name','.span1',array('class'=>'span1')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span3',array('class'=>'span3'))); 
	echo(CHtml::textField('name','.span2',array('class'=>'span2')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span2',array('class'=>'span2'))); 
	echo(CHtml::textField('name','.span3',array('class'=>'span3')));
	?>
    <br />
    <?php
	echo(CHtml::textField('name','.span1',array('class'=>'span1'))); 
	echo(CHtml::textField('name','.span4',array('class'=>'span4')));
	?>
</div>
    
    <pre>&lt;div class=&quot;controls-row&quot;&gt;<br />    &lt;?php<br />	echo(CHtml::textField('name','.span5',array('class'=&gt;'span5')));<br />	?&gt;<br />    &lt;br /&gt;<br />    &lt;?php<br />	echo(CHtml::textField('name','.span4',array('class'=&gt;'span4'))); <br />	echo(CHtml::textField('name','.span1',array('class'=&gt;'span1')));<br />	?&gt;<br />    &lt;br /&gt;<br />    &lt;?php<br />	echo(CHtml::textField('name','.span3',array('class'=&gt;'span3'))); <br />	echo(CHtml::textField('name','.span2',array('class'=&gt;'span2')));<br />	?&gt;<br />    &lt;br /&gt;<br />    &lt;?php<br />	echo(CHtml::textField('name','.span2',array('class'=&gt;'span2'))); <br />	echo(CHtml::textField('name','.span3',array('class'=&gt;'span3')));<br />	?&gt;<br />    &lt;br /&gt;<br />    &lt;?php<br />	echo(CHtml::textField('name','.span1',array('class'=&gt;'span1'))); <br />	echo(CHtml::textField('name','.span4',array('class'=&gt;'span4')));<br />	?&gt;<br />&lt;/div&gt;</pre>

    <?php $this->endWidget();?>

</div>