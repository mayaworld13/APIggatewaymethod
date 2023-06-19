def vita(event , context):
    print(event['headers']['X-Forwarded-For'])
    return {
        "body": "i m vita editing app, I know your ip :" + event['headers']['X-Forwarded-For'],
        "statusCode": 200
        }
