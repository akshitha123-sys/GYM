import boto3

# Creating a CloudWatch Logs client
cloudwatch_logs = boto3.client('logs')

# Creating a log group
cloudwatch_logs.create_log_group(logGroupName='my-log-group')

# Creating a log stream for the gym application's logs
cloudwatch_logs.create_log_stream(logGroupName='my-log-group', logStreamName='my-app-log-stream')
