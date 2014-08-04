<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name . ' - Interface Elements';
$this->breadcrumbs=array(
	'Interface Elements',
);
?>
<?php

$sample_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
?>
<div class="page-header">
	<h1>Interface elements</h1>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiAccordion",
		));
		
	?>
    <?php
    $this->widget('zii.widgets.jui.CJuiAccordion', array(
		'panels'=>array(
			'panel 1'=>$sample_text,
			'panel 2'=>$sample_text,
			'panel 3'=>$sample_text,
			'panel 4'=>$sample_text,
			// panel 5 contains the content rendered by a partial view
			//'panel 5'=>$this->renderPartial('_partial',null,true),
		),
		// additional javascript options for the accordion plugin
		'options'=>array(
			'animated'=>'bounceslide',
		),
	));
	?>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML accordion",
		));
		
	?>
    <div class="accordion" id="accordion2">
      <div class="accordion-group">
        <div class="accordion-heading">
          <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseOne">
            Collapsible Group Item #1
          </a>
        </div>
        <div id="collapseOne" class="accordion-body collapse in">
          <div class="accordion-inner">
            <?php echo $sample_text;?>
          </div>
        </div>
      </div>
      <div class="accordion-group">
        <div class="accordion-heading">
          <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseTwo">
            Collapsible Group Item #2
          </a>
        </div>
        <div id="collapseTwo" class="accordion-body collapse">
          <div class="accordion-inner">
            <?php echo $sample_text;?>
          </div>
        </div>
      </div>
      <div class="accordion-group">
        <div class="accordion-heading">
          <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseThree">
            Collapsible Group Item #3
          </a>
        </div>
        <div id="collapseThree" class="accordion-body collapse">
          <div class="accordion-inner">
            <?php echo $sample_text;?>
          </div>
        </div>
      </div>
      <div class="accordion-group">
        <div class="accordion-heading">
          <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseFour">
            Collapsible Group Item #4
          </a>
        </div>
        <div id="collapseFour" class="accordion-body collapse">
          <div class="accordion-inner">
            <?php echo $sample_text;?>
          </div>
        </div>
      </div>
    </div>
    
    
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiTabs",
		));
		
	?>
    <?php
    $this->widget('zii.widgets.jui.CJuiTabs', array(
		'tabs'=>array(
			'StaticTab 1'=>$sample_text,
			'StaticTab 2'=>$sample_text,
			'StaticTab 3'=>array('content'=>$sample_text, 'id'=>'tab3'),
		),
		// additional javascript options for the tabs plugin
		'options'=>array(
			'collapsible'=>true,
		),
	));
	?>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CPortlet",
		));
		
	?>
<p>This content is in a portlet</p>
<pre>&lt;?php $this-&gt;beginWidget('zii.widgets.CPortlet'); ?&gt;      <br />...insert content here...  <br />&lt;?php $this-&gt;endWidget(); ?&gt;</pre>
    
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiAutoComplete",
		));
		
	?>
    <p>Type <code>john</code> in the fild to see it at work</p>
    <?php
    $this->widget('zii.widgets.jui.CJuiAutoComplete', array(
		'name'=>'city',
		'source'=>array('John Doe', 'John Murry', 'Ben John', 'Johnny Walker'),
		// additional javascript options for the autocomplete plugin
		'options'=>array(
			'minLength'=>'2',
		),
		'htmlOptions'=>array(
			'style'=>'height:20px;'
		),
	));
	?>
    
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiDatePicker",
		));
		
	?>
   	<p>Click on the element below to see date picker</p>
    <?php
    $this->widget('zii.widgets.jui.CJuiDatePicker', array(
		'name'=>'publishDate',
		// additional javascript options for the date picker plugin
		'options'=>array(
			'showAnim'=>'fold',
            'language' => 'sl'
		),
		'htmlOptions'=>array(
			'style'=>'height:20px;'
		),
	));
	?>
    
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiButton",
		));
		
	?>
   
	<?php
    $this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button',
		'caption'=>'Save',
		'value'=>'asd',
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	
	$this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button1',
		'caption'=>'Save',
		'value'=>'asd1',
		'htmlOptions'=>array('class'=>'btn btn-primary'),
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	
	$this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button2',
		'caption'=>'Save',
		'value'=>'asd2',
		'htmlOptions'=>array('class'=>'btn btn-info'),
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	
	$this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button3',
		'caption'=>'Save',
		'value'=>'asd3',
		'htmlOptions'=>array('class'=>'btn btn-success'),
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	
	$this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button4',
		'caption'=>'Save',
		'value'=>'asd4',
		'htmlOptions'=>array('class'=>'btn btn-warning'),
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	
	$this->widget('zii.widgets.jui.CJuiButton', array(
		'name'=>'button5',
		'caption'=>'Save',
		'value'=>'asd5',
		'htmlOptions'=>array('class'=>'btn btn-danger'),
		'onclick'=>new CJavaScriptExpression('function(){alert("Save button has been clicked"); this.blur(); return false;}'),
	));
	?>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiDialog",
		));
		
	?>
    
    <?php
    $this->beginWidget('zii.widgets.jui.CJuiDialog', array(
		'id'=>'mydialog',
		// additional javascript options for the dialog plugin
		'options'=>array(
			'title'=>'Dialog box 1',
			'autoOpen'=>false,
		),
	));

    echo $sample_text;

