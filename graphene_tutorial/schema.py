import graphene
from graphene_tutorial.queries import Query
from graphene_tutorial.mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
