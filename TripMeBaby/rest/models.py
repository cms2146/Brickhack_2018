from django.db import models
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
# Create your models here.

from rest_framework import serializers

class output(object):
    def __init__(self, location, website, phone, distance, price, travel_time):
        self.location = location
        self.website = website
        self.phone = phone
        self.distance = distance
        self.price = price
        self.travel_time = travel_time

class output_serializer(serializers.Serializer):
    location = serializers.CharField()
    website = serializers.URLField(max_length=None, min_length=None,
                                   allow_blank=True)
    phone = serializers.CharField()
    distance = serializers.IntegerField(max_value=None, min_value=None)
    price = serializers.IntegerField(max_value = 5, min_value = 0)
    travel_time = serializers.CharField()

def basic_deserializer(json):
    data = JSONParser().parse(json)
    return data;
