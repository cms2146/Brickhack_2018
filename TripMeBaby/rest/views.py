from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from processing import views
from django.http import HttpResponse
def deserializer(json):
	stream = BytesIO(json)
	data = JSONParser().parse(stream)
	output = views.process_location(data)
	return HttpResponse(output)