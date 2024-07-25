import boto3

# Specifying the region where the RDS instance is located
region = 'us-east-1'

# Specifying the name of the RDS security group
security_group_name = 'my-rds-security-group'

# Specifying the ARNs of the IAM roles that should have access to the RDS instance
admin_role_arn = 'arn:aws:iam::123456789012:role/admin-role'
client_role_arn = 'arn:aws:iam::123456789012:role/client-role'

# Creating a new security group and adding the necessary ingress rules
ec2 = boto3.client('ec2', region_name=region)
response = ec2.create_security_group(GroupName=security_group_name,
                                      Description='Security group for my RDS instance')
security_group_id = response['GroupId']
ec2.authorize_security_group_ingress(GroupId=security_group_id,
                                     IpPermissions=[{'IpProtocol': 'tcp',
                                                     'FromPort': 3306,
                                                     'ToPort': 3306,
                                                     'UserIdGroupPairs': [{'Description': 'Allow access from admin role',
                                                                           'GroupId': security_group_id,
                                                                           'UserId': admin_role_arn},
                                                                          {'Description': 'Allow access from client role',
                                                                           'GroupId': security_group_id,
                                                                           'UserId': client_role_arn}]}])

# Updating the RDS instance to use the new security group
rds = boto3.client('rds', region_name=region)
rds.modify_db_instance(DBInstanceIdentifier='my-rds-instance',
                        VpcSecurityGroupIds=[security_group_id])
