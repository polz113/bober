<div class="test_set">
    <div class="q_top">
        <div id="title_and_timer">
            <h1 id="competition_title"><?php echo Yii::t('app', 'Loading...'); ?></h1>
        </div>
        <div class="collumns">
            <div class="column1">
                <div class="qbartop">
                    <ul class="task_navigation">
                        <div style="display: none;" class="point_template">
                            <li class="point"><a href="#"></a></li>
                        </div>
                    </ul>
                </div>
                <div class="answeredStats hide-controls">
                    <?php echo Yii::t('app', 'Answered'); ?>:&nbsp;<span id="answered_count"></span>&nbsp;/&nbsp;<span id="answers_count"></span>
                </div>
            </div>
            <div class="column2">
                <div class="header_controls">
                    <div id="answered" class="hide-controls">
                        <div class="countdown_wrapper countdown_counter">
                            <span id="countdown_title"><?php echo Yii::t('app', 'Time Left') ?>:</span><br />
                            <span class="time"><span class="minutes">00</span>&nbsp;<span class="time_enota">min</span></span>
                        </div>
                    </div>
                    <div id="ending" class="hide-controls">
                        <a href="#" id="end_quiz" onclick="finish_competition();
                                return false;"><?php echo Yii::t('app', 'Finish competition'); ?></a>
                    </div>
                </div>
            </div>
            <div class="clearfix"></div>
        </div>
        <?php
        /*
          <div class="header_warning_msg hide-controls">
          <?php echo Yii::t('app', 'Do not forget to press "Save Answer" otherwise your answer won\'t be saved!'); ?>
          </div>
         */
        ?>
    </div>

    <div class="task_header hide-controls">
        <div class="middlebar">
            <span class="task_name"></span><span id="task_country"></span>
            <input style="float: right;" type="button" value="<?php echo Yii::t('app', 'Clear Answer'); ?>" class="btn" onclick="return resetResponse();" />
            <div id="bottom_msg"></div>
        </div>
    </div>

    <div class="question" id="questions">
        <div id="progressbar"><div class="progress-label"><?php echo Yii::t('app', 'Loading...'); ?></div></div>
    </div>
</div>

<div class="podbar hide-controls" style="display: none;">
    <div class="bottombar">
        <?php
        /*
          <input type="button" value="<?php echo Yii::t('app', '<<'); ?>" class="btn" onclick="return previousQuestion();" />
          <input id="submitanswer" type="button" name="commit" value="<?php echo Yii::t('app', 'Save Answer'); ?>" onclick="return saveResponse(); return false;" class="btn" />
         */
        ?>
        <input type="button" value="<?php echo Yii::t('app', 'Clear Answer'); ?>" class="btn" onclick="return resetResponse();" />
        <?php
        /*
          <input type="button" value="<?php echo Yii::t('app', '>>'); ?>" class="btn" onclick="return nextQuestion();" />
         */
        ?>
        <div id="bottom_msg"></div>
    </div>
</div>

