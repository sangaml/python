import boto3
ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(
    CidrBlock='10.0.0.0/16')

