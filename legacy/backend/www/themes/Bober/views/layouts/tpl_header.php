<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php echo Yii::app()->language; ?>" lang="<?php echo Yii::app()->language; ?>">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="dns-prefetch" href="//<?php echo Yii::app()->params['staticDomain'] ?>" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Bober - tekmovanja" />
        <meta name="author" content="FRI / COMCODE d.o.o." />
        <meta name="robots" content="noindex" />

        <?php
        $baseUrl = Yii::app()->theme->baseUrl;
        $cs = Yii::app()->getClientScript();
        Yii::app()->clientScript->registerCoreScript('jquery');
        Yii::app()->clientScript->registerCoreScript('jquery.ui');
        $cs->registerCssFile($cs->getCoreScriptUrl() . '/jui/css/base/jquery-ui.css');
        ?>

        <title><?php echo Yii::t('app', 'Beaver'); ?></title>

        <!--[if IE 7]>
        <link href="<?php echo $baseUrl . '/css/styleIE7.css'; ?>" media="screen" rel="stylesheet" type="text/css" />
        <![endif]-->
        <?php
        $cs->registerScriptFile($baseUrl . '/js/jquery.jCounter.js');
        $cs->registerCssFile($baseUrl . '/css/style.css');
        $cs->registerScriptFile($baseUrl . '/js/rails.js');
        $cs->registerCssFile($baseUrl . '/css/jquery.jCounter.css');
        $cs->registerScriptFile($baseUrl . '/js/jquery.cookie.js');
        ?>

        <link rel="shortcut icon" href="<?php echo $baseUrl; ?>/img/favicon.ico" type="image/x-icon" />

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
