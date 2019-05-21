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

    $(".filter").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $(".movementsList tr").filter(function () {
            if ($(this).find(".nameInput").length) {
                $(this).toggleClass("showingRow", $(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
                $(this).toggle($(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
            }

        });
    });

    $("#addMovement").click(function (event) {
        event.stopPropagation();
        $("#addMovementBox").show();
    })

    $("#addMovementBox").click(function (event) {
        event.stopPropagation();
    })

    $(document).click(function () {
        $("#addMovementBox").hide();
    })
});