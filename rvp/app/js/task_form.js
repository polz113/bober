category_index = 0;

function add_age_group() {
            var index = $("#ageGroupContainter > div").length;
            if (!!index) index = $("#ageGroupContainter > div:last-child").find("select").attr("rel") * 1 + 1;
            var template = $("#ageGroupTemplate").clone(false);
            $(template).show();
            $(template).find("select").attr("name", "age_group[" + index + "]");
            $(template).find("select").attr("rel", index);
            $(template).attr("id", "");
            $(template).attr("class", "ageGroup");
            $(template).find("input").val("");
            $("#ageGroupContainter").append(template);
            $(template).find(".remove_age_group").bind("click", function (e) {
                e.preventDefault();
                $(this).parents(".ageGroup").remove();
            });
        }
        ;

        function add_category() {
            var index = category_index++;
            var template = $("#categoriesTemplate").clone(false);
            $(template).show();
            $(template).find("select").attr("name", "category[" + index + "]");
            $(template).find("select").attr("rel", index);
            $(template).find("input").val("");
            $(template).attr("id", "");
            $(template).attr("class", "category");
            $("#categoriesContainter").append(template);
            $(".remove_category").unbind();
            $(".remove_category").bind("click", function (e) {
                e.preventDefault();
                $(this).parents(".category").remove();
            });
        }
        ;


        $("a.eraseAnswer").bind("click", function (e) {
            e.preventDefault();
            var index = $(this).parents(".input-append").find("input").attr("rel"),
                    item = $(".task_preview ul li")[index];
            $(this).parents(".input-append").find("input").val("");
            $(item).text("");
        });

        $("#title input.title").keyup(function () {
            $(".task_preview h4").text($(this).val());
        });
        $("#body textarea").keyup(function () {
            $(".task_preview p").text($(this).val());
        });
        $("#answers .answer").keyup(function () {
            var index = $(this).attr("rel") * 1;
            var item = $(".task_preview ul li")[index];
            $(item).text($(this).val());
        });


        $("#add_age_group").bind("click", function (e) {
            e.preventDefault();
            add_age_group();
        });

        $("#add_category").bind("click", function (e) {
            e.preventDefault();
            add_category();
        });
