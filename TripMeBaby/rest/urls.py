from django.urls import path

from TripMeBaby.rest import views

urlpatterns = [
    path('deserializer', views.deserializer),
]