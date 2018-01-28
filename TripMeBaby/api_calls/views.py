from django.shortcuts import render
from urllib.request import urlopen
import rest.models
places_api_key = 'AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU'
def get_places(location):
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key=AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU"
	location.replace(" ", "+")
	json = urlopen(url)
	data = rest.models.basic_deserializer(json)
	print(data['results'][1]['formatted_address'])
	return data




