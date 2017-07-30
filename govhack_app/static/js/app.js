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
    forcast = $(this).val();
  });

  var age = 1;
  $('input:radio[name="age"]').on('change', function(){
    age = $(this).val();
  });

  // Map markers
  var source   = $("#entry-template").html();
  var template = Handlebars.compile(source);

  $.getJSON('/api/', function(data){
    $(data.postcodes).each(function(){
      var icon = '/static/img/marker_0' + this.score_1_year + 'b.svg';
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
    });
  });


  // Nav dropdown
  $('.has-dropdown').on('click', function(){
    $(this).toggleClass('is-active');
  });

});
