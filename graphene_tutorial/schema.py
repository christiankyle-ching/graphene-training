import graphene
from graphene_django import DjangoObjectType
from books.models import Author, Book, BookGenre


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class BookGenreType(DjangoObjectType):
    class Meta:
        model = BookGenre
        fields = '__all__'


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    genre_by_name = graphene.Field(
        BookGenreType, name=graphene.String(required=True))

    # Resolvers
    def resolve_authors(root, info):
        print(root)
        print(info)

        return Author.objects.prefetch_related('books').all()

    def resolve_genre_by_name(root, info, name):
        print(root)
        print(info)

        try:
            return BookGenre.objects.get(name=name)
        except BookGenre.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
