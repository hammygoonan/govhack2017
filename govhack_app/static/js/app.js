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
          var age_icon = this.score_5_year
        }
        if(forecast == 10){
          var age_icon = this.score_10_year
        }
        else{
          var age_icon = this.score_1_year
        }
        var icon = '/static/img/marker_0' + age_icon + 'b.svg';
        var latLng = new google.maps.LatLng(this.longitude, this.latitude);
        var marker = new google.maps.Marker({
          position: latLng,
          map: map,
          data: this,
          icon: icon,
          title: this.postcode.toString(),
        });
        marker.addListener('click', function() {
          if(!$('#details').hasClass('is-active')){
            $('#details').addClass('is-active')
          }
          $('#details').html(template(this.data));
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


  // Nav dropdown
  $('.has-dropdown').on('click', function(){
    $(this).toggleClass('is-active');
  });

});
