function getAllStocks() {

    //get all the B3 stocks from API
    const settings = {
        "async": true,
        "crossDomain": true,
        "url": "/api/stock/b3/all/get/",
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {

        var stocks = []

        if (response) {
            let size = response.length

            for (i = 0; i < response.length; i++) {

                if (response[i].cd_acao.includes(',')) {
                    //split in two valuews
                    stocks.push({ category: response[i].setor_economico, title: response[i].cd_acao.split(',')[0].trim() })
                    stocks.push({ category: response[i].setor_economico, title: response[i].cd_acao.split(',')[1].trim() })
                } else {
                    stocks.push({ category: response[i].setor_economico, title: response[i].cd_acao })
                }

            }
        }


        for (i = 0; i < stocks.length; i++) {

            if (stocks[i].title != '') {
                var tableString = "<tr>";
                tableString += "<td> <h3 class='ui center aligned header'>" + stocks[i].title + "</h3></td>";
                tableString += "<td>" + stocks[i].category + "</td>";
                tableString += "<td><center><div class='ui icon buttons'><a href='../stock/?q=" + stocks[i].title + "'><button class='ui button'><i class='eye icon'></i></button></a> </div></center></td>";
                tableString += "</tr>";

                $('table tbody').append(tableString);
            }

        }


        var content = stocks;
        $('.ui.search')
            .search({
                type: 'category',
                source: content,
                onSelect: function onSelect(result, response) {
                    window.location.href = "/stock/?q=" + result.title;

                }
            })
            ;

        //hide the loader            
        document.getElementById("loader-market").style.display = 'none'

        $('#market-table').DataTable();
    });

}