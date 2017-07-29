var map;

function initMap() {
  var centre = {
    lat: -37.811815,
    lng: 144.964858
  };
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 9,
    center: centre
  });
}


$(document).ready(function() {

  var source   = $("#entry-template").html();
  var template = Handlebars.compile(source);

  $.getJSON('/api/', function(data){
    $(data.postcodes).each(function(){
      var latLng = new google.maps.LatLng(this.longitude, this.latitude);
      var marker = new google.maps.Marker({
        position: latLng,
        map: map,
        data: this
      });
      marker.addListener('click', function() {
        $('#details').html(template(this.data));
      });
    });
  });

});
