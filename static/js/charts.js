$(document).ready(function () {
    var ctx = document.getElementById('inNOut').getContext('2d');
    var income = $("#inNOut").attr('income');
    var outcome = $("#inNOut").attr('outcome');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Entrou', 'Saiu'],
            datasets: [{
                label: 'Gastos',
                data: [income, outcome],
                backgroundColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Balanço'
            }
        }
    });

    $.get("/getMovementsByTags", function (data) {

        var tags = [];
        var values = [];
        var color = [];

        var generateDynamicColor = function () {
            var r = Math.floor(Math.random() * 255);
            var g = Math.floor(Math.random() * 255);
            var b = Math.floor(Math.random() * 255);
            return "rgb(" + r + "," + g + "," + b + ")";

        };
        for (var i in data) {
            if (!data.hasOwnProperty(i)) {
                continue;

            }
            tags.push(i);
            values.push(data[i]);
            color.push(generateDynamicColor());

        }

        var ctx = document.getElementById('outs').getContext('2d');
        var income = $("#outs").attr('income');
        var outcome = $("#outs").attr('outcome');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: tags,
                datasets: [{
                    data: values,
                    backgroundColor: color
                }]
            },
            options: {
                maintainAspectRatio: false,
                title: {
                    display: true,
                    text: 'Tags'
                }
            }
        })
    });
});