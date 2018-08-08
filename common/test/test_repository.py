import unittest
import sys
sys.path.append('..') 
from create_short_url import repository

class TestDynamoDb(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # TODO: Needs proper test setup with a local dynamo
        self.dynamo = repository.DynamoDbRepository('main', 'counter', 'eu-west-1', 'http://localhost:8000')


    def test_getNextInt_is_int(self):
        assert type(int(self.dynamo.getNextInt())) is int

    def test_putItem(self):
        id = self.dynamo.getNextInt()
        url = 'www.google.com'

        self.dynamo.putItem({'id': id, 'url': url})
        item = self.dynamo.getItem(id)
        
        assert item['id'] is id
        assert item['url'] is url
    
    def test_get_non_existing_is_none(self):
        assert self.dynamo.getItem(-1) is None