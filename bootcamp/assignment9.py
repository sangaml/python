#
import boto3
import time
ec2 = boto3.client('ec2')
reservations = ec2.get_all_reservations(
    filters={'instance-state-name': 'running'})