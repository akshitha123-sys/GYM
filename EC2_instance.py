# Launching an EC2 instance with the necessary specifications to host the Django application
import boto3

ec2 = boto3.client('ec2')

# Creating a security group
security_group_name = 'gym-project-security-group'
security_group_description = 'Security group for gym project'
vpc_id = 'vpc-123456'
response = ec2.create_security_group(GroupName=security_group_name,
Description=security_group_description,
VpcId=vpc_id)
security_group_id = response['GroupId']

# Allowing inbound traffic on necessary ports
ec2.authorize_security_group_ingress(
GroupId=security_group_id,
IpPermissions=[
{
'IpProtocol': 'tcp',
'FromPort': 22,
'ToPort': 22,
'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
},
{
'IpProtocol': 'tcp',
'FromPort': 80,
'ToPort': 80,
'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
},
{
'IpProtocol': 'tcp',
'FromPort': 443,
'ToPort': 443,
'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
}
]
)

# Launching EC2 instance
instance_type = 't2.micro'
key_name = 'gym-project-keypair'
ami_id = 'ami-0c55b159cbfafe1f0'
subnet_id_public = 'subnet-123456'
security_group_ids = [security_group_id]
user_data = '''#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
sudo yum install -y python3
sudo pip3 install django
sudo mkdir /var/www/html/gym
sudo chmod 777 /var/www/html/gym
'''

instance = ec2.run_instances(
ImageId=ami_id,
InstanceType=instance_type,
KeyName=key_name,
SubnetId=subnet_id_public,
SecurityGroupIds=security_group_ids,
UserData=user_data
)

instance_id = instance['Instances'][0]['InstanceId']

print('EC2 instance has been launched with instance id:', instance_id)

# Creating a CloudWatch Logs client
cloudwatch_logs = boto3.client('logs')

# Creating a log group
cloudwatch_logs.create_log_group(logGroupName='my-log-group')

# Creating a log stream
cloudwatch_logs.create_log_stream(logGroupName='my-log-group', logStreamName='my-log-stream')

# Configuring the CloudWatch Logs agent to send logs to CloudWatch
# One can use the UserData parameter to run a script when launching the instance
userdata = '''
#!/bin/bash
yum install -y awslogs
service awslogs start
'''

# Launch the instance with the UserData parameter
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-0123456789',
    InstanceType='t2.micro',
    KeyName='my-key-pair',
    UserData=userdata,
    SecurityGroupIds=['sg-0123456789'],
    SubnetId='subnet-0123456789'
)[0]
