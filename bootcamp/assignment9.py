# # ---------------------- Create VPC ----------------------------  

import boto3
import time

ec2 = boto3.client('ec2')
print("Creating VPC...")
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16',InstanceTenancy='default')
time.sleep(2)
vpcid = (vpc['Vpc']['VpcId'])

ec2.create_tags(Resources=[vpcid],Tags=[{"Key": "Name", "Value": "custom_vpc"}])

EnableDnsHostname = ec2.modify_vpc_attribute(EnableDnsHostnames={'Value': True},VpcId=vpcid)
Routetable = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpcid] }])
test = (Routetable['RouteTables'][0]['Associations'])
for i in test:
    default_route_table_id = (i['RouteTableId'])


# ----------------------- Creating Subnet1 ------------------------
print("Creating Public Subnet 1...")
Subnet1 = ec2.create_subnet(AvailabilityZone='ap-southeast-1a',CidrBlock='10.0.1.0/24',VpcId=vpcid)
time.sleep(2)
subnetid1 = (Subnet1['Subnet']['SubnetId'])
ec2.create_tags(Resources=[subnetid1],Tags=[{"Key": "Name", "Value": "Public"}])

# ---------------------Creating Subnet2-------------------------
print("Creating Private Subnet...")
Subnet2 = ec2.create_subnet(AvailabilityZone='ap-southeast-1c',CidrBlock='10.0.2.0/24',VpcId=vpcid)
time.sleep(2)
subnetid2 = (Subnet2['Subnet']['SubnetId'])
ec2.create_tags(Resources=[subnetid2],Tags=[{"Key": "Name", "Value": "Private"}])

# ----------------------- Creating Subnet3 ------------------------
print("Creating Public Subnet 2...")
Subnet3 = ec2.create_subnet(AvailabilityZone="ap-southeast-1b",CidrBlock='10.0.3.0/24',VpcId=vpcid)
time.sleep(2)
subnetid3 = (Subnet3['Subnet']['SubnetId'])
ec2.create_tags(Resources=[subnetid3],Tags=[{"Key": "Name", "Value": "Public2"}])

#----------------------------creating internet_gateway----------------------
print("Creating Internet gateway...")
internet_gateway = ec2.create_internet_gateway()  
internet_gateway_id = (internet_gateway['InternetGateway']['InternetGatewayId'])
ec2.create_tags(Resources=[internet_gateway_id],Tags=[{"Key": "Name", "Value": "custom_igw"}])

#Attaced igw to vpc

attached_igw = ec2.attach_internet_gateway(InternetGatewayId=internet_gateway_id,VpcId=vpcid)


#-----------------------------Create Elastic IP--------------------------
print("Creating Elastic IP...")
EIP = ec2.allocate_address(Domain='vpc') 
EIP_ID = (EIP['AllocationId'])
ec2.create_tags(Resources=[EIP_ID],Tags=[{"Key": "Name", "Value": "my_EIP"}])

# ----------------------------Create Nat GW---------------------------
print("Creating Nat Gateway...")
Nat_gw = ec2.create_nat_gateway(AllocationId=EIP_ID,SubnetId=subnetid1)
time.sleep(10)
Nat_gw_id = (Nat_gw['NatGateway']['NatGatewayId'])
ec2.create_tags(Resources=[Nat_gw_id],Tags=[{"Key": "Name", "Value": "My_Nat_gw"}])

#-------------------------------Create public Route table--------------------------
print("Creating Public Routeable...")
Route_Table_route = ec2.create_route(
    RouteTableId=default_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id
)
ec2.create_tags(Resources=[default_route_table_id],Tags=[{"Key": "Name", "Value": "Public Route table"}])

# #------------------------------Create private Route table-----------------------------------
print("Creating Private Routeable...")
Route_Table_private = ec2.create_route_table(VpcId=vpcid)
Route_Table_private_id = (Route_Table_private['RouteTable']['RouteTableId'])
Route_Table_route = ec2.create_route(
    RouteTableId=Route_Table_private_id,
    DestinationCidrBlock='0.0.0.0/0',
    NatGatewayId=Nat_gw_id,
)
ec2.create_tags(Resources=[Route_Table_private_id],Tags=[{"Key": "Name", "Value": "Private Route table"}])

