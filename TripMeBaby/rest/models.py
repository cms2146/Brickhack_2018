from django.db import models

# Create your models here.

from rest_framework import serializers

class output_serializer(serializers.Serializer):
    location = serializers.CharField()
    website = serializers.URLField(max_length=None, min_length=None,
                                   allow_blank=True)
    phone = serializers.CharField()
    distance = serializers.IntegerField(max_value=None, min_value=None)
    price = serializers.IntegerField(max_value = 5, min_value = 0)
    travel_time = serializers.CharField()