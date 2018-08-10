import json

import logging
from os import environ
from common import repository, converter

def handler(event, context):
    request = json.loads(event['body'])

    dataRepository = repository.DynamoDbRepository(
        environ.get('mainTable'),
        environ.get('counterTable'),
        environ.get('region'),
        environ.get('dynamoUrl'))

    idBase=dataRepository.getNextInt()
    id = converter.idFromInt(idBase)
    dataRepository.putItem({'id': id, 'url': request['url']})

    shortUrl='https://' + event['headers']['Host'] + event['requestContext']['path'] + id
    return {
            "statusCode": 201,
            "body": json.dumps({
                "shortened_url": shortUrl
            })
        }
