<script type="text/javascript">
//<![CDATA[
    function loadDropdown(dropdownId, items, selectedItemKey)
    {
        $('#' + dropdownId).empty();

        $('#' + dropdownId).append($('<option></option>').attr('value', '').attr('selected', 'selected').text('<?php echo Yii::t('app', 'choose'); ?>'));

        if (items != null)
        {
            $.each(items, function(k, v) {
                if (k == selectedItemKey)
                {
                    $('#' + dropdownId).append($('<option></option>').attr('value', k).attr('selected', 'selected').text(v));
                }
                else
                {
                    $('#' + dropdownId).append($('<option></option>').attr('value', k).text(v));
                }
            });        
        }
        
        $('#' + dropdownId).trigger('change');
    }    
//]]>
</script>
      