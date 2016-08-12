var task = {
    /*This is called after the task html has been loaded into the DOM
     The parameter randomSeed is an integer that can used to shuffle choices or add other types randomness
     The field mode is a string and can have 2 values: "question" or "solution"
     question => means that only the task content are loaded, and user is expected to find the answer without any help
     sloution => means that the solution is displayed, so both the task and solution contents are loaded in the page
     */
    load: function(randomSeed, mode) {
        task.randomizeAnswers(randomSeed);
    },
    
    /*This is called befor the task html has been removed from the DOM 
     It a retuns boolean, if the task is ready to unload 
     false => the platform is expected to try again one second later
     true => the second attempt should always return true
     */
    unload: function() {

        return true;
    },
    
    /**
     * Returns current task answer
     * 
     * @returns {String|@exp;@call;jQuery@call;val}
     */
    getAnswer: function() {
        var answer = jQuery("input[name='answer']:checked");
        if (answer.length > 0) {
            return jQuery(answer[0]).val();
        } else {
            return '';
        }
    },
    
    /*
     * It is called previously saved answer is loaded.
     * It can be used if the existing answer is deleted by the platform for some reason
     */
    reloadAnswer: function(answer) {
        if (answer) {
            jQuery("input[name='answer']").each(function() {
                if (jQuery(this).val() === answer) {
                    jQuery(this).prop('checked', true);
                }
            });
        } else {
            jQuery("input[name='answer']").prop('checked', false);
        }
    },
    
    /*display some standar message or button within the task. 
     type may have the following values
     -"validate": the html is a validate button
     -"cancel": the html is a cancel button
     -"saved": the message indicates that the answer has been saved
     -"changed": the message indicates that the answer has been changed
     -"deleted": the message indicates taht the answer has been deleted
     
     The validate button should call platformValidate('next'), when actived
     The cancel button chould call taskReloadAnswer(), platform('stay'), when actived
     If isOption parameter is true, it means that can choose not to display the content
     */
    displayMessage: function(type, html, isOptional) {
        if (type === 'validate') {
            // no idea what
        } else if (type === 'cancel') {
            if (confirm('Ali želite poenostaviti odgovore?')) {
                task.reloadAnswer('');
            }
        } else if (type === 'saved') {
            // ni potrebno povedat userju
        } else if (type === 'changed') {
            // no idea what
        } else if (type === 'deleted') {
            // odgovor izbrisan
        }
    },
    
    /**
     * Function that does cycle randomization based on supplied seed
     * 
     * @param float seed Value between 0..1
     */
    randomizeAnswers: function(seed) {
        seed = Math.round(seed * 100);
        var list = jQuery("input[name='answer']");
        var start = seed % jQuery(list).length;
        for (var i = start; i < jQuery(list).length; i++) {
            var input = jQuery(list[i]);
            var label = jQuery("label[for='" + jQuery(list[i]).attr('id') + "']");
            var parent = jQuery(input).parent();
            jQuery(input).remove();
            jQuery(label).remove();
            jQuery(parent).append(jQuery(input));
            jQuery(parent).append(jQuery(label));
        }
        for (var i = 0; i < start; i++) {
            var input = jQuery(list[i]);
            var label = jQuery("label[for='" + jQuery(list[i]).attr('id') + "']");
            var parent = jQuery(input).parent();
            jQuery(input).remove();
            jQuery(label).remove();
            jQuery(parent).append(jQuery(input));
            jQuery(parent).append(jQuery(label));
        }
    }
};