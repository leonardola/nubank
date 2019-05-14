$(document).ready(function () {
    $("#addTagBox .fa-plus-circle").click(function (event) {
        event.stopPropagation();
        $(this).hide();
        $(".addTag").show();
        $(".addTag input").focus();
    });

    $(".addTag input").click(function (event) {
        event.stopPropagation();
    });

    $(".addTag input").change(function (event) {
        event.stopPropagation();
        var newTagName = $(this).val();
        var movementId = $("#addTagBox").attr("movement_id");
        var that = $(this);

        $.post("/addTag/" + movementId, {name: newTagName}, function (data) {
            that.val("");
            $(".addTag").hide();
            $("#addTagBox .fa-plus-circle").show();

            var newTagHtml = "<div tag_id=\"" + data.id + "\" class=\"tag\">" + newTagName + "<i class=\"fas fa-trash-alt\"></i></div>";
            $(newTagHtml).insertBefore("#addTagBox .fa-plus-circle");
        }).fail(function () {
            alert("Erro ao salvar tag");
        });

    });

    var substringMatcher = function (strs) {
        return function findMatches(q, cb) {
            var matches, substringRegex;

            // an array that will be populated with substring matches
            matches = [];

            // regex used to determine if a string contains the substring `q`
            substrRegex = new RegExp(q, 'i');

            // iterate through the pool of strings and for any string that
            // contains the substring `q`, add it to the `matches` array
            $.each(strs, function (i, str) {
                if (substrRegex.test(str)) {
                    matches.push(str);
                }
            });

            cb(matches);
        };
    };

    $.get("/getTags", function (data) {
        $('.addTag input').typeahead({
                hint: true,
                highlight: true,
                minLength: 1
            },
            {
                name: 'states',
                source: substringMatcher(data)
            }
        );
    });

    $(".tags").click(function (event) {
        event.stopPropagation();
        $("#addTagBox").show();
        $("#addTagBox").attr("movement_id", $(this).attr("movement_id"));
    });

    $(document).click(function () {
        $("#addTagBox").hide();
        $(".addTag input").val("");
        $(".addTag").hide();
        $("#addTagBox .fa-plus-circle").show();
    });

    $("#addTagBox").click(function (event) {
        event.stopPropagation();
        $(".addTag input").val("");
        $(".addTag").hide();
        $("#addTagBox .fa-plus-circle").show();
    });
});