#Associate subnets with route tables
Route_Table_public_associate = ec2.associate_route_table(RouteTableId=default_route_table_id,SubnetId=subnetid1)
Route_Table_public2_associate = ec2.associate_route_table(RouteTableId=default_route_table_id,SubnetId=subnetid3)
Route_Table_private_associate = ec2.associate_route_table(RouteTableId=Route_Table_private_id,SubnetId=subnetid2)

#------------------------------Creating Secrity group for jump server-----------------------------------
print("Creating Secirity group for jump server...")
jump_sg = ec2.create_security_group(
    Description='Creating Secirity group for jump server',
    GroupName='jump_server',
    VpcId=vpcid
)
jump_sg_id = (jump_sg['GroupId'])
ec2.create_tags(Resources=[jump_sg_id],Tags=[{"Key": "Name", "Value": "jump_sg"}])
time.sleep(2)
#Creating Secrity group for web server
print("Creating Secirity group for web server...")
web_sg = ec2.create_security_group(
    Description='Creating Secirity group for web server',
    GroupName='web_server',
    VpcId=vpcid
)

web_sg_id = (web_sg['GroupId'])
ec2.create_tags(Resources=[web_sg_id],Tags=[{"Key": "Name", "Value": "web_sg"}])

# #--------------------------------Creating Secrity group for db server---------------------------------
# print("Creating Secirity group for db server...")
# db_sg = ec2.create_security_group(
#     Description='Creating Secirity group for db server',
#     GroupName='web_server',
#     VpcId=vpcid
# )
# db_sg_id = (db_sg['GroupId'])
#ec2.create_tags(Resources=[db_sg_id],Tags=[{"Key": "Name", "Value": "db_sg"}])

# #-------------------------------Creating Secrity group for LoadBalancer--------------------------
print("Creating Secirity group for LoadBalancer...")
loadBalancer_sg = ec2.create_security_group(
    Description='Creating Secirity group for LoadBalancer',
    GroupName='loadBalancer_sg',
    VpcId=vpcid
)
loadBalancer_sg_id = (loadBalancer_sg['GroupId'])
ec2.create_tags(Resources=[loadBalancer_sg_id],Tags=[{"Key": "Name", "Value": "loadbalancer_sg"}])

# # -------------------------- Create NSG-Rules for Load Balancer ------------------------------

loadbalancer_sg_rule = ec2.authorize_security_group_ingress(
    GroupId=loadBalancer_sg_id,
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'open http port'
                },
            ],
            'ToPort': 80
        }
    ]
)

#-----------------------Creating NSG-Rules for jump server-------------------------------
jump_sg_rule = ec2.authorize_security_group_ingress(
    GroupId=jump_sg_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'open ssh port'
                },
            ],
            'ToPort': 22
        }
    ]
)
web_sg_rule = ec2.authorize_security_group_ingress(
    GroupId=web_sg_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'TCP',
            'ToPort': 22,
            'UserIdGroupPairs': [
                {
                    'Description': 'Allow Traffic only from Jump server',
                    'GroupId': jump_sg_id
                },
            ],
        },
        {
            'FromPort': 80,
            'IpProtocol': 'TCP',
            'ToPort': 80,
            'UserIdGroupPairs': [
                {
                    'Description': 'Allow Traffic only from Load Balancer',
                    'GroupId': loadBalancer_sg_id
                },
            ]
        },
    ],

)

# db_sg_rule = ec2.authorize_security_group_ingress(
#     GroupId=db_sg_id,
#     IpPermissions=[
#         {
#             'FromPort': 22,
#             'IpProtocol': 'TCP',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                     'Description': 'open web port'
#                 },
#             ],
#             'ToPort': 22
#         },
#         {
#             'FromPort': 3306,
#             'IpProtocol': 'TCP',
#             'IpRanges': [
#                 {
#                     'CidrIp': '0.0.0.0/0',
#                     'Description': 'open mysql port'
#                 },
#             ],
#             'ToPort': 3306
#         }
#     ]
# )

