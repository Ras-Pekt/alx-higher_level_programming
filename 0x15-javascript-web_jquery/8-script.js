const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (response) {
  $.each(response.results, function (idx, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
}
);
