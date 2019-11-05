import boto3

ec2 = boto3.client('ec2')


import boto3  
#ec2 = boto3.resource('ec2')
ec2 = boto3.client('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
#vpc.wait_until_available()
#return vpc
subnet1 = vpc.create_subnet(CidrBlock='10.0.0.0/24')
#IG
#return vpc
internet_gateway = ec2.create_internet_gateway()  
internet_gateway.attach_to_vpc(VpcId=vpc.vpc_id)
##Route Table
#return vpc
route_table = vpc.create_route_table()
route_ig_ipv4 = route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway.internet_gateway_id)  

route_table.associate_with_subnet(SubnetId=subnet1.id)
##########SG
sg = vpc.create_security_group(GroupName="sample-name", Description="A sample description")

ip_ranges = [{
    'CidrIp': '0.0.0.0/0'
}]

ip_v6_ranges = [{
    'CidrIpv6': '::/0'
}]

perms = [{
    'IpProtocol': 'TCP',
    'FromPort': 80,
    'ToPort': 80,
    'IpRanges': ip_ranges,
    'Ipv6Ranges': ip_v6_ranges
}, {
    'IpProtocol': 'TCP',
    'FromPort': 443,
    'ToPort': 443,
    'IpRanges': ip_ranges,
    'Ipv6Ranges': ip_v6_ranges
}, {
    'IpProtocol': 'TCP',
    'FromPort': 22,
    'ToPort': 22,
    'IpRanges': ip_ranges, # Remember to change this!
    'Ipv6Ranges': ip_v6_ranges # Remember to change this!
}]

sg.authorize_ingress(IpPermissions=perms)

