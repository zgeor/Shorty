from os import environ
import logging
import common.repository 
logger = logging.getLogger()

def handler(event, context):
    # TODO: Validate the linkId input
    try:
        linkId = event['pathParameters']['linkId']
    except KeyError:
        logger.error("The request did not have a 'linkId'")

    dataRepository = common.repository.DynamoDbRepository(
        environ.get('mainTable'), 
        environ.get('counterTable'), 
        environ.get('region'), 
        environ.get('dynamoUrl'))

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
