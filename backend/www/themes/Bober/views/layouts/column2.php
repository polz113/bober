<?php /* @var $this Controller */ ?>
<?php $this->beginContent('//layouts/main'); ?>

<div class="row-fluid">
    <div class="span3">
        <div id="topWrapper">
            <a href="<?php echo Yii::t('app', 'http://www.bebras.org');?>" style="float: left;">
                <div class="category_button green">
                    <?php echo Yii::t('app', 'Homepage'); ?>
                </div>
            </a>
            <a href="<?php echo Yii::app()->user->loginUrl[0]; ?>">
                <div class="green category_button" style="float: right;">
                    <?php echo Yii::t('app', 'Login for teachers'); ?>
                </div>
            </a>
        </div>
        <div class="sidebar-nav">

            <?php
            $this->widget('zii.widgets.CMenu', array(
                /* 'type'=>'list', */
                'encodeLabel' => false,
                'items' => array(
                    array('label' => '<i class="icon icon-home"></i>  ' . Yii::t('app', 'Dashboard') . ' <span class="label label-info pull-right">BETA</span>', 'url' => array('/site/index'), 'itemOptions' => array('class' => '')),
                    // Include the operations menu
                    array('label' => Yii::t('app', 'operations'), 'items' => $this->menu),
                ),
            ));
            ?>
        </div>
        <br />

    </div><!--/span-->
    <div class="span9">

        <?php if (isset($this->breadcrumbs)): ?>
            <?php
            $this->widget('zii.widgets.CBreadcrumbs', array(
                'links' => $this->breadcrumbs,
                'homeLink' => CHtml::link(Yii::t('app', 'Dashboard')),
                'htmlOptions' => array('class' => 'breadcrumb')
            ));
            ?><!-- breadcrumbs -->
        <?php endif ?>

        <!-- Include content pages -->
        <?php echo $content; ?>

    </div><!--/span-->
</div><!--/row-->


<?php $this->endContent(); ?>
