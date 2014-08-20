
tinymce.PluginManager.add('nalaganje_slik', function(editor, url) {
  function show() {
    window.picUrl = false;
    window.picName = false;
      editor.windowManager.open({
          title: 'Nalaganje slik',
          width:400,
          height:500,
          body: [
                {
                    classes: "fileUploader",
                    name: "src",
                    type: "filepicker",
                    filetype: "image",
                    autofocus: !0
                },
                {
                    classes: "filePreview",
                    name: "src",
                    type: "filepicker",
                    filetype: "image",
                    autofocus: !0,
                    style: 'height:200px;'
                }
          ],
          onsubmit: function(e) {
            var img = $('<img  class="1" />')
            editor.insertContent('<img src="'+ window.picUrl +'" class="2" />');
          }
      });

      var a = $(".mce-fileUploader");
      $(a).find('input').remove();
      $(a).append('<input type="file" name="images" id="images" multiple />');
      
      var b = $(".mce-filePreview");
      $(b).height(200)
      $(b).find('input').remove();
      $(b).append('<img id="preview"  style="max-width: 360px; max-height: 400px;"/>');
      
      
    new AjaxUpload('images', {
      action: '/upload/'+task_translation_id,
      name: 'images',
      onSubmit: function(file, extension) {},
      onComplete: function(file, response) {
        response = JSON.parse(response)
        window.picUrl  = response.filepath + response.filename;
        window.picName = response.filename;
        $('img#preview').attr('src', tinyMCEbaseURL+window.picUrl);
      }
    });
  }
  
	editor.addButton('nalaganje_slik', {
    icon: "image",
    tooltip: "Insert/edit image",
    onclick: show,
    stateSelector: "img:not([data-mce-object])"
	});

	editor.addMenuItem('nalaganje_slik', {
    icon: "image",
    text: "Insert image",
    onclick: show,
    context: "insert",
    prependToContext: !0
	});
});


tinyMCE.init({
  selector: "textarea",
  plugins: [
    "advlist autolink lists link charmap print preview anchor",
    "searchreplace visualblocks code fullscreen",
    "insertdatetime media table contextmenu paste nalaganje_slik"
  ],
  toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link nalaganje_slik",
  autosave_ask_before_unload: false,
  document_base_url: tinyMCEbaseURL
});
