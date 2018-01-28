from django.urls import path

import TripMeBaby.rest.views

urlpatterns = [
    path('deserializer', TripMeBaby.rest.views.deserializer),
]