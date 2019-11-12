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
                info = (instanceIds + " " + state + "  " + tag + "\n")
                all_info.append(info)
print(all_info)
f= open("guru99.txt","w+")
for i in all_info:
     f.write(i)