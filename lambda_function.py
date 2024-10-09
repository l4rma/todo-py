import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.eu-west-1.amazonaws.com")

    table = dynamodb.Table('Tasks')
    Item={
            'Id': '123',
            'Title': event['title'],
            'Description': event['description'],
            'Complete': event['complete'],
    }
    print(Item)
    table.put_item(Item = Item)
    return Item
