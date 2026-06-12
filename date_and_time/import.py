import datetime
now = datetime.datetime.now()
print(now)
# To get only date 
get_Date = datetime.date.today()
print(get_Date)

get_only_time = datetime.datetime.now()
print(get_only_time.time())

date_ = datetime.date.today()
print(date_.month) #To print the month 
print(date_.day)#To print the day 
print(date_.year)#To print the year 

# create your own date 
own_date = datetime.date(2026, 11, 5)
print(own_date)
# create your own date and time 
own_date_time = datetime.datetime(2005,2,5,12,30,0)
print(own_date_time) 

# Format Date Using strftime()
written_date = datetime.datetime.now()
print(written_date.strftime("%A"))

# | Code | Meaning        |
# | ---- | -------------- |
# | `%d` | Day            |
# | `%m` | Month          |
# | `%Y` | Year           |
# | `%H` | Hour (24-hour) |
# | `%M` | Minute         |
# | `%S` | Second         |
# | `%A` | Weekday        |
# | `%B` | Month name     |

# Date diffrence

d1 = datetime.date(2026, 6, 1)
d2 = datetime.date(2026, 6, 12)

difference = d2 - d1

print(difference.days)

# To add new dates in calander 
today = datetime.date.today()

future = today + datetime.timedelta(days=10)

print(future)