import boto3
import json

# I am now creating an S3 client
s3 = boto3.client('s3')

# I am now creating a new bucket
bucket_name = 'my-project-bucket'
s3.create_bucket(Bucket=bucket_name)

# I am now defining the bucket policy
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowGetObject",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:role/user-role",
                    "arn:aws:iam::123456789012:role/admin-role"
                ]
            },
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

# I am now setting the bucket policy
s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
