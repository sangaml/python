# Create VPC

import boto3
import time
ec2 = boto3.client('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
time.sleep(2)
vpcid = (vpc['Vpc']['VpcId'])
ec2.create_tags(Resources=[vpcid],Tags=[{"Key": "Name", "Value": "custom_vpc"}])

# Creating Subnet1

Subnet1 = ec2.create_subnet(CidrBlock='10.0.1.0/24',VpcId=vpcid)
time.sleep(2)
subnetid1 = (Subnet1['Subnet']['SubnetId'])
ec2.create_tags(Resources=[subnetid1],Tags=[{"Key": "Name", "Value": "subnet1"}])
print(subnetid1)

# Creating Subnet2

Subnet2 = ec2.create_subnet(CidrBlock='10.0.2.0/24',VpcId=vpcid)
time.sleep(2)
subnetid2 = (Subnet2['Subnet']['SubnetId'])
ec2.create_tags(Resources=[subnetid2],Tags=[{"Key": "Name", "Value": "subnet2"}])
print(subnetid2)

