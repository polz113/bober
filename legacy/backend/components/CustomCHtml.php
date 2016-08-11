<?php

class CustomCHtml extends CHtml
{
	/**
	 * Generates a switch which only allows single selection.
	 * @param string $name name of the switch. You can use this name to retrieve
	 * the selected value(s) once the form is submitted.
	 * @param string $select selection of the radio buttons.
	 * @param array $data value-label pairs used to generate the radio button list.
	 * Note, the values will be automatically HTML-encoded, while the labels will not.
	 * @param array $htmlOptions addtional HTML options. The options will be applied to
	 * each radio button input. The following special options are recognized:
	 * <ul>
	 * <li>template: string, specifies how each radio button is rendered. Defaults
	 * to "{input} {label}", where "{input}" will be replaced by the generated
	 * radio button input tag while "{label}" will be replaced by the corresponding radio button label.</li>
	 * <li>separator: string, specifies the string that separates the generated radio buttons. Defaults to new line (<br/>).</li>
	 * <li>labelOptions: array, specifies the additional HTML attributes to be rendered
	 * for every label tag in the list.</li>
	 * <li>container: string, specifies the radio buttons enclosing tag. Defaults to 'span'.
	 * If the value is an empty string, no enclosing tag will be generated</li>
	 * </ul>
	 * @return string the generated radio button list
	 */
	public static function radioButtonSwitch($name,$select,$data,$htmlOptions=array())
	{
        $container = "div";
		$template=isset($htmlOptions['template'])?$htmlOptions['template']:'{input} {label}';
		$separator=isset($htmlOptions['separator'])?$htmlOptions['separator']:"";
		unset($htmlOptions['template'],$htmlOptions['separator'],$htmlOptions['container']);

		$labelOptions=isset($htmlOptions['labelOptions'])?$htmlOptions['labelOptions']:array();
		unset($htmlOptions['labelOptions']);

		$items=array();
		$baseID=self::getIdByName($name);
		$id=0;
		foreach($data as $value=>$label)
		{
			$checked=!strcmp($value,$select);
			$htmlOptions['value']=$value;
			$htmlOptions['id']=$baseID.'_'.$id++;
			$option=self::radioButton($name,$checked,$htmlOptions);
			$label=self::label($label,$htmlOptions['id'],$labelOptions);
			$items[]=strtr($template,array('{input}'=>$option,'{label}'=>$label));
		}

        return self::tag($container,array('id'=>$baseID,'class'=>'switch'),implode($separator,$items));

        return CHtml::radioButtonList($name, $select, $data, $htmlOptions);
    }

	public static function error($model,$attribute,$htmlOptions=array())
	{
		// self::resolveName($model,$attribute); // turn [a][b]attr into attr
        
		$error=$model->getError($attribute);
		
        if($error!='')
		{
			if(!isset($htmlOptions['class']))
				$htmlOptions['class']=self::$errorMessageCss;
			return self::tag('div',$htmlOptions,$error);
		}
		else
			return '';
	}
    
	/**
	 * Generates a drop down list for a model attribute.
     * 
	 * @param CModel $model the data model
	 * @param string $attribute the attribute
	 * @param array $data data for generating the list options (value=>display)
     * @param type $dropdownOptions additional HTML attributes for the dropdown part of the list.
     * Besides the general HTML attributes, which are already suported by {@link activeDropdownList}, 
     * the following additional options (HTML and non-HTML are supported):
     * <ul>
     * <li><b>loadingImage</b>: array of options for displaying the image for loading indicator, 
     * used to indicate "busy" state (i.e. when ajax request is being processed in background).
     * Valid options are:
     * <ul>
     * <li><b>image</b>, string, sets the image for loading indicator; if not set, the image is
     * automatically determined as Yii::app()->theme->baseUrl.'/img/icons/loading.gif'.</li>
     * <li><b>htmlOptions</b>, array (attribute => value) of HTML attributes for the IMG tag</li>
     * </ul>
     * </li>
     * </ul>
     * @param type $optionsAdd additional options for the ADD button:
     * <ul>
     * <li><b></b>
     * </li>
     * </ul>
     * @param type $optionsEdit additional options for the EDIT button:
     * <ul>
     * <li><b></b>
     * </li>
     * </ul>
	 * @return string the generated drop down list
     */
    public static function advancedDropDownList($model, $attribute, $data, $dropdownOptions = array(), $optionsAdd = array(), $optionsEdit = array())
    {
        $loadingImage = "";
        

        
        if (!array_key_exists('image', $optionsAdd))
        {
            $optionsAdd['image'] = Yii::app()->theme->baseUrl.'/img/add.png';
        }
        
        if (!array_key_exists('image', $optionsEdit))
        {
            $optionsEdit['image'] = Yii::app()->theme->baseUrl.'/img/edit.png';
        }
        
        $addButton = self::createButtonLink($optionsAdd);
        $editButton = self::createButtonLink($optionsEdit);
        
        if (array_key_exists('loadingImage', $dropdownOptions))
        {
            $loadingImage = CustomCHtml::createLoadingImage($dropdownOptions['loadingImage'], $addButton != "" && $editButton != "");
            unset($dropdownOptions['loadingImage']);
        }
        
        $dropdownList = CHtml::activeDropDownList($model, $attribute, $data, $dropdownOptions);
        
        return $dropdownList.$addButton.$editButton.$loadingImage;
    }

