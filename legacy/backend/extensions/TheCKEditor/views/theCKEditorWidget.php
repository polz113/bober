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
 * see-> readme.txt
 */

require_once($ckeditor);

$oCKeditor = new CKEditor($ckBasePath);

// configure ckeditor:
if ($width) {
	$oCKeditor->config['width'] = $width;
}
if ($height) {
	$oCKeditor->config['height'] = $height;
}

$oCKeditor->config['toolbar'] = $toolbarSet;

if ($css) {
	$oCKeditor->config['stylesSet'] = $css;
}

if (isset($config) && is_array($config))
{
	foreach ($config as $key=>$value)
	{
		$oCKeditor->config[$key] = $value;
	}
}


// prints the widget
if (!empty($model) && !empty($attribute))
{
	$oCKeditor->editor(get_class($model).'['.$attribute.']', $model->$attribute);
}
elseif (!empty($name))
{
	$oCKeditor->editor($name, isset($value) ? $value : null);
}
?>
