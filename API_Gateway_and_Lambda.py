import boto3

# Creating an API Gateway client
apigateway = boto3.client('apigateway')

# Creating a REST API
rest_api = apigateway.create_rest_api(name='my-api')

# Creating a resource
resource = apigateway.create_resource(
    restApiId=rest_api['id'],
    parentId=None,
    pathPart='my-resource'
)

# Creating a method for the resource
method = apigateway.put_method(
    restApiId=rest_api['id'],
    resourceId=resource['id'],
    httpMethod='GET',
    authorizationType='NONE'
)

# Creating a Lambda function client
lambda_client = boto3.client('lambda')

# Creating a Lambda function
lambda_function = lambda_client.create_function(
    FunctionName='my-lambda-function',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',
    Handler='lambda_function.handler',
    Code={
        'S3Bucket': 'my-bucket',
        'S3Key': 'lambda_function.zip'
    },
    Description='My Lambda function',
    Timeout=300,
    MemorySize=128
)

# Adding a permission to allow API Gateway to invoke the Lambda function
lambda_client.add_permission(
    FunctionName=lambda_function['FunctionName'],
    StatementId='api-gateway',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com'
)

# Creating an integration between the API Gateway and the Lambda function
apigateway.put_integration(
    restApiId=rest_api['id'],
    resourceId=resource['id'],
    httpMethod='GET',
    type='AWS',
    integrationHttpMethod='POST',
    uri='arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/' + lambda_function['FunctionArn'] + '/invocations'
)

# Deploying the API
apigateway.create_deployment(
    restApiId=rest_api['id'],
    stageName='prod'
)
