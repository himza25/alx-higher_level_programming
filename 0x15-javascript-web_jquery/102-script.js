#!/usr/bin/node
// 102-script.js
/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
