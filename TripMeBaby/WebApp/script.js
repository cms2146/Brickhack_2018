  
function getPlaces(){
    var request =
    {
        location: '',
        radius: '500',
        query: document.getElementById("dest").value
    };

      var service = new google.maps.places.PlacesService(map);
      service.textSearch(request, callback);

}
function callback(place, status) {
    console.log(google.maps.places.PlacesServiceStatus.OK)
    if (status == google.maps.places.PlacesServiceStatus.OK) {
    createMarker(place);
  }
}