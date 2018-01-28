from django.shortcuts import render
from urllib.request import urlopen
import rest.models
places_api_key = 'AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU'
def get_places(location):
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
	location =location.replace(" ", "+")
	url +=location
	url+='&key='
	url+= places_api_key
	print(url)
	json = urlopen(url)
	data = rest.models.basic_deserializer(json)
	return data




