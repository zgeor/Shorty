import json

import requests
import logging
from common import repository 
logger = logging.getLogger()

def handler(event, context):
    # TODO: Validate the linkId input
    try:
        linkId = event['pathParameters']['linkId']
    except KeyError:
        logger.error("The request did not have a 'linkId'")

    dataRepository = repository.DynamoDbRepository('main', 'counter', 'eu-west-1', 'http://localhost:8000')
    urlItem = dataRepository.getItem(linkId)

    if(urlItem is None):

        logger.warn("Item was not found")
        return { "statusCode": 404 }
    else:

        logger.warn("Item was" + urlItem)

        return {
            "statusCode": 302,      
            "headers": {
                "Location": urlItem
            }
        }
