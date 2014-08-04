<?php

/**
 * Widget to manage gallery.
 * Requires Twitter Bootstrap styles to work.
 *
 * @author Bogdan Savluk <savluk.bogdan@gmail.com>
 */
class GalleryManager extends CWidget {

    /** @var Gallery Model of gallery to manage */
    public $gallery;

    /** @var string Route to gallery controller */
    public $controllerRoute = false;
    public $assets;

    public function init() {
        $this->assets = Yii::app()->getAssetManager()->publish(dirname(__FILE__) . '/assets');
    }

    public $htmlOptions = array();

    /** Render widget */
    public function run() {
        /** @var $cs CClientScript */
        $cs = Yii::app()->clientScript;
        $cs->registerCssFile($this->assets . '/galleryManager.css');

        $cs->registerCoreScript('jquery');
        // $cs->registerCoreScript('jquery.ui');

        $baseUrl = Yii::app()->baseUrl;
        $cs = Yii::app()->getClientScript();
        $cs->registerScriptFile($baseUrl . '/js/jquery.lightbox-0.5.js');
        $cs->registerCssFile($baseUrl . '/css/jquery.lightbox-0.5.css');

        if (YII_DEBUG) {
            $cs->registerScriptFile($this->assets . '/jquery.iframe-transport.js');
            $cs->registerScriptFile($this->assets . '/jquery.galleryManager.js');
        } else {
            $cs->registerScriptFile($this->assets . '/jquery.iframe-transport.min.js');
            $cs->registerScriptFile($this->assets . '/jquery.galleryManager.min.js');
        }

        if ($this->controllerRoute === null)
            throw new CException('$controllerRoute must be set.', 500);

        $opts = array(
            'hasName:' => $this->gallery->name ? true : false,
            'hasDesc:' => $this->gallery->description ? true : false,
            'uploadUrl' => Yii::app()->createUrl($this->controllerRoute . '/ajaxUpload', array('gallery_id' => $this->gallery->id)),
            'deleteUrl' => Yii::app()->createUrl($this->controllerRoute . '/delete'),
            'updateUrl' => Yii::app()->createUrl($this->controllerRoute . '/changeData'),
            'arrangeUrl' => Yii::app()->createUrl($this->controllerRoute . '/order'),
            'nameLabel' => Yii::t('galleryManager.main', 'Name'),
            'descriptionLabel' => Yii::t('galleryManager.main', 'Description'),
        );

        if (Yii::app()->request->enableCsrfValidation) {
            $opts['csrfTokenName'] = Yii::app()->request->csrfTokenName;
            $opts['csrfToken'] = Yii::app()->request->csrfToken;
        }
        $opts_js = CJavaScript::encode($opts);
        $src = "jQuery('#{$this->id}').galleryManager({$opts_js});";
        $opts['uploadCustomUrl'] = Yii::app()->createUrl($this->controllerRoute . '/ajaxUploadCustom', array('gallery_id' => $this->gallery->id));
        $opts_js = CJavaScript::encode($opts);
        $src .= "\njQuery.GallerySettings_{$this->id} = {$opts_js};";
        $cs->registerScript('galleryManager#' . $this->id, $src);
        $model = new GalleryPhoto();

        $cls = "GalleryEditor ";
        if (!($this->gallery->name))
            $cls .= 'no-name';

        if (!($this->gallery->description)) {
            $cls .= (($cls != ' ') ? '-' : '') . 'no-desc';
        }
        if (isset($this->htmlOptions['class']))
            $this->htmlOptions['class'] .= ' ' . $cls;
        else
            $this->htmlOptions['class'] = $cls;
        $this->htmlOptions['id'] = $this->id;

        $this->render('galleryManager', array(
            'model' => $model,
        ));
    }

}
