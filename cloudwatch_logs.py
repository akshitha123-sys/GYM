import boto3

# Creating a CloudWatch Logs client
cloudwatch_logs = boto3.client('logs')

# Creating a log group
cloudwatch_logs.create_log_group(logGroupName='my-log-group')

# Creating a log stream
cloudwatch_logs.create_log_stream(logGroupName='my-log-group', logStreamName='my-log-stream')

# Configuring the CloudWatch Logs agent to send logs to CloudWatch
# We can use the UserData parameter to run a script when launching the instance
userdata = '''
#!/bin/bash
yum install -y awslogs
service awslogs start
'''

# Launching the instance with the UserData parameter
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-0123456789',
    InstanceType='t2.micro',
    KeyName='my-key-pair',
    UserData=userdata,
    SecurityGroupIds=['sg-0123456789'],
    SubnetId='subnet-0123456789'
)[0]
