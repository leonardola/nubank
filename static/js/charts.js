$(document).ready(function () {
    var ctx = document.getElementById('inNOut').getContext('2d');
    var income = $("#inNOut").attr('income');
    var outcome = $("#inNOut").attr('outcome');
    new Chart(ctx, {
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

    $.get("/getMovementsByTags", function (data) {

        var tags = [];
        var values = [];

        for (var i in data) {
            if (!data.hasOwnProperty(i)) {
                continue;
            }

            tags.push(i);
            values.push(data[i]);
        }

        var ctx = document.getElementById('outs').getContext('2d');
        var income = $("#outs").attr('income');
        var outcome = $("#outs").attr('outcome');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: tags,
                datasets: [{
                    label: 'Gastos',
                    data: values,
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
        })
    });

});