const Plots = {
    config: null,
    linePlot: null,
    chartColors: {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(75, 192, 192)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(201, 203, 207)'
    },
    timeFormat: 'HH:mm:ss',
    init: function () {
		Plots.config = {
			type: 'line',
			data: {
				// labels: [],
				datasets: [{
                    id: 'temperature',
					label: 'Temperature',
					backgroundColor: Plots.chartColors.red,
					borderColor: Plots.chartColors.red,
                    data: [],
                    pointRadius: 0,
					fill: false,
                    yAxisID: 'y-axis-1',
				}, {
                    id: 'humidity',
					label: 'Humidity',
					backgroundColor: Plots.chartColors.blue,
					borderColor: Plots.chartColors.blue,
                    data: [],
                    pointRadius: 0,
                    fill: false,
                    yAxisID: 'y-axis-1',
				}, {
                    id: 'pressure',
					label: 'Pressure',
					backgroundColor: Plots.chartColors.yellow,
					borderColor: Plots.chartColors.yellow,
                    data: [],
                    pointRadius: 0,
                    fill: false,
                    yAxisID: 'y-axis-2',
				}]
			},
			options: {
				responsive: true,
				title: {
					display: false
				},
				scales: {
					xAxes: [{
                        type: 'linear',
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Time'
                        },
                        ticks: {
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return moment(new Date(value)).format(Plots.timeFormat);
                            },
                            stepSize: 1000
                        }
					}],
					yAxes: [{
                        type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                        display: true,
                        position: 'left',
                        id: 'y-axis-1',
                        scaleLabel: {
							display: true,
							labelString: 'Temperature / Humidity'
						}
                    }, {
                        type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                        display: true,
                        position: 'right',
                        id: 'y-axis-2',
                        scaleLabel: {
							display: true,
							labelString: 'Pressure'
						},
                        // grid line settings
                        gridLines: {
                            drawOnChartArea: false, // only want the grid lines for one axis to show up
                        },
                    }],
				}
			}
        };

		var ctx = document.getElementById('graph').getContext('2d');
        Plots.linePlot = new Chart(ctx, Plots.config);
    },
    addData: function(senses) {
        if (Plots.config.data.datasets.length > 0) {
            Plots.config.data.datasets.forEach(function(dataset) {
                dataset.data.push({
                    x: Number(senses['current_time']),
                    y: senses[dataset['id']]
                });
            });

            if (Plots.config.data.datasets[0].data.length > 30) {
                Plots.config.data.datasets.forEach(function(dataset) {
                    dataset.data.splice(0, 1);
                });
            }

            Plots.linePlot.update();
        }
    }
}
