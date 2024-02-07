#!/usr/bin/node
// 2-script.js
/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
