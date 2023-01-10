from graphene_tutorial.graphql.books.mutations import Mutation as BooksMutation


class Mutation(
    # subclass mutations per app
    BooksMutation
):
    pass
