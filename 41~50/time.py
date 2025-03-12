from dateutil.relativedelta import relativedelta
from datetime import datetime

today = datetime.today()
print(today)

today_str=today.strftime('%Y年%m月%d日')
print(today_str)

d1=today - relativedelta(months=7)
print(d1)

import calendar
c = calendar.month(2023,1)
print(c)

w,days=calendar.monthrange(2023,7)
print(days)