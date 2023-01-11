import graphene
from django.utils.translation import gettext_lazy as _
from graphene_tutorial.graphql.books.types import (AuthorType, BookType,
                                                   GenderEnumType)

from books.models import Author, Book


""" Author Mutations """


class AddAuthorInput(graphene.InputObjectType):
    # input object type for complex data
    name = graphene.String(required=True)
    gender = GenderEnumType(required=True)


class AddAuthor(graphene.Mutation):
    # arguments for mutation. uses input object type for complex input data
    class Arguments:
        input = AddAuthorInput(required=True)

    # output fields after mutation
    author = graphene.Field(AuthorType)

    # action to do after calling mutation
    @classmethod
    def mutate(cls, root, info, input):
        author = Author(
            name=input.name,
            gender=input.gender
        )
        author.save()
        return AddAuthor(author=author)


""" Book Mutations """


class AddBookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    genre = graphene.String(required=True)


class AddBook(graphene.Mutation):
    # arguments for mutation. uses input object type for complex input data
    class Arguments:
        input = AddBookInput(required=True)

    # output fields after mutation
    book = graphene.Field(BookType)

    # action to do after calling mutation
    @classmethod
    def mutate(cls, root, info, input):
        book = Book(
            title=input.title,
            genre=input.genre
        )
        book.save()
        return AddBook(book=book)


class Mutation(graphene.ObjectType):
    add_author = AddAuthor.Field()
    add_book = AddBook.Field()
