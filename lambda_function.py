import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.eu-west-1.amazonaws.com")

    table = dynamodb.Table('tasks')
    Item={
            'id': '123',
            'title': event['title'],
            'description': event['description'],
            'complete': event['complete'],
    }
    print(Item)
    table.put_item(Item = Item)
    return Item
