#!/usr/bin/node
// 6-script.js
/* global $ */
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
