import boto3
import logging
import json
logger = logging.getLogger("test")

class DynamoDbRepository:

    def createTablesIfNotExists(self, mainTableName, counterTableName):
        try:
            response = self.dynamoDb.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': 'counterName',
                        'AttributeType': 'S',
                    },
                ],
                KeySchema=[
                    {
                        'AttributeName': 'counterName',
                        'KeyType': 'HASH',
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1,
                },
                TableName=counterTableName,
            )
        except Exception:
            pass
        try:
            response = self.dynamoDb.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'N',
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH',
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1,
                },
                TableName=mainTableName,
            )
        except Exception:
            pass

    def __init__(self, mainTableName, counterTableName, regionName, endpointUrl):
        self.dynamoDb = boto3.resource('dynamodb',  region_name=regionName, endpoint_url=endpointUrl)
        self.createTablesIfNotExists(mainTableName, counterTableName)

        self.mainTable = self.dynamoDb.Table(mainTableName)
        self.counterTable = self.dynamoDb.Table(counterTableName)
    
    def getNextInt(self):
        response = self.counterTable.update_item(
            Key= { 'counterName': 'counter1' },
            UpdateExpression='ADD counterValue :inc',
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues="UPDATED_NEW"
        )

        return response['Attributes']['counterValue']

    def putItem(self, item):
        return self.mainTable.put_item(
            Item=item,
            ReturnValues="NONE"
        )
    def getItem(self, key):
        item = self.mainTable.get_item(
            Key={ 'id': key }
        )
        return item['Item']