<script type="text/javascript">
    //<![CDATA[
    var root_url = "<?php echo Yii::app()->baseUrl; ?>";
    var images_url ="<?php echo Yii::app()->theme->baseUrl . '/img'; ?>";
    var question_data = [];
    var current_selected_question = 0;
    var controlsEnabled = true;
    var answers = {};
    var questionLoaded = {};
    var progressbar, progressLabel;
    var counterStarted = false;
    var counterTimer = 0;
    var counterRedBeforeEndTimeSeconds = 5 * 60; // 5 minut
    var enabledConfirmExit = false;
    var countAllQuestions = 0;
    var callback_question_id = 0;
    var timers = {};

    // prevent refresh without saving
    window.onbeforeunload = confirmExit;
    function confirmExit() {
        if (enabledConfirmExit) {
            saveResponse();
            GAPushEvent("ExitBrowserOrBrowserRefresh", "confirm")
            return "<?php echo Yii::t('app', 'You have attempted to leave this page. Your last question answer will be saved automatically. Are you sure you want to exit this page?'); ?>";
        }
    }

    function cleanupLastQuestionCookie() {
        jQuery.removeCookie('current_selected_question');
    }

    function LoadQuestions() {
        timers.loadQuestionTimer = new Date().getTime() / 1000;
        GAPushEvent("CompetitionQuestionLoading", "start")
        progressbar = $("#progressbar")
        progressLabel = $(".progress-label");
        progressbar.progressbar({
            "value": false,
            "change": function() {
                progressLabel.text(progressbar.progressbar("value") + "%");
            },
            "complete": function() {
                progressLabel.text("<?php echo Yii::t('app', 'Complete!'); ?>");
            }
        });
        jQuery.ajax({
            "url": root_url + "/CompetitionService/GetQuestions",
            "type": "GET",
            "dataType": "JSON",
            "cache": false,
            "success": function(allData) {
                if (allData["success"]) {
                    // testing
                    // allData['questions'] = [allData['questions'][0], allData['questions'][1]];
                    countAllQuestions = allData['questions'].length;
                    jQuery("#competition_title").empty().append(allData['competition_title']);
                    jQuery("title").empty().append("<?php echo Yii::t('app', 'Beaver'); ?> :: " + allData['competition_title']);
                    if (allData["seconds_to_end"] === -1) {
                        cleanupLastQuestionCookie();
                    }
                    var data = allData['questions'];

                    // previous question
                    var el = jQuery('.point_template .point').clone();
                    var a = jQuery(el).find('a');
                    jQuery(a).attr('id', 'previous_button');
                    jQuery(a).attr('href', '#');
                    jQuery(a).addClass("navigation");
                    jQuery(a).bind('click', function() {
                        previousQuestion();
                        return false;
                    });
                    jQuery(a).html("<");
                    jQuery("ul.task_navigation").append(el);

                    for (var i = 0; i < data.length; ++i) {
                        // console.log(data[i]);
                        var el = jQuery('.point_template .point').clone();
                        // link
                        var a = jQuery(el).find('a');
                        a.attr('id', 'question_button_' + data[i]["id"]);
                        a.bind('click', function() {
                            if (controlsEnabled) {
                                var splited = this.href.split('#')
                                var current_selected_question_local = parseInt(splited[1], 10);
                                loadQuestion(current_selected_question_local);
                                // updateIframeSize();
                                GAPushEvent("CompetitionNavigation", "clickedDirectly");
                            }
                            return false;
                        });
                        jQuery(a).attr('href', '#' + data[i]["id"].toString());
                        jQuery(a).html((i + 1).toString());
                        questionLoaded[data[i]["id"]] = false;
                        question_data[data[i].id] = data[i];
                        checkIfAllTasksLoaded();
                        var iframe = jQuery('<iframe />');
                        iframe.attr('src', root_url + '/questionResource/get/' + data[i]["link"]);
                        iframe.addClass('naloga');
                        iframe.addClass('naloga_hide');
                        iframe.attr('id', 'naloga_' + data[i]["id"]);
                        iframe.appendTo(jQuery('#questions'));
                        iframe.bind('load', function() {
                            var splited = jQuery(this).attr('id').split('_');
                            var question_id = splited[1];
                            document.getElementById('naloga_' + question_id).contentWindow.task.load(question_data[question_id]["random_seed"], 1);
                            document.getElementById('naloga_' + question_id).contentWindow.task.reloadAnswer(answers[question_id]);
                            markQuestionAsAnswered(question_id, answers[question_id]);
                            questionLoaded[question_id] = true;
                            checkIfAllTasksLoaded();
                            if (question_data[question_id]["css"] && question_data[question_id]["css"] !== '') {
                                pushStyleToIframe(document.getElementById('naloga_' + question_id).contentWindow, question_data[question_id]["css"]);
                            }
                            GAPushEvent("CompetitionQuestionLoading", "questionLoaded");
                        });
                        answers[data[i]["id"]] = data[i]["custom_answer"];
                        jQuery("ul.task_navigation").append(el);
                    }

                    // next question
                    var el = jQuery('.point_template .point').clone();
                    var a = jQuery(el).find('a');
                    jQuery(a).attr('id', 'next_button');
                    jQuery(a).attr('href', '#');
                    jQuery(a).addClass("navigation");
                    jQuery(a).bind('click', function() {
                        nextQuestion();
                        return false;
                    });
                    jQuery(a).html(">");
                    jQuery("ul.task_navigation").append(el);

                    if (current_selected_question === 0) {
                        current_selected_question = data[0].id;
                    }
                    updateAnsweredQuestionCountDisplay();
                } else {
                    if (allData['errorCode'] && allData['errorCode'] === 999) {
                        onCompetitionNoTimeLeft();
                    } else {
                        alert(allData['error']);
                    }
                }
            }
        });
    }

    function pushStyleToIframe(doc, css) {
        var head = doc.document.getElementsByTagName('head')[0];
        var style = doc.document.createElement('style');
        style.type = 'text/css';
        if (style.styleSheet) {
            style.styleSheet.cssText = css;
        } else {
            style.appendChild(doc.document.createTextNode(css));
        }
        head.appendChild(style);
    }

    function markQuestionAsAnswered(question_id, answer) {
        if (answer === '') {
            jQuery("#question_button_" + question_id).removeClass("question_answered");
        } else {
            jQuery("#question_button_" + question_id).addClass("question_answered");
        }
    }

    function GetTimeToEndOfCompetition() {
        jQuery.ajax({
            "url": root_url + "/CompetitionService/GetTimeToEndOfCompetition",
            "type": "GET",
            "dataType": "JSON",
            "cache": false,
            "success": function(allData) {
                GAPushEvent("CompetitionTimer", "update");
                if (allData["success"]) {
                    var seconds_to_end = allData['seconds_to_end'];
                    // console.log(seconds_to_end);
                    if (counterStarted) {
                        jQuery(".countdown_counter").jCounter('stop');
                        clearTimeout(counterTimer);
                    }
                    var secondsToTimeout = seconds_to_end - counterRedBeforeEndTimeSeconds;
                    changeColorOfTime('black');
                    if (secondsToTimeout > 0) {
                        counterTimer = setTimeout("changeColorOfTime('red')", (secondsToTimeout) * 1000);
                    } else {
                        changeColorOfTime('red');
                    }
                    // console.log(seconds_to_end);
                    if (seconds_to_end > 60) {
                        jQuery(".seconds").addClass("minutes").removeClass("seconds");
                        var custom_duration = seconds_to_end.toString() + ":60";
                        // console.log(custom_duration);
                        jQuery(".countdown_counter").jCounter({
                            "animation": "slide",
                            "format": "mm",
                            "twoDigits": 'off',
                            // "customDuration": seconds_to_end,
                            "serverDateSource": '',
                            "customRange": custom_duration,
                            "callback": function() {
                                GetTimeToEndOfCompetition();
                            }
                        });
                    } else {
                        if (counterStarted) {
                            jQuery(".countdown_counter").jCounter('stop');
                            clearTimeout(counterTimer);
                        }
                        jQuery(".minutes").addClass("seconds").removeClass("minutes");
                        jQuery(".time_enota").html("s");
                        jQuery(".countdown_counter").jCounter({
                            "animation": "slide",
                            "format": "ss",
                            "twoDigits": 'off',
                            "customDuration": seconds_to_end,
                            "serverDateSource": '',
                            "callback": function() {
                                onCompetitionNoTimeLeft();
                            }
                        });
                    }
                    counterStarted = true;
                    enabledConfirmExit = true;
                } else {
                    if (allData['errorCode'] && allData['errorCode'] === 9) {
                        onCompetitionNoTimeLeft();
                    } else {
                        alert(allData['error']);
                    }
                }
            }
        });
    }

    function changeColorOfTime(color) {
        jQuery(".time").css('color', color);
    }

    function checkIfAllTasksLoaded() {
        var count = 0;
        var count_all = 0;
        for (var key in questionLoaded) {
            if (questionLoaded[key]) {
                count++;
            }
            count_all++;
        }
        for (var key2 in question_data) {
            count++;
        }
        count_all = count_all + countAllQuestions;
        var progress = Math.round(count / count_all * 10000.0) / 100.0;
        progressbar.progressbar("value", progress);
        if (count === count_all) {
            GAPushEventExtended("CompetitionQuestionLoading", "finished", "Finished loading questions", (new Date().getTime() / 1000)-timers.loadQuestionTimer);
            // jQuery('#loader1').hide();
            progressbar.hide();
            if (jQuery.cookie("current_selected_question")) {
                current_selected_question = jQuery.cookie("current_selected_question");
            }
            loadQuestion(current_selected_question, true);
            jQuery('.hide-controls').removeClass('hide-controls');
            GetTimeToEndOfCompetition();
            setInterval("GetTimeToEndOfCompetition()", 5 * 60 * 1000);
        }
    }

    function onCompetitionNoTimeLeft() {
        GAPushEvent("CompetitionFinished", "timeout");
        enabledConfirmExit = false;
        cleanupLastQuestionCookie();
        alert("<?php echo Yii::t('app', 'Your are out of time for solving competition.'); ?>");
        window.close();
        window.location = root_url + '/StartCompetition';
    }

    function loadQuestionPreviousSaved() {
        loadQuestion(callback_question_id, true);
    }

    function loadQuestion(question_id, saved) {
        if (saved) {
            current_selected_question = question_id;
            jQuery.cookie('current_selected_question', current_selected_question);
            DisableEnableControls(false);
            var naloga = jQuery('#naloga_' + question_id);
            if (!naloga) {
                alert('Missing HTML element for task.');
            }

            jQuery('.naloga').each(function() {
                if (!jQuery(this).hasClass('naloga_hide')) {
                    jQuery(this).fadeOut(500);
                    jQuery(this).delay(500).addClass('naloga_hide');
                }
            });

            naloga.removeClass('naloga_hide');
            jQuery('.point a').removeClass('currentQuestion');
            jQuery("#question_button_" + question_id).addClass("currentQuestion");

            DisableEnableControls(true);

            jQuery(naloga).fadeIn(300, "swing", updateIframeSize);
            jQuery(".task_name").html(jQuery("#question_button_" + question_id).text() + ". " + question_data[question_id]["title"]);
            jQuery("#task_country").html("<img src=\""+images_url + "/flags-iso/flat/32/"+ question_data[question_id]["country"] + ".png\" alt=\""+question_data[question_id]["country"]+"\"/>");
            return true;
        } else {
            callback_question_id = question_id;
            saveResponse(loadQuestionPreviousSaved);
        }
    }

    function DisableEnableControls(enable) {
        // console.log('Controls: ', enable);
        controlsEnabled = enable;
        if (enable) {
            jQuery('a').unbind("click.myDisable");
            jQuery('input').unbind("click.myDisable");
        } else {
            jQuery('a').bind("click.myDisable", function() {
                return false;
            });
            jQuery('input').bind("click.myDisable", function() {
                return false;
            });
        }
    }

    function saveResponse(callback) {
        if (controlsEnabled) {
            var saved_msg = "<?php echo Yii::t('app', 'Your answer was successfully saved!'); ?>";
            var cleaned_msg = "<?php echo Yii::t('app', 'Your answer was successfully cleared!'); ?>";
            var answer = document.getElementById('naloga_' + current_selected_question).contentWindow.task.getAnswer();
            DisableEnableControls(false);
            jQuery.ajax({
                "url": root_url + "/CompetitionService/SaveResponse",
                "type": "POST",
                "data": {"q": current_selected_question, "a": answer},
                "dataType": "JSON",
                "cache": false,
                "success": function(data) {
                    GAPushEvent("CompetitionQuestionSaving", "clicked");
                    if (data["success"]) {
                        answers[current_selected_question] = answer;
                        updateAnsweredQuestionCountDisplay();
                        var msg = '';
                        if (data["same_in_db"]) {
                            // same in db, do not show message
                        } else {
                            msg = answer === '' ? cleaned_msg : saved_msg;
                        }
                        markQuestionAsAnswered(current_selected_question, answer);
                        jQuery("#bottom_msg").empty().append(msg);
                        jQuery("#bottom_msg").fadeIn('fast', function() {
                            setTimeout(function() {
                                $("#bottom_msg").fadeOut('slow');
                            }, 5000);
                        });
                    } else {
                        if (data['errorCode'] && data['errorCode'] === 999) {
                            onCompetitionNoTimeLeft();
                        } else {
                            alert(data["error"]);
                        }
                    }
                },
                "complete": function() {
                    DisableEnableControls(true);
                    if (callback) {
                        callback();
                    }
                }
            });
        }
    }

    function updateAnsweredQuestionCountDisplay() {
        var count = updateAnsweredQuestionCount();
        jQuery('#answered_count').empty().append(count["count"].toString());
        jQuery('#answers_count').empty().append(count["all"].toString());
    }

    function updateAnsweredQuestionCount() {
        var count = 0;
        var count_all = 0;
        for (var key in answers) {
            if (answers[key] !== '') {
                count++;
            }
            count_all++;
        }
        return {"count": count, "all": count_all};
    }

    function resetResponse() {
        if (controlsEnabled) {
            if (confirm("<?php echo Yii::t('app', 'Are you sure you want to clear answer?'); ?>")) {
                document.getElementById('naloga_' + current_selected_question).contentWindow.task.reloadAnswer("");
                saveResponse();
                GAPushEvent("CompetitionQuestionReset", "clicked");
            }
        }
    }

    function nextQuestion(saved) {
        if (controlsEnabled) {
            jQuery("#question_button_" + current_selected_question).parent().next().find('a:not(.navigation)').click();
            GAPushEvent("CompetitionNavigation", "clickedNext");
        }
    }

    function previousQuestion(saved) {
        if (controlsEnabled) {
            jQuery("#question_button_" + current_selected_question).parent().prev().find('a:not(.navigation)').click();
            GAPushEvent("CompetitionNavigation", "clickedPrevious");
        }
    }

    String.prototype.format = function() {
        var formatted = this;
        for (arg in arguments) {
            formatted = formatted.replace("{" + arg + "}", arguments[arg]);
        }
        return formatted;
    };

    function finish_competition_saved() {
        finish_competition(true);
    }

    function finish_competition(saved) {
        if (saved) {
            var confirm_msg = "";
            var count = updateAnsweredQuestionCount();
            if (count['count'] !== count['all']) {
                var unanswered = count['all'] - count['count'];
                confirm_msg += "<?php echo Yii::t('app', 'You left {0} unanswered {1}.') ?>".format(unanswered, unanswered > 1 ? "<?php echo Yii::t('app', 'questions'); ?>" : "<?php echo Yii::t('app', 'question'); ?>");
            }
            confirm_msg += " <?php echo Yii::t('app', 'Are you sure that you want to finish competition?'); ?>";

            if (confirm(confirm_msg)) {
                GAPushEvent("CompetitionFinished", "clicked");
                DisableEnableControls(false);
                enabledConfirmExit = false;
                cleanupLastQuestionCookie();
                jQuery.ajax({
                    "url": root_url + "/CompetitionService/FinishCompetition",
                    "type": "POST",
                    "data": {"finish": true},
                    "dataType": "JSON",
                    "cache": false,
                    "success": function(data) {
                        if (data["success"]) {
                            alert("<?php echo Yii::t('app', 'Thank you for your participation in competition!'); ?>");
                        } else {
                            alert(data["error"]);
                        }
                    },
                    "error": function() {
                        alert("<?php echo Yii::t('app', 'An error has occured. Please try to finish competition again.'); ?>");
                    },
                    "complete": function() {
                        DisableEnableControls(true);
                        window.close();
                        window.location = root_url + '/StartCompetition';
                    }
                });
            }
        } else {
            GAPushEvent("CompetitionFinished", "confirm");
            saveResponse(finish_competition_saved);
        }
    }

    function updateIframeSize() {
        // update to windows size
        // jQuery("#naloga_" + current_selected_question).css('height', (jQuery(window).height() - 310) + 'px');
        // maximize to size of iframe
        var height = Math.max(jQuery("#naloga_" + current_selected_question).contents().height(), jQuery(window).height() - 307);
        // console.log("update iframe size, naloga: " + current_selected_question, "height: " + height);
        jQuery("#naloga_" + current_selected_question).css('height', height+"px");
    }

    function hideFooter() {
        jQuery('footer').hide();
        jQuery('#footer_wrapper').hide();
    }

    function clickIE() {
        if (document.all) {
            return false;
        }
    }
    function clickNS(e) {
        if (document.layers || (document.getElementById && !document.all)) {
            if (e.which == 2 || e.which == 3) {
                return false;
            }
        }
    }
    function disableMouseLeftClick() {
        if (document.layers) {
            document.captureEvents(Event.MOUSEDOWN);
            document.onmousedown = clickNS;
        } else {
            document.onmouseup = clickNS;
            document.oncontextmenu = clickIE;
        }
        document.oncontextmenu = function() {
            return false;
        };
    }

    jQuery(document).ready(function() {
        hideFooter();
        LoadQuestions();
        jQuery(window).resize(function() {
            updateIframeSize();
        });
        disableMouseLeftClick();
    });
    //]]>
</script>
