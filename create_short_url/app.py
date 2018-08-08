import json

import requests
import logging
import os
from common import repository
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("Requesting short url for: " + event['body'])
    request = json.loads(event['body'])

    dataRepository = repository.DynamoDbRepository(
        os.environ.get('mainTable'), 
        os.environ.get('counterTable'), 
        'eu-west-1', 
        'https://dynamodb.eu-west-1.amazonaws.com')
    
    id = dataRepository.getNextInt()
    dataRepository.putItem({ 'id': id, 'url': request['url']})

    shortUrl = 'https://' + event['headers']['Host'] + event['requestContext']['path'] + str(id)
    return {
            "statusCode": 201,
            "body": json.dumps({
                "shortened_url": shortUrl
            })
        }