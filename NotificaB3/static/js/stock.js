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

        if (response) {

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

            console.log(response)
            news = response.news

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
        //after all, hide the loader
        document.getElementById("loader-news").style.display = 'none'

    });

}