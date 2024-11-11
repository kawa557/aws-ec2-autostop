import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ec2 = boto3.client('ec2')

def handler(event, context):
    # Stop EC2 instances
    try:
        instances = ec2.describe_instances(Filters=[
            {'Name': 'tag:shutdown', 'Values': ['true']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ])
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                ec2.stop_instances(InstanceIds=[instance_id])
                logger.info(f'Stopped EC2 instance: {instance_id}')

    except Exception as e:
        logger.error('An error occurred')
        logger.error(e)