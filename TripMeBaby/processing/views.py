from django.shortcuts import render
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import TripMeBaby.rest
import TripMeBaby.api_calls

def process_location(data):
    location = data['location']         #string
    types = data['tags'][0]             #string
    budget = data['budget']             #int
    start_date = data['startDate']      #string
    end_date = data['endDate']          #string
    start_time = data['startTime']      #string
    end_time = data['endTime']          #string
    radius = data['radius']             #int

    budget -= 1
    radius *= 1609.34

    results = TripMeBaby.api_calls.views.get_places(location)
    return results
    #read_results = rest.models.basic_deserializer(results)

