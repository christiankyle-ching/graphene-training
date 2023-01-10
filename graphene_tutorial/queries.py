from graphene_tutorial.graphql.books.queries import Query as BooksQuery


class Query(
    # subclass queries per app
    BooksQuery
):
    pass
