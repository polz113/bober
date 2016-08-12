
tinymce.PluginManager.add('nalaganje_slik', function(editor, url) {
  function show() {
    window.picUrl = false;
    window.picName = false;
      editor.windowManager.open({
          title: 'Nalaganje slik',
          width:400,
          height:300,
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
            var img = $('<img height=100 width=100 />')
            editor.insertContent('<img src="'+ window.picUrl +'" height=100 width=100 />');          
          }
      });

      var a = $(".mce-fileUploader");
      $(a).find('input').remove();
      $(a).append('<input type="file" name="images" id="images" multiple />');
      
      var b = $(".mce-filePreview");
      $(b).height(200)
      $(b).find('input').remove();
      $(b).append('<img id="preview"  style="width:400px; height:200px;"/>');
      
      
    new AjaxUpload('images', {
      action: '/upload/'+window.task_id,
      name: 'images',
      onSubmit: function(file, extension) {},
      onComplete: function(file, response) {
        response = JSON.parse(response)
        window.picUrl  = "/resources/uploads/" + response.filename;
        window.picName = response.filename;
        $('img#preview').attr('src', window.picUrl);
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
  max_height: 200,
  min_height: 160,
  height : 180  
});
