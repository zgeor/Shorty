import json

import requests
import logging

logger = logging.getLogger()

def handler(event, context):
    logger.info("Requesting short url Id: " + event['pathParameters']['linkId'])
    
    return {
        "statusCode": 302,      
         "headers": {
            "Location": event['pathParameters']['linkId']
        }
    }
