#!/usr/bin/node
// 3-script.js
/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
