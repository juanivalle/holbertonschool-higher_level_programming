#!/usr/bin/node

$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (i, movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
