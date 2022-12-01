from rest_framework import serializers

from shop.models import Book

class BooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price']