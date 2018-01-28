from django.shortcuts import render
from urllib.request import urlopen
import rest.models

places_api_key = 'AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU'


# location is whatever text-formatted input that the user gives
def get_places(location):
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key=AIzaSyBMkM6kLxccjjZhtwVuGiA6roJTZz9AmoU"
	location.replace(" ", "+")
	json = urlopen(url)
	data = rest.models.basic_deserializer(json)
	print(data['results'][1]['formatted_address'])

    # this data should contain-> opening_hours (also open_now), place_id,
    # price_level (from 0-4), rating (from 1.0-5.0)
	return data



# location is the place_id of the location
def get_details(location):
    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid" \
          "=" + location + "&key=" + places_api_key
