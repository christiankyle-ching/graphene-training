# Create a fixture using the graphql_query helper and `client` fixture from `pytest-django`.
import json
import unittest

import pytest
from django.utils import timezone
from graphene_django.utils.testing import graphql_query
from graphene_tutorial.graphql.books.tests.factories import BookFactory


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


# TestCase method using: https://www.hacksoft.io/blog/improve-your-tests-django-fakes-and-factories
class BookCreateTest(unittest.TestCase):
    def setUp(self):
        self.book = BookFactory()

    def test_book_create_sets_author(self, now_mock):
        assert self.book.author.id is not None
