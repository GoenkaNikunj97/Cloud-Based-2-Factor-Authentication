import json
import boto3
import configparser

def dynamodb_handler(event, context):

    configuration = configparser.ConfigParser()
    configuration.read('credentials.ini')
    
    region_name = configuration.get('default', "region_name")
    aws_access_key_id = configuration.get('default', "aws_access_key_id")
    aws_secret_access_key = configuration.get('default', "aws_secret_access_key")
    aws_session_token = configuration.get('default', "aws_session_token")
    
    client = boto3.resource('dynamodb', region_name=region_name, aws_access_key_id=aws_access_key_id, 
                    aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
    table = client.Table('cloud9_users')

    #With Query Parameters
    # table.put_item(Item={
    #     'emailid' : event['queryStringParameters']['emailid'],
    #     'username' : event['queryStringParameters']["username"],
    #     'password' : event['queryStringParameters']["password"],
    #     'mobile' : event['queryStringParameters']["mobile"],
    #     'account_number' : event['queryStringParameters']["account_number"]
    #     })

    #With Body
    response = client.get_item(Key={'emailid': {'S': 'userwer2@gmail.com'}},TableName='cloud9_users')

    print(response)
    
    return {
          "statusCode": 200,
          "body": json.dumps({ 'status':'success', 'response' : response}),
          "headers": {
            "content-type": "application/json"
          }
    }
    