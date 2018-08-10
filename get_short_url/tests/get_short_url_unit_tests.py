import json
import unittest
import unittest.mock as mock
import sys
sys.path.append('..')
import common.repository
from get_short_url import app

@mock.patch.dict(
            'get_short_url.app.environ', 
            { 'region': 'eu-west-1',
              'mainTable': 'testMain', 
              'counterTable': 'testCounter',
              'dynamoUrl': 'https://dummy' })
class GetShortUrlUnitTests(unittest.TestCase):
    valid_url = 'https://grt.local/something-long'

    @mock.patch('common.repository.DynamoDbRepository', autospec=True)
    def test_returns_302_code_when_valid_url(self, mock_dynamo_db):
        ret = app.handler(self.apigw_event(), "")
        self.assertEqual(ret['statusCode'], 302)
    
    @mock.patch('common.repository.DynamoDbRepository', autospec=True)
    def test_returns_correct_header_value_when_valid_url(self, mock_dynamo_db):
        mock_dynamo_db.return_value.getItem.return_value = {'url': self.valid_url } 

        ret = app.handler(self.apigw_event(), "")
        self.assertEqual(ret['headers']['Location'], self.valid_url)

    @mock.patch('common.repository.DynamoDbRepository', autospec=True)
    def test_returns_404_code_when_not_found(self, mock_dynamo_db):
        mock_dynamo_db.return_value.getItem.return_value = None
        ret = app.handler(self.apigw_event(), "")
        self.assertEqual(ret['statusCode'], 404)
   
    def apigw_event(self):
        """ Generates API GW Event"""

        return {
            "body": "",
            "resource": "/{proxy+}",
            "requestContext": {
                "resourceId": "123456",
                "apiId": "1234567890",
                "resourcePath": "/{proxy+}",
                "httpMethod": "POST",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "stage": "prod"
            },
            "queryStringParameters": {},
            "headers": {
                "Via":
                "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
                "X-Forwarded-Port":
                "443",
                "Host":
                "1234567890.execute-api.us-east-1.amazonaws.com",
                "X-Forwarded-Proto":
                "https"
            },
            "pathParameters": {
                "linkId": "0"
            },
            "httpMethod": "GET",
            "path": "/0"
        }

if __name__ == '__main__':
    unittest.main()