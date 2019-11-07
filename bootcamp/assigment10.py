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