import json
import unittest
import unittest.mock as mock
import sys
sys.path.append('..')
import common.repository
from create_short_url import app



@mock.patch.dict(
    'get_short_url.app.environ',
    {'region': 'eu-west-1',
     'mainTable': 'testMain',
     'counterTable': 'testCounter',
     'dynamoUrl': 'https://dummy'})
class CreateShortUrlUnitTests(unittest.TestCase):

    valid_url_with_id_1 = "https://1234567890.execute-api.us-east-1.amazonaws.com/Prod/AQAA"
    def create_url_event(self):
        """ Generates API GW Event"""

        return {
            "body": "{\"url\": \"http://www.test.com\"}",
            "resource": "/{proxy+}",
            "requestContext": {
                "resourceId": "123456",
                "resourcePath": "/{proxy+}",
                "httpMethod": "POST",
                "path": "/Prod/",
                "stage": "prod"
            },
            "headers": {
                "X-Forwarded-Port":
                "443",
                "Host":
                "1234567890.execute-api.us-east-1.amazonaws.com",
            },
            "pathParameters": {
                "linkId": "0"
            },
            "httpMethod": "GET",
            "path": "/0"
        }


    @mock.patch('common.repository.DynamoDbRepository', autospec=True)
    def test_returns_201_code_on_success(self, mock_dynamo_db):
        mock_dynamo_db.return_value.getNextInt.return_value = 1

        ret = app.handler(self.create_url_event(), "")
        assert ret['statusCode'] == 201

    @mock.patch('common.repository.DynamoDbRepository', autospec=True)
    def test_returns_correct_status_body(self, mock_dynamo_db):
        mock_dynamo_db.return_value.getNextInt.return_value = 1

        ret = app.handler(self.create_url_event(), "")
        response = json.loads(ret['body'])
        self.assertEqual(response.get("shortened_url"), self.valid_url_with_id_1)


if __name__ == '__main__':
    unittest.main()