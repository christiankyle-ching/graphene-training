import graphene
from django.utils.translation import gettext_lazy as _
from graphene_django import DjangoObjectType

from books.models import GenderEnum, Author, Book, BookGenre

""" Enums """

GenderEnumType = graphene.Enum.from_enum(GenderEnum)

""" Types """


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', 'gender', 'books')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre')


class BookGenreType(DjangoObjectType):
    class Meta:
        model = BookGenre
        fields = ('id', 'name')
