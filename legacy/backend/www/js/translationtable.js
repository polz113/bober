function ajaxElementTranslation(button, languageTo)
{
    var slovenianValue = $(button).closest(".translation_content").find("input[lang='sl']").val();

    $(button).siblings(".loading_translation").css('display' ,'inline');

    if (slovenianValue != '')
    {
        $.get('/index.php/ajaxTranslation/?from=sl&to='+languageTo+'&text='+encodeURI(slovenianValue), function(data) {
            if (data != '') {
                $(button).siblings("input").val(data);
            }

            $(button).siblings(".loading_translation").css('display' ,'none');
        });
    }
}