from django.urls import path
from . import views
urlpatterns = [
	path('deserializer',views.deserializer),
]
