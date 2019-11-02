#pip install boto3

'''
Infra creation
Write a code in python to setup infrastructure in the public cloud of your choice (AWS/Azure/GCP/Openshift etc.)                                             
- A front end layer consisting of one web server accepting traffic (private subnet) from load balancer.                                                      
- Install nginx or apache HTTP server as well as latest version of python through startup script.                                                            
- Add another VM called DB VM which will host the database and will accept the traffic from web VM. Install mysql DB through startup script on this VM.      
- Attach 5 GB volume to this instance while instance creation.                                                                                               
- Spin up one more VM in the public subnet acting as jump server or bastion host.                                                                            
- Use custom VNET/VPC, subnets, firewall/security group rules to limit/allow the traffic.                                                                    
- Add tags to these instances. For e.g. Web and DB vm will have tag as Env=Prod, Jump server will have tag as Env=Dev
'''

import logging
import boto3
from botocore.exceptions import ClientError


def create_ec2_instance(image_id, instance_type, keypair_name):
    """Provision and launch an EC2 instance

    The method returns without waiting for the instance to reach
    a running state.

    :param image_id: ID of AMI to launch, such as 'ami-XXXX'
    :param instance_type: string, such as 't2.micro'
    :param keypair_name: string, name of the key pair
    :return Dictionary containing information about the instance. If error,
    returns None.
    """

    # Provision and launch the EC2 instance
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]

    # import boto3  
    # ec2 = boto3.resource('ec2')
    # vpc = ec2_client.create_vpc(CidrBlock='10.0.0.0/16')
    # vpc.wait_until_available()
    # return vpc
    # subnet1 = vpc.create_subnet(CidrBlock='10.0.0.0/24')

def main():
    """Exercise create_ec2_instance()"""

    # Assign these values before running the program
    image_id = 'ami-0123b531fc646552f'
    instance_type = 't2.micro'
    keypair_name = 'sangamtest'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Provision and launch the EC2 instance
    instance_info = create_ec2_instance(image_id, instance_type, keypair_name)
    if instance_info is not None:
        logging.info(f'Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info(f'    VPC ID: {instance_info["VpcId"]}')
        logging.info(f'    Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info(f'    Current State: {instance_info["State"]["Name"]}')


if __name__ == '__main__':
    main()


