import graphene

from graphene_tutorial.graphql.books.subscriptions import \
    Subscription as BooksSubscription


class Subscription(
    # subclass all subscriptions
    BooksSubscription
):
    pass
