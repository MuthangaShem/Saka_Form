$(document).ready(function() {

  // $("#").geocomplete(); //location autocomplete

  $(document).ajaxStart(function() {
    $('#loader').show();
    $('#content').hide();
  })

  $(document).ajaxStop(function() {
    $('#loader').hide();
    $('#content').show();
  })

  $('.search-query').keyup(function(event) {
    event.preventDefault();

    let search_form = $('form#custom-search-input');

    let ajax1 = $.ajax({
      url: "event/ajax/search/event/",
      type: 'POST',
      data: search_form.serialize(),
      dataType: 'json'
    });

    ajax1.done(function(data) {
      $(data).insertBefore("#content");
    });

  });



})