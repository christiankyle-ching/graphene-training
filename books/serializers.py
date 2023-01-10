from rest_framework import serializers
from books.models import Author, Book, BookGenre, GENDER_CHOICES


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Book
            fields = '__all__'