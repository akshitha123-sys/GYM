import boto3

def create_user(username, password, email, phone):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('gym_users')
    table.put_item(
        Item={
            'username': username,
            'password': password,
            'email': email,
            'phone': phone
        }
    )