#-----------------------------Creating Load Balancer----------------------------
elb = boto3.client('elbv2')
print('Creating Application Load Balancer Target Group...')
elb_target_group = elb.create_target_group(
    Name='ALB-Target-Group',
    Protocol='HTTP',
    Port=80,
    VpcId=vpcid,
    HealthCheckProtocol='HTTP',
    HealthCheckPort='80',
    HealthCheckEnabled=True,
    HealthCheckIntervalSeconds=30,
    HealthCheckTimeoutSeconds=5,
    HealthyThresholdCount=5,
    UnhealthyThresholdCount=2,
    Matcher={
        'HttpCode': '200'
    },
    TargetType='instance'
)

albtarget = (elb_target_group['TargetGroups'])
for i in albtarget:
    ALB_target_ARN_ID = (i['TargetGroupArn'])

#--------------------------Creating Load_Balancer -----------------------------------
print('Creating Application Load Balancer...')
Load_Balancer = elb.create_load_balancer(
    Name='FrontEnd-ALB',
    Subnets=[
        subnetid1,
        subnetid2,
        subnetid3
    ],
    SecurityGroups=[
        loadBalancer_sg_id,
    ],
    Scheme='internet-facing',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'FrontEnd-ALB'
        },
    ],
    Type='application',
    IpAddressType='ipv4'
)
ALB = (Load_Balancer['LoadBalancers'])
for i in ALB:
    ALB_ARN_ID = (i['LoadBalancerArn'])

#----------------------Creating Load_Balancer_listner -----------------------------
print('Creating Application Load Balancer Listner...')
Load_Balancer_listner = elb.create_listener(
    LoadBalancerArn=ALB_ARN_ID,
    Protocol='HTTP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': ALB_target_ARN_ID,
            'Order': 1,
        },
    ]
)
user_data = '''#!/bin/bash
apt update
apt install apache2 -y
'''
# ------------------Creating web EC2 instance------------------------
print("Creating web EC2 instance...")
ec2 = boto3.client('ec2')
web_server = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2',
                'Encrypted': False,
            }
        },
    ],
    ImageId="ami-061eb2b23f9f8839c",
    InstanceType='t2.micro',
    KeyName='sangamtest',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    UserData=user_data,
    InstanceInitiatedShutdownBehavior='stop',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': False,
            'DeleteOnTermination': True,
            'Description': 'Creating network',
            'DeviceIndex': 0,
            'Groups': [
                web_sg_id,
            ],
            'SubnetId': subnetid2
        },  
    ],
) 
instanceid_web = (web_server['Instances'])
for i in instanceid_web:
    web_instance_id = (i['InstanceId'])
ec2.create_tags(Resources=[web_instance_id],Tags=[{"Key": "Name", "Value": "Web_Server"}])

# ------------------Creating jump EC2 instance------------------------
print("Creating jump EC2 instance...")
ec2 = boto3.client('ec2')
jump_server = ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2',
                'Encrypted': False,
            }
        },
    ],
    ImageId="ami-061eb2b23f9f8839c",
    InstanceType='t2.micro',
    KeyName='sangamtest',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    UserData=user_data,
    InstanceInitiatedShutdownBehavior='stop',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            'Description': 'Creating network',
            'DeviceIndex': 0,
            'Groups': [
                jump_sg_id,
            ],
            'SubnetId': subnetid1
        },  
    ],
) 
instanceid_jump = (jump_server['Instances'])
for i in instanceid_jump:
    jump_instance_id = (i['InstanceId'])
ec2.create_tags(Resources=[jump_instance_id],Tags=[{"Key": "Name", "Value": "Jump_Server"}])
time.sleep(90)
#Creating  register target
print('Regiser targets into alb...')
albregistertarget = elb.register_targets(
    TargetGroupArn=ALB_target_ARN_ID,
    Targets=[
        {
            'Id': web_instance_id,
            'Port': 80,
        },
    ]
)