    private static function createLoadingImage($options, $twoButtons)
    {
        $img = "";

        $image = array_key_exists('image', $options) ? $options['image'] : Yii::app()->theme->baseUrl.'/img/icons/loading.gif';
        $id = array_key_exists('id', $options) ? ' id="'.$options['id'].'"' : '';

        $marginLeft = $twoButtons ? 67 + 25 : 67;
        
        $defaultStyle = "z-index: 999; display: none; position: relative; left: -".$marginLeft."px;";
        $style = array_key_exists('style', $options) ? $defaultStyle.$options['style'] : $defaultStyle;
        
        if (array_key_exists('htmlOptions', $options))
        {
            if (array_key_exists('style', $options['htmlOptions']))
            {
                $style .= $options['htmlOptions']['style'];
                unset($options['htmlOptions']['style']);
            }

            $imageAttributes = self::renderAttributes($options['htmlOptions']);
        }
        else
        {
            $imageAttributes = "";
        }
        
        $img = '<img'.$imageAttributes.$id.' src="'.$image.'" style="'.$style.'"/>';

        return $img;
    }
    
    private static function createButtonLink($options)
    {
        $fullLink = ""; 
        
        $visible = array_key_exists('visible', $options) ? (bool)$options['visible'] : true;

        if ($visible)
        {
            $title = array_key_exists('title', $options) ? $options['title'] : "";
            $url = array_key_exists('url', $options) ? $options['url'] : "";
            $image = array_key_exists('image', $options) ? $options['image'] : Yii::app()->theme->baseUrl.'/img/edit.png';
            $tooltipText = array_key_exists('tooltip', $options) ? $options['tooltip'] : "";
            
            if (array_key_exists("linkHtmlOptions", $options) &&
                array_key_exists("class", $options['linkHtmlOptions']))
            {
                $options['linkHtmlOptions']["class"] .= " hideWhenReadOnly";
            }
            else
            {
                $options['linkHtmlOptions']["class"] = "hideWhenReadOnly";
            }
            
            $linkAttributes = array_key_exists('linkHtmlOptions', $options) ? self::renderAttributes($options['linkHtmlOptions']) : "";
            $imageAttributes = array_key_exists('imageHtmlOptions', $options) ? self::renderAttributes($options['imageHtmlOptions']) : "";
            
            $jsOptions = self::getJsOptions($options);

            if ($jsOptions != "")
            {
                $command = "showModalWindow('".$title."', '".$url."', ".$jsOptions.");";
            }
            else
            {
                $command = "showModalWindow('".$title."', '".$url."');";
            }

            $tooltip = $tooltipText != "" ? 'title="'.$tooltipText.'"' : "";

            $img = '<img'.$imageAttributes.' src="'.$image.'" />';
            $link = '<a '.$tooltip.$linkAttributes.' href="" onclick="'.$command.'; return false;" style="margin-left: 5px;">';
            $fullLink = $link.$img.'</a>';
        }
        
        return $fullLink;
    }

