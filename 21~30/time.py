from datetime import date
t = date.today()
d=date(2023,7,7)
print(t)
print(d)
print(d.weekday())

from datetime import datetime
n=datetime.now()
print(n)
print(n.year,n.month,n.day)
print(n.hour,n.minute,n.second,n.microsecond)

from datetime import datetime,timedelta
d1=datetime(2023,12,25,0,0,0)
d2=datetime(2023,11,25,0,0,0)
result=d1-d2
print(result)
print(result.days)

d=datetime(2023,12,25,3,0,0)
result2=d+timedelta(days=10)
print(result2)

from datetime import datetime,timedelta,timezone
JST=timezone(timedelta(hours=+9))
result3=datetime(2023,1,1,12,15,30,tzinfo=JST)
print(result3)

import jpholiday
result4 = jpholiday.year_holidays(2023)
print(result4)