# I am now Creating IAM roles for users and admins
import boto3

iam = boto3.client('iam')

# Creating role for users
users_role = iam.create_role(
RoleName='gym-users-role',
AssumeRolePolicyDocument={
'Version': '2012-10-17',
'Statement': [
{
'Effect': 'Allow',
'Principal': {'Service': 'lambda.amazonaws.com'},
'Action': 'sts:AssumeRole'
}
]
}
)

# I am now Attaching necessary policies to users role
iam.attach_role_policy(
PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
RoleName='gym-users-role'
)

iam.attach_role_policy(
PolicyArn='arn:aws:iam::aws:policy/AmazonRDSReadOnlyAccess',
RoleName='gym-users-role'
)

# I am now Creating role for admins
admins_role = iam.create_role(
RoleName='gym-admins-role',
AssumeRolePolicyDocument={
'Version': '2012-10-17',
'Statement': [
{
'Effect': 'Allow',
'Principal': {'Service': 'lambda.amazonaws.com'},
'Action': 'sts:AssumeRole'
}
]
}
)

# I am now Attaching necessary policies to admins role
iam.attach_role_policy(
PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
RoleName='gym-admins-role'
)

iam.attach_role_policy(
PolicyArn='arn:aws:iam::aws:policy/AmazonRDSFullAccess',
RoleName='gym-admins-role'
)

iam.attach_role_policy(
PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',
RoleName='gym-admins-role'
)