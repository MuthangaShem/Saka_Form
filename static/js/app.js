$(document).ready(function() {

  $('.search-query').keyup(function(event) {
    event.preventDefault()

    var search_item = $('.search-query').val();
    let search_form = $('form#custom-search-input')

    $.ajax({
      url: "{% url 'home' %}",
      type: 'POST',
      data: search_form.serialize(),
      dataType: 'json'
    }).done(function(data) {
      console.log("ssss")
    });

  });

})