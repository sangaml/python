volume = ec2.create_volume(
    AvailabilityZone='ap-southeast-1c',
    Encrypted=False,
    Size=123,
    VolumeType='standard',
)


response = client.attach_volume(
    Device='string',
    InstanceId='string',
    VolumeId='string',
    DryRun=True|False
)