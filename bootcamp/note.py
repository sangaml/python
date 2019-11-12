import datetime
from datetime import datetime
nowo = str(datetime.utcnow())
nowt = str(nowo[:10])
bucket='mystoppedec2sangam'
bucketname = str(bucket + nowt)
print(bucketname)

s3 = boto3.client('s3')

create_s3 = s3.create_bucket(ACL='private',Bucket=bucketname,CreateBucketConfiguration={'LocationConstraint': 'ap-south-1' })

putbucket = s3.put_object(
    ACL='private',
    Body=data,
    Bucket=bucketname,
    Key='testing',
    StorageClass='STANDARD'
)
print(putbucket)