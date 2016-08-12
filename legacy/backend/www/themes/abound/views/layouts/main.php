<?php
$superuser = Generic::isSuperAdmin();
header('X-UA-Compatible: IE=edge,chrome=1');
require_once('tpl_header.php');
?>

<!-- Require the navigation -->
<?php require_once('tpl_navigation.php') ?>

<div class="container-fluid">				

    <!-- Include content pages -->
    <?php echo $content; ?>

</div><!--/.fluid-container-->

<?php require_once('tpl_modal.php') ?>
<?php require_once('tpl_dynamic.php')?>

<!-- Require the footer -->
<?php require_once('tpl_footer.php') ?>
