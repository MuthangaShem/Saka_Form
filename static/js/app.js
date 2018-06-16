$(document).ready(function() {

  // Event Location Google maps suggestion
  $("input#id_event_location").geocomplete();

  // Ajax Loader Start Trigger
  $(document).ajaxStart(function() {
    $('#loader').show();
    $('#content').hide();
  })

  // Ajax Loader Stop Trigger
  $(document).ajaxStop(function() {
    $('#loader').hide();
    $('#content').show();
  })

  // Search Functionality
  $('.search-query').keyup(function(event) {
    event.preventDefault();

    let search_form = $('form#custom-search-input');

    let ajax1 = $.ajax({
      url: "event/ajax/search/",
      type: 'POST',
      data: search_form.serialize()
    });

    ajax1.done(function(data) {
      $('div#e-content').empty().html(data)
    });

  });

  // Event Accordion Click Functionality
  $('#ev-accordion').each(function() {
    $(this).click(function(event) {
      event.preventDefault();

  $(".interests").on("click", function(){
    $(this).find(".answer").toggle(300);
    $(this).find($(".fa")).toggleClass('fa_plus fa_minus');

      let event_id = $(this).data('evid');


      let ajax1 = $.ajax({
        url: "event/ajax/accordion/",
        type: 'POST',
        data: {
          event_pk: event_id
        }
      });

      ajax1.done(function(data) {
        $('div#e-content').empty().html(data)
      });

    })
  });

  // Category Accordion Click Functionality
  $('#cat-accordion').each(function() {
    $(this).click(function(event) {
      event.preventDefault();

      let cat_id = $(this).data('catid');

      let ajax1 = $.ajax({
        url: "event/ajax/accordion/",
        type: 'POST',
        data: {
          'category_pk': cat_id
        }
      });

      ajax1.done(function(data) {
        $('div#e-content').empty().html(data)
      });

    })
  });

  // Modal Form Details Update
  $("a#trigger-edit-modal").each(function() {
    $(this).click(function() {
      var event_id = $(this).data('href');

      var modal_ajax = $.ajax({
        url: '/event/manage_event/',
        type: 'GET',
        data: {
          'event_id': event_id
        },
      });

      modal_ajax.done(function(data) {
        console.log(data)
        $("div.update-e").find('input[type=hidden]').after(data);
      });

    });

  });


  $(".interests").on("click", function() {
    $(this).toggleClass("interestsActive");
  });

});

// mapping function
function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    mapTypeControl: false,
    center: {
      lat: -1.28333,
      lng: 36.81667
    },
    zoom: 10
  });

  new AutocompleteDirectionsHandler(map);
}

/**
 * @constructor
 */
function AutocompleteDirectionsHandler(map) {
  this.map = map;
  this.originPlaceId = null;
  this.destinationPlaceId = null;
  this.travelMode = 'WALKING';
  var originInput = document.getElementById('origin-input');
  var destinationInput = document.getElementById('destination-input');
  var modeSelector = document.getElementById('mode-selector');
  this.directionsService = new google.maps.DirectionsService;
  this.directionsDisplay = new google.maps.DirectionsRenderer;
  this.directionsDisplay.setMap(map);

  var originAutocomplete = new google.maps.places.Autocomplete(
    originInput, {
      placeIdOnly: true
    });
  var destinationAutocomplete = new google.maps.places.Autocomplete(
    destinationInput, {
      placeIdOnly: true
    });

  this.setupClickListener('changemode-walking', 'WALKING');
  this.setupClickListener('changemode-transit', 'TRANSIT');
  this.setupClickListener('changemode-driving', 'DRIVING');

  this.setupPlaceChangedListener(originAutocomplete, 'ORIG');
  this.setupPlaceChangedListener(destinationAutocomplete, 'DEST');

  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(originInput);
  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(destinationInput);
  this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(modeSelector);
}

// Sets a listener on a radio button to change the filter type on Places
// Autocomplete.
AutocompleteDirectionsHandler.prototype.setupClickListener = function(id, mode) {
  var radioButton = document.getElementById(id);
  var me = this;
  radioButton.addEventListener('click', function() {
    me.travelMode = mode;
    me.route();
  });
};

AutocompleteDirectionsHandler.prototype.setupPlaceChangedListener = function(autocomplete, mode) {
  var me = this;
  autocomplete.bindTo('bounds', this.map);
  autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    if (!place.place_id) {
      window.alert("Please select an option from the dropdown list.");
      return;
    }
    if (mode === 'ORIG') {
      me.originPlaceId = place.place_id;
    } else {
      me.destinationPlaceId = place.place_id;
    }
    me.route();
  });

};

AutocompleteDirectionsHandler.prototype.route = function() {
  if (!this.originPlaceId || !this.destinationPlaceId) {
    return;
  }
  var me = this;

  this.directionsService.route({
    origin: {
      'placeId': this.originPlaceId
    },
    destination: {
      'placeId': this.destinationPlaceId
    },
    travelMode: this.travelMode
  }, function(response, status) {
    if (status === 'OK') {
      me.directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
};
