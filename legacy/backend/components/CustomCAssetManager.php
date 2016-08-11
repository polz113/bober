<?php

class CustomCAssetManager extends CAssetManager {
    public function publish($path, $hashByName = false, $level = -1, $forceCopy = null) {
        $hashByName = true;
        return parent::publish($path, $hashByName, $level, $forceCopy);
    }
}