    private static function getJsOptions($options)
    {
        $all = array(
             'formId' => array_key_exists('formId', $options) ? $options['formId'] : null,
             'submitUrl' => array_key_exists('submitUrl', $options) ? $options['submitUrl'] : null,
             'onSuccess' => array_key_exists('onSuccess', $options) ? $options['onSuccess'] : null,
             'onError' => array_key_exists('onError', $options) ? $options['onError'] : null,
             'reloadPage' => array_key_exists('reloadPageAfterSubmit', $options) ? (bool)$options['reloadPageAfterSubmit'] : null,
             'data' => array_key_exists('data', $options) ? $options['data'] : null,
             'size' => array_key_exists('size', $options) ? $options['size'] : null,
        );
        
        $filtered = array_filter($all, function($el) { return $el != null; });

        $strings = array();
        $dataStrings = array();
        
        if (array_key_exists('data', $filtered))
        {
            foreach ($filtered['data'] as $key => $value)
            {
                if (mb_substr(mb_strtolower($value), 0, 3) == "js:")
                {
                    $dataStrings[] = "'".$key."': ".mb_substr($value, 3);
                }
                else
                {
                    $dataStrings[] = "'".$key."': '".$value."'";
                }
            }
            
            if (count($dataStrings) == 0)
            {
                unset($filtered['data']);
            }
            else
            {
                $filtered['data'] = "js:{ ".implode(", ", $dataStrings)." }";
            }
        }
        
        foreach ($filtered as $key=>$value)
        {
            if (mb_substr(mb_strtolower($value), 0, 3) == "js:")
            {
                $strings[] = "'".$key."': ".mb_substr($value, 3);
            }
            else
            {
                $strings[] = "'".$key."': '".$value."'";
            }
        }
        
        if (count($strings) == 0)
        {
            return "";
        }
        else
        {
            return "{ ".implode(", ", $strings)." }";
        }
    }
    
    public static function translationTable($values, $options = array(), $inputHtmlOptions = array())
    {
        $baseUrl = Yii::app()->baseUrl; 
        $cs = Yii::app()->getClientScript();
        $cs->registerScriptFile($baseUrl.'/js/translationtable.js');
        
        $showHeader = array_key_exists('showHeader', $options) && $options['showHeader'] == true;
        $headerTitle = array_key_exists('headerTitle', $options) ? $options['headerTitle'] : '';
        unset($options['showHeader']);
        unset($options['headerTitle']);
        
        $inputName = array_key_exists('inputName', $inputHtmlOptions) ? $inputHtmlOptions['inputName'] : "translation";
        unset($inputHtmlOptions['inputName']);
        
        $inputAttributes = self::renderAttributes($inputHtmlOptions);
        $contentAttributes = self::renderAttributes($options);
?>        
        <div class="translation_content" <?php echo $contentAttributes ?>>
        <table class="table table-striped table-bordered table-hover translation_table" style="margin-bottom: 0px">
<?php
    if ($showHeader)
    {
?>
            <thead>
                <tr>
                    <th style="width: 140px;"><?php echo Yii::t('app', 'language'); ?></th>
                    <th><?php echo $headerTitle; ?></th>
                </tr>
            </thead>
<?php            
    }
?>
            <tbody>
                <?php
                 foreach ($values as $value) {
                ?>
                <tr>
                    <td style="width: 140px;">
                        <label><?php echo $value["name"]; ?></label>
                    </td>
                    <td>
                        <input type="text" lang="<?php echo $value["key"] ?>" name="<?php echo $inputName; ?>[<?php echo $value["key"]; ?>]" <?php echo $inputAttributes; ?> value="<?php echo $value["value"]; ?>" />
                        <?php
                        if ($value["showTranslate"]) 
                        {
                            echo "<button type=\"button\" onclick=\"ajaxElementTranslation(this, '" . $value["key"] . "');return false;\"><i class=\"icon-random\"></i></button>";
                            echo "<img src=\"/themes/abound/img/icons/loading.gif\" width=\"16\" height=\"16\" alt=\"L\" class=\"loading_translation\" />";
                        }
                        ?>
                    </td>
                </tr>
                <?php
                 }
                ?>
            </tbody>
        </table>   
        </div>
<?php
    }
}


//                <div class="translation_content" style="display: none">
//                    <table class="table table-striped table-bordered table-hover" style="margin-bottom: 0px">
//                        <tbody>
//                            <?php
//                             foreach ($languages as $language) {
//                            <tr>
//                                <td style="width: 140px;">
//                                    <label> $language->name; </label>
//                                </td>
//                                <td>
//                                    <input type="text" style="width: 500px;" lang=" echo $language->short " onkeyup="translationOnKeyUp(this);" value="" />
//                                    if ($language->short != 'sl') {
//                                        echo "<button type=\"button\" onclick=\"ajaxElementTranslation(this, '" . $language->short . "');return false;\"><i class=\"icon-random\"></i></button>";
//                                        echo "<img src=\"/themes/abound/img/icons/loading.gif\" width=\"16\" height=\"16\" alt=\"L\" class=\"loading_translation\" />";
//                                    }
//                                </td>
//                            </tr>
//                             }
//                        </tbody>
//                    </table>
//                </div>