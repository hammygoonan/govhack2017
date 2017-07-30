// define map
var map;


// initialise map
function initMap() {
  var centre = {
    lat: -37.811815,
    lng: 144.964858
  };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: centre,
    styles: [ { stylers : [
			{ "saturation": -100 },
			{ "lightness": 70 },
			{ "gamma": 0.5 }
		] } ]
  });
}


$(document).ready(function() {

  // Map filters

  var forecast = 1;
  $('input:radio[name="forecast"]').on('change', function(){
    forecast = $(this).val();
  });

  var age = 1;
  $('input:radio[name="age"]').on('change', function(){
    age = $(this).val();
  });

  $('#filter-form').on('submit', function(e){
    e.preventDefault();
    deleteMarkers();
    addMarkers(age);
  })

  // Map markers
  var source   = $("#entry-template").html();
  var template = Handlebars.compile(source);

  var markers = []

  function addMarkers(age){
    $.getJSON('/api/age/' + age, function(data){
      $(data.postcodes).each(function(){
        if(forecast == 5){
          var icon = this.score_5_year
        }
        if(forecast == 10){
          var icon = this.score_10_year
        }
        else{
          var icon = this.score_1_year
        }
        this.score = icon;
        this.age = age;
        var icon_img = '/static/img/marker_0' + icon + 'b.svg';
        var latLng = new google.maps.LatLng(this.longitude, this.latitude);
        var marker = new google.maps.Marker({
          position: latLng,
          map: map,
          data: this,
          icon: icon_img,
          title: this.postcode.toString(),
        });
        marker.addListener('click', function() {
          if(!$('#pcode-details').hasClass('is-active')){
            $('#pcode-details').addClass('is-active')
          }
          $('#pcode-details').html(template(this.data));
        });
        markers.push(marker);
      });
    });
  }

  function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(map);
    }
  }

      // Removes the markers from the map, but keeps them in the array.
  function clearMarkers() {
    setMapOnAll(null);
  }

      // Shows any markers currently in the array.
  function showMarkers() {
    setMapOnAll(map);
  }

  // Deletes all markers in the array by removing references to them.
  function deleteMarkers() {
    clearMarkers();
    markers = [];
  }

  // intialise markers
  addMarkers(age);


  // Postcode filter
  $('#pcode-form').on('submit', function(e){
    e.preventDefault();
    var pcode = $('#pcode-field').val()
    $.getJSON('/api/postcode/' + pcode + '/age/' + age, function(data){
      $('#pcode-details').html(template(data));
      if(!$('#pcode-details').hasClass('is-active')){
        $('#pcode-details').addClass('is-active')
      }
    });
  });

  // Nav dropdown
  $('.has-dropdown').on('click', function(){
    $(this).toggleClass('is-active');
  });

});
