<?php

class CCAssetManager extends CAssetManager {

    public $bucket;
    public $path;
    public $host;
    public $ccComponent = 'cc';
    public $cacheComponent = 'cache';
    private $_baseUrl;
    private $_basePath;
    private $_published;

    public function getBasePath() {
        if ($this->_basePath === null) {
            $this->_basePath = $this->path;
        }
        return $this->_basePath;
    }

    public function getBaseUrl() {
        if ($this->_baseUrl === null) {
            $this->_baseUrl = 'http'.(array_key_exists('HTTPS', $_SERVER) && $_SERVER['HTTPS'] == 'on' ? 's' : '').'://' . $this->host . '/' . $this->path;
        }
        return $this->_baseUrl;
    }

    private function getCache() {
        if (!Yii::app()->{$this->cacheComponent})
            throw new CException('You need to configure a cache storage or set the variable cacheComponent');

        return Yii::app()->{$this->cacheComponent};
    }

    private function getCacheKey($path) {
        return $this->hash(Yii::app()->request->serverName) . '.' . $path;
    }

    private function copy_r($path, $dest) {
        if (!defined('DS')) {
            define('DS', DIRECTORY_SEPARATOR);
        }
        if (is_dir($path)) {
            @mkdir($dest);
            $objects = scandir($path);
            if (sizeof($objects) > 0) {
                foreach ($objects as $file) {
                    if ($file == "." || $file == ".." || in_array($file, $this->excludeFiles))
                        continue;
                    // go on
                    if (is_dir($path . DS . $file)) {
                        $this->copy_r($path . DS . $file, $dest . DS . $file);
                    } else {
                        copy($path . DS . $file, $dest . DS . $file);
                    }
                }
            }
            return true;
        } elseif (is_file($path)) {
            return copy($path, $dest);
        } else {
            return false;
        }
    }

    public function publish($path, $hashByName = false, $level = -1, $forceCopy = false) {
        if (isset($this->_published[$path]) && !$forceCopy) {
            return $this->_published[$path];
        } else if (($src = realpath($path)) !== false) {
            if (is_file($src)) {
                $dir = $this->hash($hashByName ? basename($src) : dirname($src) . filemtime($src));
                $asset_dir = dirname(__FILE__) . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'static' . DIRECTORY_SEPARATOR . 'assets' . DIRECTORY_SEPARATOR;
                if (!is_dir($asset_dir)) {
                    mkdir($asset_dir);
                }
                $staticDir = $asset_dir . $dir . DIRECTORY_SEPARATOR;
                // echo $staticDir;
                if (!is_dir($staticDir)) {
                    mkdir($staticDir);
                }
                $fileName = basename($src);
                if (!file_exists($staticDir . $fileName)) {
                    copy($src, $staticDir . $fileName);
                }
                return $this->_published[$path] = $this->getBaseUrl() . '/' . $dir . '/' . $fileName;
            } else if (is_dir($src)) {
                $dir = $this->hash($hashByName ? basename($src) : $src . filemtime($src));
                if ($this->getCache()->get($this->getCacheKey($path)) === false) {
                    $asset_dir = dirname(__FILE__) . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'static' . DIRECTORY_SEPARATOR . 'assets' . DIRECTORY_SEPARATOR;
                    if (!is_dir($asset_dir)) {
                        mkdir($asset_dir);
                    }
                    $staticDir = $asset_dir . $dir . DIRECTORY_SEPARATOR;
                    // echo $staticDir;
                    if (!is_dir($staticDir)) {
                        mkdir($staticDir);
                    }
                    $this->copy_r($src, $staticDir);

                    $this->getCache()->set($this->getCacheKey($path), true, 0, new CDirectoryCacheDependency($src));
                }
                return $this->_published[$path] = $this->getBaseUrl() . '/' . $dir;
            }
        }
        throw new CException(Yii::t('yii', 'The asset "{asset}" to be published does not exist.', array('{asset}' => $path)));
    }

}

?>