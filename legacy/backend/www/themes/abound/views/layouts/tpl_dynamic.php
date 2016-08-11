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

        sortDropDownListByText(dropdownId);

        $('#' + dropdownId).trigger('change');
    }

    function sortDropDownListByText(selectId) {
        var foption = $('#' + selectId + ' option:first');
        var soptions = $('#' + selectId + ' option:not(:first)').sort(function(a, b) {
            return a.text == b.text ? 0 : a.text.toString().localeCompare(b.text) < 0 ? -1 : 1
        });
        $('#' + selectId).html(soptions).prepend(foption);
    }
//]]>
</script>
