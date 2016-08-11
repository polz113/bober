<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php echo Yii::app()->language; ?>" lang="<?php echo Yii::app()->language; ?>">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="dns-prefetch" href="//fonts.googleapis.com" />
        <link rel="dns-prefetch" href="//<?php echo Yii::app()->params['staticDomain'] ?>" />
        <title><?php echo Yii::app()->name; ?></title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Bober - tekmovanja" />
        <meta name="author" content="FRI / COMCODE d.o.o." />
        <meta name="robots" content="noindex" />
        <link href='https://fonts.googleapis.com/css?family=Carrois+Gothic' rel='stylesheet' type='text/css' />
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        <?php
        $baseUrl = Yii::app()->theme->baseUrl;
        $cs = Yii::app()->getClientScript();
        Yii::app()->clientScript->registerCoreScript('jquery');
        ?>
        <!-- Fav and Touch and touch icons -->
        <link rel="shortcut icon" href="<?php echo $baseUrl; ?>/img/favicon.ico" />
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="<?php echo $baseUrl; ?>/img/icons/apple-touch-icon-144-precomposed.png" />
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="<?php echo $baseUrl; ?>/img/icons/apple-touch-icon-72-precomposed.png" />
        <link rel="apple-touch-icon-precomposed" href="<?php echo $baseUrl; ?>/img/icons/apple-touch-icon-57-precomposed.png" />
        <?php
        $cs->registerCssFile($baseUrl . '/css/bootstrap.min.css');
        $cs->registerCssFile($baseUrl . '/css/bootstrap-responsive.min.css');
        $cs->registerCssFile($baseUrl . '/css/abound.css');
        $cs->registerCssFile($baseUrl . '/css/style-blue.css');

        $cs->registerScriptFile($baseUrl . '/js/bootstrap.min.js');
        $cs->registerScriptFile($baseUrl . '/js/plugins/jquery.sparkline.js');
        $cs->registerScriptFile($baseUrl . '/js/plugins/jquery.flot.min.js');
        $cs->registerScriptFile($baseUrl . '/js/plugins/jquery.flot.pie.min.js');
        $cs->registerScriptFile($baseUrl . '/js/charts.js');
        $cs->registerScriptFile($baseUrl . '/js/plugins/jquery.knob.js');
        $cs->registerScriptFile($baseUrl . '/js/plugins/jquery.masonry.min.js');
        ?>

        <script type="text/javascript">

            function calculateNewWidth()
            {
                var newWidth = $(".row-fluid").width() - $(".span3").width() - 55;

                $(".span9").width(Math.max(1000, newWidth));
            }

            function initializeFancyCheckboxes(container) {
                if (container != '')
                {
                    container = container + ' ';
                }

                $(container + ".switch label:not(.checked)").click(function() {
                    var label = $(this);
                    var input = $('#' + label.attr('for'));

                    if (input.prop('disabled'))
                    {
                        return;
                    }

                    if (!input.prop('checked')) {
                        label.closest('.switch').find("label").removeClass('checked');
                        label.addClass('checked');
                        input.prop('checked', true);
                    }
                });

                $(container + ".switch input[checked=checked]").each(function() {
                    $("label[for=" + $(this).attr('id') + "]").addClass('checked');
                });
            }

            $(window).resize(calculateNewWidth);
            $(window).load(calculateNewWidth);
            $(".span9").resize(calculateNewWidth);

            $(window).load(function() {
                initializeFancyCheckboxes('');
            });

        </script>

        <script type="text/javascript">
            //<![CDATA[
            var _prum = [['id', '528063f9abe53dad38000000'],
                ['mark', 'firstbyte', (new Date()).getTime()]];
            (function() {
                var s = document.getElementsByTagName('script')[0]
                        , p = document.createElement('script');
                p.async = 'async';
                p.src = '//rum-static.pingdom.net/prum.min.js';
                s.parentNode.insertBefore(p, s);
            })();
            //]]>
        </script>
    </head>
    <body>
        <script type="text/javascript">
            //<![CDATA[
            (function(i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r;
                i[r] = i[r] || function() {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date();
                a = s.createElement(o),
                        m = s.getElementsByTagName(o)[0];
                a.async = 1;
                a.src = g;
                m.parentNode.insertBefore(a, m)
            })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

            ga('create', 'UA-45522902-1', 'acm.si');
            ga('send', 'pageview');

            function GAPushEvent(category, action) {
                ga('send', 'event', category, action);
            }
            function GAPushEventExtended(category, action, label, value) {
                ga('send', 'event', category, action, label, value);
            }
            //]]>
        </script>