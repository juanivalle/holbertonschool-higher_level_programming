#!/usr/bin/node

$(document).ready(function () {
  const toggleHeader = $('#toggle_header');

  const header = $('header');

  toggleHeader.on('click', function () {
    header.toggleClass('red green');
  });
});
