<div class="modal hide fade" id="modalWindow">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal">×</button>
    <h3></h3>
  </div>
  <div class="modal-body">
      <div id="modalWindow_loading" style="text-align: center; margin: auto; margin-top: 20px; margin-bottom: 20px;" >
          <img src="<?php echo Yii::app()->theme->baseUrl; ?>/img/icons/loading.gif" width="16" height="16" alt="L" />
      </div>
      <div id="modalWindow_content"></div>
  </div>
  <div class="modal-footer">
    <div id="modalWindow_required" class="pull-left" style="display: none">
        <?php echo Yii::t('app', 'fields_with_asterisk_are_required'); ?>
    </div>
    <div id="modalWindow_submitting" class="pull-left" style="display: none">
        <img src="<?php echo Yii::app()->theme->baseUrl; ?>/img/icons/loading.gif" width="16" height="16" alt="L" />
        <?php echo Yii::t('app', 'submitting'); ?>
    </div>
    <a href="#" id="modalWindow_submit" class="btn btn-primary"><?php echo Yii::t('app', 'save'); ?></a>
    <a href="#" id="modalWindow_close" class="btn" data-dismiss="modal"><?php echo Yii::t('app', 'close'); ?></a>
  </div>
</div>

<script type="text/javascript">
//<![CDATA[
    $('#modalWindow').on('hidden', clearModalWindow);
    
    function showModalWindow(title, url, options)
    {
        if (!options.saveUrl)
        {
            options.url = url;
        }
        
        if (!options.data)
        {
            options.data = "";
        }
        
        if (options.size)
        {
            if (options.size == "large")
            {
                $('#modalWindow').attr("style", "width: 1045px; margin: -250px 0 0 -515px; top: 40%");
                $('#modalWindow .modal-body').attr("style", "max-height: 500px");
            }
            else
            {
                $('#modalWindow').attr("style", "width: 56px; margin: -250px 0 0 -280px; top: 50%");
                $('#modalWindow .modal-body').attr("style", "max-height: 400px");
            }
            
            options.style="";
        }
        
        $("#modalWindow .modal-header h3").html(title);

        $('#modalWindow').on('shown', function() { loadModalWindowContent(url, options.data); });
        $('#modalWindow_submit').on('click', function() { submitModalWindowForm(options); return false; });
        $('#modalWindow_close').on('click', closeModalWindow);
        
        $('#modalWindow').modal('show');
    }
    
    function closeModalWindow()
    {
        $('#modalWindow').modal('hide');
        
        $('#modalWindow').off('shown');
        $('#modalWindow_submit').off('click');
        $('#modalWindow_close').off('click');
    }
    
    function clearModalWindow()
    {
        $('#modalWindow_content').html("");
        $('#modalWindow_loading').css('display', 'block');
        $('#modalWindow_submitting').css('display', 'none');
        $('#modalWindow_required').css('display', 'none');
    }
    
    function loadModalWindowContent(url, data) {
        jQuery.ajax({
            'url': url,
            'type': 'get',
            'data': data,
            'success':function(response) {
                $('#modalWindow_content').html(response);
                $('#modalWindow_loading').css('display', 'none');
                $('#modalWindow_submitting').css('display', 'none');
                $('#modalWindow_required').css('display', 'block');
                
                initializeFancyCheckboxes('#modalWindow_content');
             },
             'cache': false
        });
    }  
    
    function submitModalWindowForm(options)
    {
        $('#modalWindow_required').css('display', 'none');
        $('#modalWindow_submitting').css('display', 'block');

        var requestData = options.formId ? $("#" + options.formId).serialize() : null;

        jQuery.ajax({
            'url': options.url,
            'type': 'post',
            'data': requestData,
            'dataType' : 'json',
            'success':function(responseData) 
            {
                console.log(responseData);
                
                if (!responseData.error)
                {
                    closeModalWindow();
                    
                    if (options.onSuccess)
                    {
                        options.onSuccess(responseData);
                    }

                    if (options.reloadPage)
                    {
                        window.location.reload();
                    }
                }
                else
                {
                    $('#modalWindow_submitting').css('display', 'none');
                    $('#modalWindow_required').css('display', 'block');
                    $('#modalWindow_content').html(responseData);
                }
            },
            'error':function(responseData) 
            { 
                if (options.onError)
                {
                    options.onError(responseData);
                }
                else
                {
                    // if error occured
                    alert("Error occured. Please try again.");
                }
            },
            'cache':false
        });
    }
//]]>
</script>