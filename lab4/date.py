#1
from datetime import date,  timedelta, datetime
current = date.today() - timedelta(5)
print("Current time: ", date.today())
print("Subtract five days : ",current)

#2
from datetime import datetime, timedelta
today = datetime.today().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime
now = datetime.now().replace(microsecond=0)
print("Datetime without microseconds:", now)

#4
from datetime import datetime
date1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
diff_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", int(diff_seconds))

