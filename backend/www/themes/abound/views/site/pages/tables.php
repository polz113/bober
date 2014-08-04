<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name . ' - Tables - CGridview and HTML';
$this->breadcrumbs=array(
	'Tables - CGridview and HTML',
);
?>
<?php
$gridDataProvider = new CArrayDataProvider(array(
    array('id'=>1, 'firstName'=>'Mark', 'lastName'=>'Otto', 'language'=>'<span class="badge badge-warning">HTML</span>','usage'=>'<span class="inlinebar">1,4,4,7,5,9,10</span>'),
    array('id'=>2, 'firstName'=>'Jacob', 'lastName'=>'Thornton', 'language'=>'<span class="badge badge-important">CSS</span>','usage'=>'<span class="inlinebar">1,4,4,7,5,9,10</span>'),
    array('id'=>3, 'firstName'=>'Stu', 'lastName'=>'Dent', 'language'=>'<span class="badge badge-info">Javascript</span>','usage'=>'<span class="inlinebar">1,4,4,7,5,9,10</span>'),
));
?>

<div class="page-header">
  <h1>Tables <small>CGridview and HTML</small></h1>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CGridview - Row hovering",
		));
		
	?>
  	<?php $this->widget('zii.widgets.grid.CGridView', array(
			/*'type'=>'striped bordered condensed',*/
			'itemsCssClass'=>'table table-hover',
			'dataProvider'=>$gridDataProvider,
			'template'=>"{items}",
			'columns'=>array(
				array('name'=>'id', 'header'=>'#'),
				array('name'=>'firstName', 'header'=>'First name'),
				array('name'=>'lastName', 'header'=>'Last name'),
				array('name'=>'language', 'header'=>'Language', 'type'=>'raw'),
				array('name'=>'usage', 'header'=>'Usage', 'type'=>'raw'),
				
			),
		)); ?>
<?php $this->endWidget();?>
  </div>
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CGridview - Striped rows",
		));
		
	?>
    
  	<?php $this->widget('zii.widgets.grid.CGridView', array(
			/*'type'=>'striped bordered condensed',*/
			'itemsCssClass'=>'table table-striped',
			'dataProvider'=>$gridDataProvider,
			'template'=>"{items}",
			'columns'=>array(
				array('name'=>'id', 'header'=>'#'),
				array('name'=>'firstName', 'header'=>'First name'),
				array('name'=>'lastName', 'header'=>'Last name'),
				array('name'=>'language', 'header'=>'Language', 'type'=>'raw'),
				array('name'=>'usage', 'header'=>'Usage', 'type'=>'raw'),
				
			),
		)); ?>
        
        <?php $this->endWidget();?>
  </div>
</div>

<div class="row-fluid">
  <div class="span6">
  	<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CGridview - Bordered",
		));
		
	?>
    
  	<?php $this->widget('zii.widgets.grid.CGridView', array(
			/*'type'=>'striped bordered condensed',*/
			'itemsCssClass'=>'table table-bordered',
			'dataProvider'=>$gridDataProvider,
			'template'=>"{items}",
			'columns'=>array(
				array('name'=>'id', 'header'=>'#'),
				array('name'=>'firstName', 'header'=>'First name'),
				array('name'=>'lastName', 'header'=>'Last name'),
				array('name'=>'language', 'header'=>'Language', 'type'=>'raw'),
				array('name'=>'usage', 'header'=>'Usage', 'type'=>'raw'),
				
			),
		)); ?>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  	
    <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"CGridview - Striped, bordered and with row hovering",
		));
		
	?>
    
  	<?php $this->widget('zii.widgets.grid.CGridView', array(
			/*'type'=>'striped bordered condensed',*/
			'itemsCssClass'=>'table table-striped table-bordered table-hover',
			'dataProvider'=>$gridDataProvider,
			'template'=>"{items}",
			'columns'=>array(
				array('name'=>'id', 'header'=>'#'),
				array('name'=>'firstName', 'header'=>'First name'),
				array('name'=>'lastName', 'header'=>'Last name'),
				array('name'=>'language', 'header'=>'Language', 'type'=>'raw'),
				array('name'=>'usage', 'header'=>'Usage', 'type'=>'raw'),
				
			),
		)); ?>
    <?php $this->endWidget();?>
  </div>
