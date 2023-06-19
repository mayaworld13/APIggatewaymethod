def lambda_handler(event, context):
    if event['httpMethod'] == "GET":
        print(event['queryStringParameters']['name'])
        print("i am get method") 
    elif event['httpMethod'] == "POST":
        print("i am post")
        print(event)
    else :
        print("idk this method")
    return {
        'statusCode': 200,
        'body': 'welcome maya world ' 
    }
