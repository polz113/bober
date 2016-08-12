<?php
/*
 * Created on 01.01.2009
 * Updated on 27.06.2012
 *
 * Copyright: Christian Kütbach
 * Updated by: Ali Qanavatian
 *
 * GNU LESSER GENERAL PUBLIC LICENSE
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Requirements:
 * The CK-Editor have to be installed and configured. The Editor itself is
 * not included to this extension.
 *
 * This extension have to be installed into:
 * <Yii-Application>/protected/extensions/TheCKEditor
 *
 * Usage:
 * <?php $this->widget('application.extensions.TheCKEditor.theCKEditorWidget',array(
 * 			'model'			=>	$pages,
 * 			'property'		=>	'content',
 * 			'height'		=>	'400px',
 * 			'width'			=>	'100%',
 * 			'ckeditor'		=>	Yii::app()->basePath.'/../ckeditor.php',
 * 			'ckBasePath'	=>	Yii::app()->baseUrl.'/',
 * 			'css'			=>	Yii::app()->baseUrl.'/css/index.css'
 * ) ); ?>
 */

class TheCKEditorWidget extends CInputWidget
{
	public $ckeditor;
	public $ckBasePath;
	public $height = '375px';
	public $width = '100%';
	public $toolbarSet;
	public $config;
	public $css;

	public function run()
	{
		if (!isset($this->ckeditor)){
			throw new CHttpException(500,'Parameter "ckeditor" has to be set!');
		}
		if (!isset($this->ckBasePath)){
			throw new CHttpException(500,'Parameter "ckBasePath" has to be set!');
		}
		if (!$this->hasModel() && !isset($this->name)) {
			throw new CHttpException(500,'Parameters "model" and "attribute" or "name" have to be set!');
		}
		if (!isset($this->toolbarSet)){
			$this->toolbarSet = "Default";
		}
		$this->render('theCKEditorWidget',array(
			'ckeditor'=>$this->ckeditor,
			'ckBasePath'=>$this->ckBasePath,
			'model'=>$this->model,
			'attribute'=>$this->attribute,
			'name'=>$this->name,
			'value'=>$this->value,
			'height'=>$this->height,
			'width'=>$this->width,
			'toolbarSet'=>$this->toolbarSet,
			'config'=>$this->config,
			'css'=>$this->css,
		));
	}
}
?>
