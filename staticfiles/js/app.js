$(document).ready(function() {
  // Event Location Google maps suggestion
  $("input#id_location").geocomplete();
  $("input#id_event_location").geocomplete();

  // Ajax Loader Start Trigger
  $(document).ajaxStart(function() {
    $('#loader').show();
    $('div#e-content').hide();
  })

  // Ajax Loader Stop Trigger
  $(document).ajaxStop(function() {
    // $('#loader').hide();
    // $('div#e-content').show();
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
  $('.ev-accordion').each(function() {
    $(this).click(function(event) {
      event.preventDefault();

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
  $('.cat-accordion').each(function() {
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

  // Subscribe Functionality
  $('#navbarSubscribe').click(function(event) {
      event.preventDefault();

      let user_id = $(this).data('user-id');
      let subscribe_url = $(this).data('sub-url');

      let ajax1 = $.ajax({
        url: subscribe_url,
        type: 'POST',
        data: {
          user_pk: user_id
        }
      });

      ajax1.done(function(data) {

        if (data == "subscribed"){
          $('#navbarSubscribe').empty().html('Unsubscribe');
        }

        if (data == "unsubscribed"){
          $('#navbarSubscribe').empty().html('Subscribe')
        }

      });

  });

  // Modal Form Details Update
  // $("body").each("#id_number_of_tickets",function(){
  $("a#trigger-edit-modal").each(function() {
    $(this).click(function() {
      let event_id = $(this).data('href');

      let modal_ajax = $.ajax({
        url: '/event/manage_event/',
        type: 'GET',
        data: {
          'event_id': event_id
        },
      });

      modal_ajax.done(function(data) {
        console.log(data)
        $("div.update-e").after(data);
      });

    });

  });
  // Modal Payment Form Details Update
  // $("a#trigger-payment-modal").each(function() {
  //   $(this).click(function() {
  //     let event_id = $(this).data('href');
  //
  //     let modal_ajax = $.ajax({
  //       url: '/event/manage_event/',
  //       type: 'GET',
  //       data: {
  //         'event_id': event_id
  //       },
  //     });
  //
  //     modal_ajax.done(function(data) {
  //       $("div.update-e").find('input[type=hidden]').after(data);
  //     });
  //
  //   });
  //
  // });


  //Ensure forms are removed in modal
  $("#editeventmodal").on("hidden.bs.modal", function () {
    location.reload()
});
  $("#paymentmodal").on("hidden.bs.modal", function () {
    location.reload()
});

  // Modal Payment Form Details Update
  $("a#trigger-payment-modal").each(function() {
    $(this).click(function() {
      let event_id = $(this).data('href');

      let modal_ajax = $.ajax({
        url: '/event/manage_event/',
        type: 'GET',
        data: {
          'e_id': event_id
        },
      });

      modal_ajax.done(function(data) {
        $("div#update-e").after(data);
      });

    });

  });


  // interests click handler
  var checkedCounter = 0;
  $("div[class='zoomimage']").each(function() {
    let $this = $(this)

    $this.click(function() {
      $this.find('.answer').toggle(300);
      $this.find('.fa').toggleClass('fa_plus fa_minus');

      if ($this.find('input:checkbox[class=check]').is(":checked")) {
        $this.find('input:checkbox[class=check]').attr("checked", false);
        checkedCounter-=1;
      } else {
        $this.find('input:checkbox[class=check]').attr("checked", true);
        checkedCounter+=1;
      }

      // Check Min Selected Categories
      if (checkedCounter>=3){
        $("button#done").attr("disabled",false);
      }else{
        $("button#done").attr("disabled",true);
      }

    })

  });

  // Get All Checked Categories Handler
$("button#done").click(function(){
  var checkedCat = [];
  $('input:checkbox:checked').each(function () {
       let $ThisVal = (this.checked ? $(this).data('id') : "");
       checkedCat.push($ThisVal);
  });

  let ajax4 = $.ajax({
    url: "ajax/handle/",
    type: 'POST',
    data: {
      'category_arr': JSON.stringify(checkedCat)
    }
  });

  ajax4.done(function(data) {
    window.location.href = "/";
  });

});

// Update Charges on Modal
$("body").on('keyup', "#id_number_of_tickets",function(){

  let $eventId =$("#booking-form").data('id');
  let $url = $("#booking-form").data('cost-url');
  let $input = $("#id_number_of_tickets").val();


  if($input>=1){
  let ajax4 = $.ajax({
    url: $url,
    type: 'POST',
    data: {
      'the_event':$eventId,
      't_num':$input
    }
  });

  ajax4.done(function(data) {
    $('#cost').empty().html(data);
  });
}else{
    $('#cost').empty();
}

});

// Fade out alert messages after four seconds
window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
          $(this).remove();
        });
      }, 5000);

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