$this->endWidget('zii.widgets.jui.CJuiDialog');

// the link that may open the dialog
$dialog_button = '<button type="button" class="btn btn-primary" data-loading-text="Loading...">Open dialog</button>';
echo CHtml::link($dialog_button, '#', array(
   'onclick'=>'$("#mydialog").dialog("open"); return false;',
));
	?>
    
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiProgressBar",
		));		
	?>
    <p>Standard progress bar</p>
    <p><code> with no styles defined</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>30,
	));
	?>
    <p>Striped progress bar</p>
    <p><code>'htmlOptions'=>array('class'=>'progress-striped'),</code></p>
    
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>40,
		'htmlOptions'=>array('class'=>'progress-striped'),
	));
	?>
    <p>Striped scrolling progress bar</p>
    <p><code>'htmlOptions'=>array('class'=>'progress-striped active'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>50,
		'htmlOptions'=>array('class'=>'progress-striped active'),
	));
	?>
    <p>Different colors to chose from</p>
    <p><code>'htmlOptions'=>array('class'=>'progress-info'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>60,
		'htmlOptions'=>array('class'=>'progress-info'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-success')</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>70,
		'htmlOptions'=>array('class'=>'progress-success'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-warning'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>80,
		'htmlOptions'=>array('class'=>'progress-warning'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-danger'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>90,
		'htmlOptions'=>array('class'=>'progress-danger'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-info progress-striped'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>90,
		'htmlOptions'=>array('class'=>'progress-info progress-striped'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-success progress-striped'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>80,
		'htmlOptions'=>array('class'=>'progress-success progress-striped'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-warning progress-striped'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>70,
		'htmlOptions'=>array('class'=>'progress-warning progress-striped'),
	));
	?>
    <p><code>'htmlOptions'=>array('class'=>'progress-danger progress-striped'),</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiProgressBar', array(
		'value'=>60,
		'htmlOptions'=>array('class'=>'progress-danger progress-striped'),
	));
	?>
  <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML - Progress bar",
		));
		
	?>
    <p>Standard progress bar</p>
    <p><code>.progress</code></p>
    <div class="progress">
      <div class="bar" style="width: 30%;"></div>
    </div>
    <p>Striped progress bar</p>
    <p><code>.progress-striped</code></p>
    <div class="progress progress-striped">
      <div class="bar" style="width: 40%;"></div>
    </div>
    <p>Striped active progress bar</p>
    <p><code>.progress-striped .active</code></p>
    <div class="progress progress-striped active">
      <div class="bar" style="width: 50%;"></div>
    </div>
    <p>Different colors to chose from</p>
    <p><code>.progress-info</code></p>
    <div class="progress progress-info">
      <div class="bar" style="width: 60%;"></div>
    </div>
    <p><code>.progress-success</code></p>
    <div class="progress progress-success">
      <div class="bar" style="width: 70%;"></div>
    </div>
    <p><code>.progress-warning</code></p>
    <div class="progress progress-warning">
      <div class="bar" style="width: 80%;"></div>
    </div>
    <p><code>.progress-danger</code></p>
    <div class="progress progress-danger">
      <div class="bar" style="width: 90%;"></div>
    </div>
    <p><code>.progress-info .progress-striped</code></p>
    <div class="progress progress-info progress-striped">
      <div class="bar" style="width: 90%;"></div>
    </div>
    <p><code>.progress-success .progress-striped</code></p>
    <div class="progress progress-success progress-striped">
      <div class="bar" style="width: 80%;"></div>
    </div>
    <p><code>.progress-warning .progress-striped</code></p>
    <div class="progress progress-warning progress-striped">
      <div class="bar" style="width: 70%;"></div>
    </div>
    <p><code>.progress-danger .progress-striped</code></p>
    <div class="progress progress-danger progress-striped">
      <div class="bar" style="width: 60%;"></div>
    </div>
    
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiSlider",
		));
		
	?>
    <p><code> with no style defined</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>30,
	));
	?>
    
    <p><code>.progress-info</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>40,
		'htmlOptions'=>array('class'=>'progress-info'),
	));
	?>
    <p><code>.progress-success</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>30,
		'htmlOptions'=>array('class'=>'progress-success'),
	));
	?>
    <p><code>.progress-warning</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>20,
		'htmlOptions'=>array('class'=>'progress-warning'),
	));
	?>
    <p><code>.progress-danger</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>30,
		'htmlOptions'=>array('class'=>'progress-danger'),
	));
	?>
    
    <p><code>.progress-striped</code></p>
    <?php
    $this->widget('zii.widgets.jui.CJuiSlider', array(
		'value'=>30,
		'htmlOptions'=>array('class'=>'progress-striped'),
	));
	?>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CJuiSlider - vertical",
		));
	?>
    
    <?php $this->endWidget();?>
  </div>
</div>