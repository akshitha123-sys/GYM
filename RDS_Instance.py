import boto3

# creating RDS client
client = boto3.client('rds')

# setting up database parameters
db_instance_identifier = 'gym-management-db'
db_engine = 'mysql'
db_engine_version = '5.7.33'
db_instance_class = 'db.t2.micro'
master_username = 'admin'
master_password = 'password123'
allocated_storage = 30

# creating database instance
response = client.create_db_instance(
    DBInstanceIdentifier=db_instance_identifier,
    Engine=db_engine,
    EngineVersion=db_engine_version,
    DBInstanceClass=db_instance_class,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    AllocatedStorage=allocated_storage
)

# printing response
print(response)
