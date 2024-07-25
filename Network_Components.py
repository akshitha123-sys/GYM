import boto3

# Creating EC2 client
ec2 = boto3.client('ec2')

# Creating VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']

# Adding a name tag to VPC
ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': 'my-vpc'}])

# Enabling DNS support and hostname
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

# Creating public subnet
public_subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1a')
public_subnet_id = public_subnet['Subnet']['SubnetId']

# Adding a name tag to the public subnet
ec2.create_tags(Resources=[public_subnet_id], Tags=[{'Key': 'Name', 'Value': 'public-subnet'}])

# Creating a private subnet
private_subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24', AvailabilityZone='us-east-1a')
private_subnet_id = private_subnet['Subnet']['SubnetId']

# Adding name tag to private subnet
ec2.create_tags(Resources=[private_subnet_id], Tags=[{'Key': 'Name', 'Value': 'private-subnet'}])

# Creating a internet gateway
internet_gateway = ec2.create_internet_gateway()
internet_gateway_id = internet_gateway['InternetGateway']['InternetGatewayId']

# Attaching internet gateway to VPC
ec2.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)

# Creating a route table for public subnet
public_route_table = ec2.create_route_table(VpcId=vpc_id)
public_route_table_id = public_route_table['RouteTable']['RouteTableId']

# Adding a route for internet gateway to public route table
ec2.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway_id, RouteTableId=public_route_table_id)

# Associate public subnet with public route table
ec2.associate_route_table(RouteTableId=public_route_table_id, SubnetId=public_subnet_id)

# Creating a NAT gateway
nat_gateway = ec2.create_nat_gateway(SubnetId=public_subnet_id, AllocationId='allocation_id')
nat_gateway_id = nat_gateway['NatGateway']['NatGatewayId']

# Creating a route table for private subnet
private_route_table = ec2.create_route_table(VpcId=vpc_id)
private_route_table_id = private_route_table['RouteTable']['RouteTableId']

# Adding a route for NAT gateway to private route table
ec2.create_route(DestinationCidrBlock='0.0.0.0/0', NatGatewayId=nat_gateway_id, RouteTableId=private_route_table_id)

# Associating private subnet with private route table
ec2.associate_route_table(RouteTableId=private_route_table_id, SubnetId=private_subnet_id)

# Creating a security group
security_group = ec2.create_security_group(GroupName='my-security-group', Description='Security group for my project', VpcId=vpc_id)
security_group_id = security_group['GroupId']

# Allowing inbound traffic on necessary ports
ec2_sg.authorize_ingress(
IpProtocol='tcp',
FromPort=22,
ToPort=22,
CidrIp='0.0.0.0/0' # allows SSH access from any IP address
)

ec2_sg.authorize_ingress(
IpProtocol='tcp',
FromPort=80,
ToPort=80,
CidrIp='0.0.0.0/0' # allows HTTP access from any IP address
)

ec2_sg.authorize_ingress(
IpProtocol='tcp',
FromPort=443,
ToPort=443,
CidrIp='0.0.0.0/0' # allows HTTPS access from any IP address
)

ec2_sg.authorize_ingress(
IpProtocol='tcp',
FromPort=3306,
ToPort=3306,
CidrIp='10.0.1.0/24' # allows access to MySQL from the private subnet
)
