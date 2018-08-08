import os
import logging
from common import repository 
logger = logging.getLogger()

def handler(event, context):
    # TODO: Validate the linkId input
    try:
        linkId = event['pathParameters']['linkId']
    except KeyError:
        logger.error("The request did not have a 'linkId'")

    dataRepository = repository.DynamoDbRepository(
        os.environ.get('mainTable'), 
        os.environ.get('counterTable'), 
        os.environ.get('region'), 
        'https://dynamodb.'+ os.environ.get('region') +'.amazonaws.com')

    urlItem = dataRepository.getItem(int(linkId))

    if(urlItem is None):
        return { "statusCode": 404 }
    else:
        return {
            "statusCode": 302,
            "headers": {
                "Location": urlItem['url']
            }
        }
