from django.shortcuts import render
from urllib.request import urlopen
places_api_key = 'AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU '
def get_places(location):
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
	for i in location:
		if i ==" ":
			i = "+"
	url +=location
	url+= "&key="
	url+= places_api_key
	html = urlopen(url)
	


