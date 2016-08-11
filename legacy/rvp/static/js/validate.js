validacija = function () {
    var errors = false;
    alert("here");
    $("fieldset").each(function (index) {
      if($(this).attr('rel')){
        $(this).find('input, select').each(function(){
           if($(this).val() == "0" || $(this).val() == "") errors = true;
        });
      }
      
      if(errors)
      {
        if($(this).attr("rel") && !$(this).find('legend > b').size()) $(this).find('legend').append('&nbsp;<b style="color:red;">'+ $(this).attr("rel") +'</b>')
        window.scrollTo(0, 0);
      }
      else
      {
        $(this).find('legend > b').remove();
      }
    });
    return !errors;
}

$('form').submit(validacija);