</div>

<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>'CGridView - Striped, bordered, row hovering and condensed',
		));
		
?>

<?php $this->widget('zii.widgets.grid.CGridView', array(
			/*'type'=>'striped bordered condensed',*/
			'itemsCssClass'=>'table table-hover table-striped table-bordered table-condensed',
			'dataProvider'=>$gridDataProvider,
			'template'=>"{items}",
			'columns'=>array(
				array('name'=>'id', 'header'=>'#'),
				array('name'=>'firstName', 'header'=>'First name'),
				array('name'=>'lastName', 'header'=>'Last name'),
				array('name'=>'language', 'header'=>'Language', 'type'=>'raw'),
				array('name'=>'usage', 'header'=>'Usage', 'type'=>'raw'),
				
			),
		)); ?>
<?php 
$this->endWidget();
?>


<div class="row-fluid">
  <div class="span6">
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML Table - Row hovering",
		));
		
	?>
  	<table class="table table-hover">
      <caption>Table Caption</caption>
      <thead>
        <tr>
          <th>Browser</th>
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Internet Explorer</td>
          <td>60%</td>
        </tr>
        <tr>
          <td>Firefox</td>
          <td>20%</td>
        </tr>
        <tr>
          <td>Google Chrome</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Safari</td>
          <td>5%</td>
        </tr>
        <tr>
          <td>Opera</td>
          <td>5%</td>
        </tr>
      </tbody>
    </table>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML Table - Striped rows",
		));
		
	?>
    
  	<table class="table table-striped">
      <caption>Table Caption</caption>
      <thead>
        <tr>
          <th>Browser</th>
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Internet Explorer</td>
          <td>60%</td>
        </tr>
        <tr>
          <td>Firefox</td>
          <td>20%</td>
        </tr>
        <tr>
          <td>Google Chrome</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Safari</td>
          <td>5%</td>
        </tr>
        <tr>
          <td>Opera</td>
          <td>5%</td>
        </tr>
      </tbody>
    </table>
    <?php $this->endWidget();?>
  </div>
</div>


<div class="row-fluid">
  <div class="span6">
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML Table - Bordered",
		));
		
	?>
    
  	<table class="table table-bordered">
      <caption>Table Caption</caption>
      <thead>
        <tr>
          <th>Browser</th>
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Internet Explorer</td>
          <td>60%</td>
        </tr>
        <tr>
          <td>Firefox</td>
          <td>20%</td>
        </tr>
        <tr>
          <td>Google Chrome</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Safari</td>
          <td>5%</td>
        </tr>
        <tr>
          <td>Opera</td>
          <td>5%</td>
        </tr>
      </tbody>
    </table>
    <?php $this->endWidget();?>
  </div>
  <div class="span6">
  <?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>"HTML Table - Striped, bordered and with row hovering",
		));
		
	?>
  	<table class="table table-striped table-hover table-bordered">
      <caption>Table Caption</caption>
      <thead>
        <tr>
          <th>Browser</th>
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Internet Explorer</td>
          <td>60%</td>
        </tr>
        <tr>
          <td>Firefox</td>
          <td>20%</td>
        </tr>
        <tr>
          <td>Google Chrome</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Safari</td>
          <td>5%</td>
        </tr>
        <tr>
          <td>Opera</td>
          <td>5%</td>
        </tr>
      </tbody>
    </table>
    <?php $this->endWidget();?>
  </div>
</div>

<?php
		$this->beginWidget('zii.widgets.CPortlet', array(
			'title'=>'HTML Table - Striped, bordered, row hovering and condensed',
		));
		
?>

<table class="table table-striped table-hover table-bordered table-condensed">
      <caption>Table Caption</caption>
      <thead>
        <tr>
          <th>Browser</th>
          <th>Users</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Internet Explorer</td>
          <td>60%</td>
        </tr>
        <tr>
          <td>Firefox</td>
          <td>20%</td>
        </tr>
        <tr>
          <td>Google Chrome</td>
          <td>10%</td>
        </tr>
        <tr>
          <td>Safari</td>
          <td>5%</td>
        </tr>
        <tr>
          <td>Opera</td>
          <td>5%</td>
        </tr>
      </tbody>
    </table>
<?php 
$this->endWidget();
?>