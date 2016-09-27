
import time
import datetime
s = '20150101'
a = time.strptime(s,'%Y%m%d')
a_datetime=datetime.datetime(*a[:3])
s1 = '20150102'
a1 = time.strptime(s1,'%Y%m%d')
a1_datetime=datetime.datetime(*a1[:3])

o = 20160101


k = [1,2,3,4,5]
print type(max(k))


