<?php
/**
 * YDataLinkColumn extends {@link CDataColumn} to facilitate adding
 * links to data values.
 *
 * This is particularly usefull in the backend to go from one entity
 * to the other.
 *
 * YDataLinkColumn 'joins' the {@link CLinkColumn} and {@link CDataColumn}
 * interfaces.
 */
class YDataLinkColumn extends CDataColumn {
 
    public $urlExpression;
    public $url="javascript:void(0)";
    public $linkHtmlOptions=array();
    public $imageUrl;
 
    protected function renderDataCellContent($row, $data) {
        ob_start();
        parent::renderDataCellContent($row, $data);
        $label = ob_get_clean();
 
        if($this->urlExpression!==null)
            $url=$this->evaluateExpression($this->urlExpression,array('data'=>$data,'row'=>$row));
        else
            $url=$this->url;
 
        $options=$this->linkHtmlOptions;
        if(is_string($this->imageUrl))
            echo CHtml::link(CHtml::image($this->imageUrl,$label),$url,$options);
        else
            echo CHtml::link($label,$url,$options);
    }
}
?>