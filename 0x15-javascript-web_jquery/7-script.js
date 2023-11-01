const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, function (response) {
  console.log(response);
  $('#character').text(response.name);
}
);
