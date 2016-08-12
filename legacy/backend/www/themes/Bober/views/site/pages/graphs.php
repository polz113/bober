<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name . ' - Graphs & Charts';
$this->breadcrumbs=array(
	'Graphs & Charts',
);
?>
<div class="page-header">
  <h1>Graphs &amp; Charts - <small>Flot and Sparkline</small></h1>
</div>

<div class="row-fluid">
  <div class="span9">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-user'></i> Live Visitors",
		));
		
	?>
  		<div class="auto-update-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
	<?php $this->endWidget();?>
  </div>
  <div class="span3">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-tag'></i> Account Stats",
		));
		
	?>
    <div style="text-align:center;">
        <p style="margin-bottom:20px;">
            <strong>Open Invoices - $24,270</strong><br />
            <span class="pie"></span>
        </p>
        <p style="margin-bottom:20px;">
            <strong>Overdue Invoices - $45,690</strong><br />
            <span class="dynamicbar">Loading..</span>
        </p>
        <p style="margin-bottom:20px;">
            <strong>Converted Quotes - $165,320</strong><br />
            <span class="inlinesparkline">1,4,4,7,5,9,10</span>
        </p>
        <p style="margin-bottom:20px;">
            <strong>Monthly Income - $245,000</strong><br />
        	<span class="dynamicsparkline">Loading..</span>
        </p>
	</div>


        
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span12">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-user'></i> Total Visitors",
		));
		
	?>
    	<div class="visitors-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
        
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-repeat'></i> Bar chart",
		));
		
	?>
  		<div class="horizontal-bars-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-share'></i> Returning Visitors",
		));
		
	?>
    	<div class="lines-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
        
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-pencil'></i> Data Usage",
		));
		
	?>
  		<div class="stacked-bars-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-arrow-down'></i> Data Usage Monthly",
		));
		
	?>
    	<div class="order-bars-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
        
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-tint'></i> Pie Charts",
		));
		
	?>
  		<div class="simple-pie" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-adjust'></i> Location Chart",
		));
		
	?>
    	<div class="simple-donut" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
        
    <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-check'></i> Other chart",
		));
		
	?>
  		<div class="simple-chart" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
	<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"<i class='icon-info-sign'></i> Pie chart",
		));
		
	?>
    	<div class="pieStats" style="height: 250px;width:100%;margin-top:15px; margin-bottom:15px;"></div>
        
    <?php $this->endWidget();?>
  </div>
</div>