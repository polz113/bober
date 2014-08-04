<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name . ' - Typography';
$this->breadcrumbs=array(
	'Typography',
);
?>

<div class="page-header">
  <h1>Typography</h1>
</div>
<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Alerts - HTML",
		));
		
	?>
<p>
<code>.alert</code>
</p>
<div class="alert">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Warning!</strong> Best check yo self, you're not looking too good.
</div>
<p>
<code>.alert .alert-error</code>
</p>
<div class="alert alert-error">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Oh snap!</strong> Change a few things up and try submitting again.
</div>
<p>
<code>.alert .alert-success</code>
</p>
<div class="alert alert-success">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Well done!</strong> You successfully read this important alert message.
</div>
<p>
<code>.alert .alert-info</code>
</p>
<div class="alert alert-info">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Heads up!</strong> This alert needs your attention, but it's not super important.
</div>

  	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Alerts - Yii flash messages",
		));
		
	?>

<?php
Yii::app()->user->setFlash('notice', "<strong>Warning!</strong> Best check yo self, you're not looking too good.");
Yii::app()->user->setFlash('error', "<strong>Oh snap!</strong> Change a few things up and try submitting again.");
Yii::app()->user->setFlash('success', "<strong>Well done!</strong> You successfully read this important alert message.");
Yii::app()->user->setFlash('info', "<strong>Heads up!</strong> This alert needs your attention, but it's not super important.");

foreach(Yii::app()->user->getFlashes() as $key => $message) {
	echo '<p><code>Yii::app()->user->setFlash("' . $key . '", "Your message...");</code></p>'
			. '<div class="alert alert-' . $key . '">'
	 		.'<button type="button" class="close" data-dismiss="alert">×</button>'
			. $message . "</div>\n";
}
?>
<?php $this->endWidget();?>
  </div>
</div>
<p>
    This is a hero unit <code>class="hero-unit"</code>
  </p>
<div class="hero-unit">
  <h1>Amazing free Yii theme</h1>
  <p>... bring the life out of your web apps</p>
  <p>
    <a class="btn btn-success btn-large">
      Learn more
    </a>
  </p>
  
</div>



<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Header Tag",
		));
		
	?>
    	<h1>h1. Heading 1</h1>
        <h2>h2. Heading 2</h2>
        <h3>h3. Heading 3</h3>
        <h4>h4. Heading 4</h4>
        <h5>h5. Heading 5</h5>
        <h6>h6. Heading 6</h6>
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Lead, body and fine print",
		));
		
	?>
    
	<p class="lead">
    	Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Duis mollis, est non commodo luctus. <code>&lt;p class=&quot;lead&quot;&gt;...&lt;/p&gt;</code>
    </p>
    
    <p>
    	Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Duis mollis, est non commodo luctus.
    </p>
    
    <p>
      <small>This line of text is meant to be treated as fine print.</small>
    <code>&lt;small&gt;...&lt;/small&gt;</code></p>
        
  	<?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Block quote",
		));
		
	?>
    	
<blockquote class="pull-right">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
      <p><small>Someone famous <cite title="Source Title">Source Title</cite></small>
      </p>
      
        </blockquote>
        <p><code>&lt;blockquote class=&quot;pull-right&quot;&gt;...&lt;/blockquote&gt;</code></p>
        <blockquote>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
          <small>Someone famous <cite title="Source Title">Source Title</cite></small>
        </blockquote>
        
    <p><code>&lt;blockquote&gt;...&lt;/blockquote&gt;</code></p>    
        
        
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Emphasis",
		));
		
	?>
    
	<p class="muted">Fusce dapibus, tellus ac cursus commodo.<br />
    <code>&lt;p class=&quot;muted&quot;&gt;...&lt;/p&gt;</code>	</p>
	<p class="text-warning">Etiam porta sem malesuada magna mollis euismod.<br />
    <code>&lt;p class=&quot;text-warning&quot;&gt;...&lt;/p&gt;</code></p>
    <p class="text-error">Donec ullamcorper nulla non metus auctor fringilla.<br />
    <code>&lt;p class=&quot;text-error&quot;&gt;...&lt;/p&gt;</code></p>
    <p class="text-info">Aenean eu leo quam. Pellentesque ornare sem.<br />
    <code>&lt;p class=&quot;text-info&quot;&gt;...&lt;/p&gt;</code></p>
    <p class="text-success">Duis mollis, est non commodo luctus.<br />
    <code>&lt;p class=&quot;text-success&quot;&gt;...&lt;/p&gt;</code></p>
        
  	<?php $this->endWidget();?>
  </div>
</div>


<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Labels",
		));
		
	?>
    	<p>
        	<span class="label">Default</span> <code>class="label"</code>
        </p>
        <p>
        	<span class="label label-success">Success</span> <code>class="label label-success"</code>
        </p>
        <p>
        	<span class="label label-warning">Warning</span> <code>class="label label-warning"</code>
        </p>
        <p>
        	<span class="label label-important">Important</span> <code>class="label label-important"</code>
        </p>
        <p>
        	<span class="label label-info">Info</span> <code>class="label label-info"</code>
        </p>
        <p>
        	<span class="label label-inverse">Inverse</span> <code>class="label label-inverse"</code>
        </p>
   <?php $this->endWidget();?>     
   </div>
  <div class="span6">
    <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"Badges",
		));
		
	?>    
        <p>
        	<span class="badge">1</span> <code>class="badge"</code>
        </p>
        <p>
        	<span class="badge badge-success">2</span> <code>class="badge badge-success"</code>
        </p>
        <p>
        	<span class="badge badge-warning">3</span> <code>class="badge badge-warning"</code>
        </p>
        <p>
        	<span class="badge badge-important">4</span> <code>class="badge badge-important"</code>
        </p>
        <p>
        	<span class="badge badge-info">5</span> <code>class="badge badge-info"</code>
        </p>
        
        <p>
        	<span class="badge badge-inverse">6</span> <code>class="badge-inverse"</code>
        </p>
        
	<?php $this->endWidget();?>
  </div>
</div>
