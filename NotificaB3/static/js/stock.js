function showConfigAlert() {

    var x = document.getElementById("configAlert");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function getAllQuoteInformation(code) {

    //get all quote information
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "/api/stock/quotes/get/?code=" + code,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {

        var quote = []

        if (response.quoteResponse.result.length > 0 && response.quoteResponse.result[0].quoteType != 'NONE') {

            let res = response.quoteResponse.result[0]

            quote.push({ name: "regularMarketPreviousClose", value: res.regularMarketPreviousClose })
            quote.push({ name: "regularMarketPrice", value: res.regularMarketPrice })
            quote.push({ name: "bid", value: res.bid })
            quote.push({ name: "ask", value: res.ask })
            quote.push({ name: "regularMarketDayRange", value: res.regularMarketDayRange })
            quote.push({ name: "regularMarketVolume", value: res.regularMarketVolume })
            quote.push({ name: "trailingPE", value: res.trailingPE })
            quote.push({ name: "epsTrailingTwelveMonths", value: res.epsTrailingTwelveMonths })
            quote.push({ name: "dividendRate", value: res.dividendRate })
            quote.push({ name: "dividendYield", value: res.dividendYield })
            quote.push({ name: "longname", value: res.longName })

            for (let i = 0; i < quote.length; i++) {
                document.getElementById(quote[i].name).innerHTML = quote[i].value;
            }

            //change the price of quote
            document.getElementById("actualPrice").innerHTML = quote[1].value
            let date = new Date()
            document.getElementById("actualDate").innerHTML = date.toLocaleString('pt-BR')

            //update forms values
            document.getElementsByName("name_company").value = quote[9].value

        } else {

            //after all, hide the loader
            document.getElementById("stock-info").style.display = 'none'
            document.getElementById("stock-chart").style.display = 'none'
            document.getElementById("stock-news").style.display = 'none'

            document.getElementById("msg-error-stock").style.display = 'block'

        }


        //after all, hide the loader
        document.getElementById("loader-stock").style.display = 'none'

    });

}

//function get stock news
function getStockNews(code) {

    //get all quote information
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "/api/stock/news/get/?code=" + code,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {

        var news = []

        if (response) {

            news = response.news

            if (news.length == 0) {

                document.getElementById("stock-news").style.display = 'none'

            } else {

                for (let i = 0; i < news.length; i++) {

                    //date news from api is in timestamp, for this we have to multiply by 1000
                    let dateFormated = new Date(news[i].providerPublishTime * 1000)

                    var listString = '<div class="item">';
                    listString += '<div class="content">';
                    listString += '<a href="' + news[i].link + '" target="_blank" class="header">' + news[i].title + ' </a><div class="description">' + dateFormated.toLocaleDateString() + '</div>';
                    listString += "</div></div>";

                    $('#list-news').append(listString);

                }
            }
        }
        //after all, hide the loader
        document.getElementById("loader-news").style.display = 'none'

    });

}

function getChart(code) {


    //get chart data from api
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "/api/stock/chart/get/?code=" + code,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {

        chart_res = response.chart.result

        if (chart_res.length > 0) {

            timestamp = chart_res[0].timestamp
            close_quote = chart_res[0].indicators.quote[0].close
            /*
            high_quote = chart_res[0].timestamp
            low_quote = chart_res[0].timestamp
            open_quote = chart_res[0].timestamp
            volume_quote = chart_res[0].timestamp
            */
            var options = {
                chart: {
                    type: "area",
                    height: 300,
                    foreColor: "#999",
                    stacked: true,
                    /*
                    dropShadow: {
                        enabled: true,
                        enabledSeries: [0],
                        top: -2,
                        left: 2,
                        blur: 5,
                        opacity: 0.06
                    }*/
                },
                colors: ['#00E396'],
                stroke: {
                    curve: "smooth",
                    width: 3
                },
                dataLabels: {
                    enabled: false
                },
                series: [{
                    name: 'Valor (BRL)',
                    data: generateDayWiseTimeSeries(close_quote, timestamp)
                }],
                markers: {
                    size: 0,
                    strokeColor: "#fff",
                    strokeWidth: 3,
                    strokeOpacity: 1,
                    fillOpacity: 1,
                    hover: {
                        size: 6
                    }
                },
                xaxis: {
                    type: "datetime",
                    axisBorder: {
                        show: false
                    },
                    axisTicks: {
                        show: false
                    }
                },
                yaxis: {
                    labels: {
                        offsetX: 14,
                        offsetY: -5
                    },
                    tooltip: {
                        enabled: true
                    },
                    title: {
                        text: 'Valor (BRL)'
                    },
                },
                grid: {
                    padding: {
                        left: -5,
                        right: 5
                    }
                },
                tooltip: {
                    x: {
                        format: "dd MMM yyyy"
                    },
                },
                legend: {
                    position: 'top',
                    horizontalAlign: 'left'
                },
                fill: {
                    fillOpacity: 0.2
                },

                defaultLocale: "br"
            };

            var chart = new ApexCharts(document.querySelector("#chart"), options);
            chart.render();


        } else {

            //after all, hide the loader
            document.getElementById("stock-chart").style.display = 'none'

        }


        //after all, hide the loader
        document.getElementById("loader-chart").style.display = 'none'

    });


}

function generateDayWiseTimeSeries(values, timestamp) {

    var series = [];
    for (i = 0; i < values.length; i++) {

        series.push([new Date(timestamp[i] * 1000), values[i].toFixed(2)]);
    }
    return series;
}