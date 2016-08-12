<?php

date_default_timezone_set('Europe/Ljubljana');
if (!function_exists('pre_print')) {

    function pre_print($obj) {
        echo '<pre>';
        print_r($obj);
        echo '</pre>';
    }

}
Yii::$classMap = array(
        // 'CCAssetManager' => dirname(__FILE__) . '/../../common/components/CCAssetManager.php',
        // 'Bootstrap' => dirname(__FILE__) . '/../../common/extensions/bootstrap/components/Bootstrap.php'
);
// uncomment the following to define a path alias
// Yii::setPathOfAlias('local','path/to/local-folder');
// This is the main Web application configuration. Any writable
// CWebApplication properties can be configured here.
return array(
    'basePath' => dirname(__FILE__) . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR,
    'name' => 'Bober',
    'charset' => 'utf-8',
    'language' => 'en',
    'sourceLanguage' => '00',
    'theme' => 'abound',
    // preloading 'log' component
    'preload' => array('log' /* , 'bootstrap' */),
    // autoloading model and component classes
    'import' => array(
        'application.models.*',
        'application.components.*',
        'application.modules.user.models.*',
        'application.modules.user.components.*',
        'application.validators.*',
        'ext.galleryManager.models.*',
        'ext.galleryManager.*'
    ),
    'behaviors' => array(
        'onbeginRequest' => array('class' => 'application.components.StartupBehavior'),
    ),
    'modules' => array(
        'gii' => array(
            'class' => 'system.gii.GiiModule',
            'password' => 'CHANGETHIS',
            // If removed, Gii defaults to localhost only. Edit carefully to taste.
            'ipFilters' => array('127.0.0.1', '::1'),
            'generatorPaths' => array(
                'bootstrap.gii'
            )
        ),
        'user' => array(
            # encrypting method (php hash function)
            'hash' => 'sha512',
            # send activation email
            'sendActivationMail' => true,
            # allow access for non-activated users
            'loginNotActiv' => false,
            # activate user on registration (only sendActivationMail = false)
            'activeAfterRegister' => false,
            # automatically login from registration
            'autoLogin' => true,
            # registration path
            'registrationUrl' => array('/user/registration'),
            # recovery password path
            'recoveryUrl' => array('/user/recovery'),
            # login form path
            'loginUrl' => array('/site/login'),
            # page after login
            'returnUrl' => array('/site/index'),
            # page after logout
            'returnLogoutUrl' => array('/site/login'),
        // 'profileRelations' => array(
        // 'country' => array(CActiveRecord::BELONGS_TO, 'Country', 'country_id'),
        // ),
        ),
    ),
    // application components
    'components' => array(
        'themeManager' => array(
        // 'basePath' => dirname(__FILE__).DIRECTORY_SEPARATOR.'..'.DIRECTORY_SEPARATOR.'themes'
        ),
        'localtime' => array(
            'class' => 'LocalTime',
        ),
        'user' => array(
            // enable cookie-based authentication
            'class' => 'WebUser',
            'allowAutoLogin' => true,
            'loginUrl' => array('/user/login'),
        ),
        'browser' => array(
            'class' => 'application.extensions.browser.CBrowserComponent',
        ),
        /* 'bootstrap' => array(
          'class' => 'Bootstrap', // assuming you extracted bootstrap under extensions
          ), */
        // uncomment the following to enable URLs in path-format
        'urlManager' => array(
            'urlFormat' => 'path',
            'rules' => array(
                '<controller:\w+>/<id:\d+>' => '<controller>/view',
                '<controller:\w+>/<action:\w+>/<id:\d+>' => '<controller>/<action>',
                '<controller:\w+>/<action:\w+>' => '<controller>/<action>',
            ),
        ),
        'session' => array(
            'sessionName' => 'Session',
            'class' => 'system.web.CDbHttpSession',
            'autoCreateSessionTable' => false,
            'connectionID' => 'db',
            'autoStart' => 'true',
            'timeout' => 3600
        ),
        'assetManager' => array(
            'class' => 'application.components.CustomCAssetManager',
        ),/*
        'db' => array(
            'connectionString' => 'mysql:host=127.0.0.1;dbname=bober',
            'emulatePrepare' => true,
            'username' => (in_array($_SERVER['HTTP_HOST'], array('bober.comcode.si', 'boberadmin.comcode.si', 'bober1.acm.si', 'bober.acm.si', '193.2.76.42', '193.2.76.43', '193.2.76.37')) ? 'bober' : 'root'),
            'password' => (in_array($_SERVER['HTTP_HOST'], array('bober.comcode.si', 'boberadmin.comcode.si', 'bober1.acm.si', 'bober.acm.si', '193.2.76.42', '193.2.76.43', '193.2.76.37')) ? 'SOMELONGHASH' : ''),
            'charset' => 'utf8',
        ),*/
	'db'=>array(
		'connectionString'=>'mysql:host=127.0.0.1;dbname=bober',
		'username'=>'bober',
		'password'=>'DATABASE PASSWORD',
		'charset'=>'utf8',
	),

        'cache' => array(
            'class' => 'system.caching.CMemCache',
            'servers' => array(
                array('host' => '127.0.0.1', 'port' => '11211', 'weight' => '60'),
            ),
        ),
        'errorHandler' => array(
            // use 'site/error' action to display errors
            'errorAction' => 'site/error',
        ),
        'log' => array(
            'class' => 'CLogRouter',
            'routes' => array(
                array(
                    'class' => 'CFileLogRoute',
                    'levels' => 'error, warning',
                ),
            /* array( // used for debugging sql queries
              'class' => 'CWebLogRoute',
              'enabled' => YII_DEBUG_SHOW_PROFILER,
              'categories' => 'system.db.*',
              ), */
            // uncomment the following to show log messages on web pages
            /*
              array(
              'class'=>'CWebLogRoute',
              ),
             */
            ),
        ),
        'image' => array(
            'class' => 'ext.image.CImageComponent',
            // GD or ImageMagick
            'driver' => 'GD',
        // ImageMagick setup path
        // 'params'=>array('directory'=>'D:/Program Files/ImageMagick-6.4.8-Q16'),
        ),
        'widgetFactory' => array(
            'class' => 'WidgetFactory',
            'onAfterCreateWidget' => function(WidgetEvent $event) {
        static $defaultPageSize = 20;
        $widget = $event->widget;
        // pre_print(get_class($widget));
        if ($widget instanceof CBaseListView || $widget instanceof CGridView) {
            /** @var CBaseListView $widget */
            if ($widget->dataProvider !== null && $widget->dataProvider->pagination !== false)
                $widget->dataProvider->pagination->pageSize = $defaultPageSize;
        }
    },
        ),
    ),
    'controllerMap' => array(
        'gallery' => 'ext.galleryManager.GalleryController'
    ),
    // application-level parameters that can be accessed
    // using Yii::app()->params['paramName']
    'params' => array(
        // the language used for competitions on this server
        'preferred_language' => 'en',
        // dump answers to disk instead of a database for marginally improved performance
        'dump_answers_to_disk' => False,
        // this is used in contact page
        'adminEmail' => 'admin@localhost',
        'staticDomain' => (in_array($_SERVER['HTTP_HOST'], array('bober.comcode.si', 'boberadmin.comcode.si')) ? 'static-bober.comcode.si' : 'static.bober' . ($_SERVER['SERVER_PORT'] != 80 ? ':' . $_SERVER['SERVER_PORT'] : ''))
    ),
);
