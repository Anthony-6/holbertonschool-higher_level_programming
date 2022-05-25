$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    $.each( data.results, function (key, value) {
        $("#list_movies").append("<li>" + value.title  + "</li>")
    })
});