from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.http import HttpResponse
import api_calls.views
import processing


@csrf_exempt
def deserializer(json):
    stream = BytesIO(json.body)
    data = JSONParser().parse(stream)
    output = processing.views.process_location(data)
    #var = data['location']
    #api_calls.views.get_places("New york")
    return HttpResponse(output)
