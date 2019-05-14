$(document).ready(function () {
    $(".hideMovement").click(function () {
        var that = $(this);
        $.post("/removeMovement/" + $(this).attr("movement_id"), function () {
            that.parent().parent().fadeOut(500, function () {
                $(this).remove();
                var totalValue = 0;
                $(".value").each(function () {
                    totalValue += parseFloat($(this).attr("value"))
                });

                $(".totalValue").html("R$ " + totalValue.toFixed(2).toString())
            })
        })
    });

    $('.monthsWrapper').slick({
        infinite: false,
        slidesToShow: 7.5,
        slidesToScroll: 3,
        arrows: false
    });

    $(".nameInput").change(function () {
        var data = {newName: $(this).val()};
        $.post("/changeMovementName/" + $(this).attr("movement_id"), data)
    });

    var ctx = document.getElementById('myChart').getContext('2d');
    var income = $("#myChart").attr('income');
    var outcome = $("#myChart").attr('outcome');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Entrou', 'Saiu'],
            datasets: [{
                label: 'Gastos',
                data: [income, outcome],
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

    $(".filter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $(".movementsList tr").filter(function () {
            if ($(this).find(".nameInput").length) {
                $(this).toggleClass("showingRow", $(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
                $(this).toggle($(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
            }

        });
    });

    $("#addTagBox .fa-plus-circle").click(function () {
        $(this).hide();
        $(".addTag").show();
        $(".addTag input").focus();
    });

    $(".addTag input").change(function () {
        var newTagName = $(this).val();
        var that = $(this);
        $.post("/addTag", {name: newTagName}, function (data) {
            that.val("");
            that.parent().hide();
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

    $('.addTag input').typeahead({
            hint: true,
            highlight: true,
            minLength: 1
        },
        {
            name: 'states',
            source: substringMatcher(['asdf', 'abc'])
        }
    );

});