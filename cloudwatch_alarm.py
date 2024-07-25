import boto3

# Setting up a CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Defining the CPU usage metric to monitor
cpu_metric = 'AWS/EC2 CPUUtilization'

# Defining the dimensions for the metric
dimensions = [
    {
        'Name': 'InstanceId',
        'Value': 'i-0123456789abcdefg'
    }
]

# Creating the CloudWatch alarm
cloudwatch.put_metric_alarm(
    AlarmName='CPUUsageAlarm',
    MetricName=cpu_metric,
    Namespace='AWS/EC2',
    Dimensions=dimensions,
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=90.0,
    ComparisonOperator='GreaterThanThreshold',
    AlarmActions=[
        'arn:aws:sns:us-east-1:123456789012:MyTopic'
    ],
    OKActions=[
        'arn:aws:sns:us-east-1:123456789012:MyTopic'
    ],
    InsufficientDataActions=[]
)
