function mce_filebrowser(field_name, url, type, win) {
    tinyMCE.activeEditor.windowManager.open({
        url: "/mce_filebrowser/" + type + "/",
        width: 300,
        height: 400,
        movable: true,
        inline: true,
        close_previous: "no"
    }, {
        window : win,
        input : field_name
    });
}
