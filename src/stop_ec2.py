import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    ec2 = boto3.client('ec2')

    # Stop EC2 instances
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:shutdown', 'Values': ['true']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.stop_instances(InstanceIds=[instance_id])
            logger.info(f'Stopped EC2 instance: {instance_id}')