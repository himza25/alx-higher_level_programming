#!/usr/bin/node
// 103-script.js
/* global $ */
$(document).ready(function () {
  function translate () {
    const languageCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      $('#hello').html(data.hello);
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) { // Check if the key pressed is the ENTER key
      translate();
    }
  });
});
