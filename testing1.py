def lambda_handler(event, context):
    print(event['queryStringParameters']['name'])
    
    return {
        'statusCode': 200,
        'body': 'welcome ' + event['queryStringParameters']['name']
    }
