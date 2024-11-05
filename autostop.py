import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # 全インスタンスを取得
    instances = ec2.describe_instances()
    instance_ids = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            # タグを確認
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            if tags.get('auto_shutdown') == 'true':
                instance_ids.append(instance['InstanceId'])
    
    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped your instances: {instance_ids}')
    else:
        print('No instances to stop')
