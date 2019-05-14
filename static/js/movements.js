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

                $(".totalValue").html("R$ "+ totalValue.toFixed(2).toString())
            })
        })
    })

    $('.monthsWrapper').slick({
        infinite: false,
        slidesToShow: 7.5,
        slidesToScroll: 3,
        arrows: false
    });

    $(".nameInput").change(function () {
        var data = {newName: $(this).val()};
        $.post("/changeMovementName/"+ $(this).attr("movement_id"), data)
    })

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

    $(".filter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".movementsList tr").filter(function() {
            if($(this).find(".nameInput").length){
                $(this).toggleClass("showingRow", $(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
                $(this).toggle($(this).find(".nameInput").val().toLowerCase().indexOf(value) > -1)
            }

        });
    });


});