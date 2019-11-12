import boto3

s3 = boto3.client('s3')

create_s3 = s3.create_bucket(ACL='private',Bucket='mybucketsangamdevguru',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1' })
print(create_s3)

f= open("guru99.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
# print(all_instanceIds)
# print(all_state)
# print(all_tag)
# if tag == 'Dev':
#     if state == 'stop':
#         print('Match Found, Deleting vm....')
#         stopvm = ec2.terminate_instances(InstanceIds=[instanceIds])
# else:
#     print("No Match Found")
        

        