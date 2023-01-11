# Create a fixture using the graphql_query helper and `client` fixture from `pytest-django`.
import json
import pytest
from graphene_django.utils.testing import graphql_query


# Helper fixture to setup gql client.
# From: https://docs.graphene-python.org/projects/django/en/latest/testing/#using-pytest
@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


# Required to mark this with django_db to prevent errors in Database access
@pytest.mark.django_db
def test_all_authors(client_query):
    response = client_query(
        '''
        query Authors {
            authors {
                id
                name
            }
        }
        ''',
    )

    content = json.loads(response.content)
    assert 'errors' not in content
