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

        # prevents graphene from creating another Enum type for `gender`, that results to incompatibility
        # Workflow:
        # 1. model.TextChoices
        # 2. graphene.Enum.from_enum()
        # 3. convert_choices_to_enum = False
        convert_choices_to_enum = False


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'published_at')


class BookGenreType(DjangoObjectType):
    class Meta:
        model = BookGenre
        fields = ('id', 'name')
