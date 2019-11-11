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
#--------------------Script 1 -----------------
import boto3
import time

from datetime import datetime
now = datetime.now()
creation_time = now.strftime("%H:%M:%S")

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
InstanceIds=[
        'i-0d00216f7e9e2f3cc'
    ]
)
test = (response['Reservations'])
for i in test:
    test1 = (i['Instances'])
    for j in test1:
        name = (j['Tags'])
        volume = (j['BlockDeviceMappings'])
        for k, l in zip(volume, name):
            device = (k['DeviceName'])
            volumeid = (k['Ebs']['VolumeId'])
            instancename = (l['Value'])

#-------------Creating Snapshot
response = ec2.create_snapshot(
    VolumeId=volumeid
)
snapshotid = (response['SnapshotId'])
creationdate = (response['ResponseMetadata']['HTTPHeaders']['date'])
ec2.create_tags(Resources=[snapshotid],Tags=[{"Key": "Name", "Value": instancename + creationdate}])

#------------Delete Snapshot-----------
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
retentionp = '01:00:00'
if (current_time - creation_time) >= (retentionp):
    response = ec2.delete_snapshot(
    SnapshotId=snapshotid
)
