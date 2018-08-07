import pytest
import unittest
import sys
sys.path.append('..') 
from create_short_url import repository

class TestDynamoDb(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # TODO: Needs proper test setup with a local dynamo
        self.dynamo = repository.DynamoDbRepository('main', 'counter', 'eu-west-1', 'http://localhost:8000')


    def test_dynamoDb_getNextInt_is_int(self):
        assert type(int(self.dynamo.getNextInt())) is int

    def test_dynamoDb_putItem(self):
        id = self.dynamo.getNextInt()
        url = 'www.google.com'
        self.dynamo.putItem({'id': id, 'url': url})
        item = self.dynamo.getItem(id)
        print(item)
        assert item['id'] == id
        assert item['url'] == url