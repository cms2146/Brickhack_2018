from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
def deserializer(json):
	stream = BytesIO(json)
	data = JSONParser().parse(stream)
	serializer = CommentSerializer(data=data)
	serializer.is_valid()
	serializer.validated_data
	print(data)
