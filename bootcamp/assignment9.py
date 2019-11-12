import datetime
import time
from datetime import timedelta
import boto3
#import time
import datetime
from datetime import timedelta

from datetime import datetime

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat)\
    - datetime.datetime.strptime(date2, datetimeFormat)
print(diff)
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
import time
import pytz  # 3rd party: $ pip install pytz
import datetime
u = datetime.now()
u = u.replace(tzinfo=pytz.utc) #NOTE: it works only with a fixed utc offset
print(u)
# import boto3
# #import time
# import datetime
# from datetime import timedelta

# from datetime import datetime

# nowo = str(datetime.now())
# nowt = str(nowo[:19])
# print("------------------------")
# print(nowt)