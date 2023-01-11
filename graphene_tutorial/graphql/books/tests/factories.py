import factory
from graphene_tutorial.utils.tests import faker
from books.models import Author, Book, BookGenre, GenderEnum


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda _: faker.name())
    gender = factory.LazyAttribute(
        lambda _: "MALE")


class BookGenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookGenre

    name = factory.LazyAttribute(lambda _: faker.name())


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.LazyAttribute(lambda _: faker.name())
    author = factory.SubFactory(AuthorFactory)
    name = factory.SubFactory(BookGenreFactory)
