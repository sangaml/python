'''
Automation scripts
Script I 
- Write a python script to take the snapshot of volumes attached to the instance in the previous step.
- This script should tag the snapshot created using VM name + current timestamp. For e.g. Web Server + Timestamp
- In addition to this it should also perform snapshot retention task. Retention period 1 hour. All the snapshots older than that should be deleted.

Script II
- Write a script in python to shutdown the servers present in the infrastructure based on their tag.
- The servers which has tag as "Env=Dev" should be stopped.
- Create a list of stopped servers and upload it in to storage bucket for audit purpose. 

'''
###########################  Script 1 ##################################3
instanceid = input("Enter Instance id to start snapshot creation:")
import boto3
import datetime
from datetime import timedelta
from datetime import datetime
ec2 = boto3.client('ec2')
#------------------Retrieving ec2 instance info -----------------------
def Creating_snapshot(instanceid):

    instance_info = ec2.describe_instances(
    InstanceIds=[
            instanceid
        ]
    )
    test = (instance_info['Reservations'])
    for i in test:
        test1 = (i['Instances'])
        for j in test1:
            name = (j['Tags'])
            volume = (j['BlockDeviceMappings'])
            for k, l in zip(volume, name):
                volumeid = (k['Ebs']['VolumeId'])
                instancename = (l['Value'])

    #-------------Creating Snapshot------------------------------
    creating_snapshot = ec2.create_snapshot(
        VolumeId=volumeid
    )
    snapshotid = (creating_snapshot['SnapshotId'])
    creationdate = (creating_snapshot['ResponseMetadata']['HTTPHeaders']['date'])
    ec2.create_tags(Resources=[snapshotid],Tags=[{"Key": "Name", "Value": instancename + creationdate}])


#------------------- Delete Snapshot & Retrieving Snapshots info-----------------------
def Delete_snapshot(snapshotid):
    nowo = str(datetime.utcnow())
    nowt = str(nowo[:19])

    response = ec2.describe_snapshots(
        SnapshotIds=[
            snapshotid
        ]
    )
    datetimeFormat = '%Y-%m-%d %H:%M:%S'
    a = (response['Snapshots'])
    for s in a:
        b = str(s['StartTime'])
        new = (b[:19])
        test22 = str(datetime.strptime(new, datetimeFormat))

    diff = datetime.strptime(nowt, datetimeFormat)\
        - datetime.strptime(test22, datetimeFormat)

    print("Seconds:", diff.seconds)

    if diff.second >= 3600:
        del_snapshot = ec2.delete_snapshot(
        SnapshotId=snapshotid
        )


##################################### Script II ##################################

import boto3

ec2 = boto3.client('ec2')
vms = ec2.describe_instances()
a = (vms['Reservations'])
for i in a:
    j = (i['Instances'])
    for k in j:
        instanceIds = (k['InstanceId'])
        l = (k['Tags'])
        state = (k['State']['Name'])
        for m in l:
            tag = (m['Value'])

if tag == 'Dev':
    if state == 'running':
        print('Match Found, Deleting vm....')
        stopvm = ec2.terminate_instances(InstanceIds=[instanceIds])
else:
    print("No Match Found")

#-------------------Copy Data to S3-------------------

import boto3
all_state = []
all_instanceIds = []
all_tag = []
all_info = []
ec2 = boto3.client('ec2')
vms = ec2.describe_instances()
a = (vms['Reservations'])
for i in a:
    j = (i['Instances'])
    for k in j:
        instanceIds = (k['InstanceId'])
        all_instanceIds.append(instanceIds)
        l = (k['Tags'])
        state = (k['State']['Name'])
        all_state.append(state)
        for m in l:
            tag = (m['Value'])
            all_tag.append(tag)
            #print(state)
            if state == 'stopped':
                info = (instanceIds + " " +state + "  " + tag)
                all_info.append(info)
#-------------------Puting data on s3----------------------
nowo = str(datetime.utcnow())
nowt = str(nowo[:10])
bucket='mystoppedec2status'
bucketname = str(bucket + nowt)
#-------Creating bucket----------------
s3 = boto3.client('s3')
create_s3 = s3.create_bucket(ACL='private',Bucket=bucketname,CreateBucketConfiguration={'LocationConstraint': 'ap-south-1' })
#--------------copying data to bucket---------
putbucket = s3.put_object(
    ACL='private',
    Body=all_info,
    Bucket=bucketname,
    Key='testing',
    StorageClass='STANDARD'
)