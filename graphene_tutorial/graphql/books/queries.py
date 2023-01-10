import graphene
from django.utils.translation import gettext_lazy as _
from graphene_django import DjangoListField, DjangoObjectType
from graphene_tutorial.graphql.books.types import AuthorType, BookGenreType

from books.models import Author, BookGenre

"""
Queries
"""


class Query(graphene.ObjectType):
    # use DjangoListField to automatically use resolver
    authors = DjangoListField(AuthorType, description=_("Get all the authors"))
    genre_by_name = graphene.Field(
        BookGenreType, name=graphene.String(required=True), description=_("Get all genre by name"))
    authors_by_genre = graphene.List(
        graphene.NonNull(AuthorType), id=graphene.String(required=True), description=_("Get all authors by genre")
    )

    # Resolvers
    def resolve_genre_by_name(root, _, name):
        try:
            return BookGenre.objects.get(name=name)
        except BookGenre.DoesNotExist:
            return None

    def resolve_authors_by_genre(root, _, id):
        # prefetch_related is to optimize query to include books in a single db hit
        return Author.objects.prefetch_related('books').filter(books__genre__pk=id)
