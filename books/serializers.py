from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	
