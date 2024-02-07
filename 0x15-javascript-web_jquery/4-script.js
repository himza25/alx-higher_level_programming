#!/usr/bin/node
// 4-script.js
/* global $ */
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
