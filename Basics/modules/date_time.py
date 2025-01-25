# import datetime
# datetime.datetime
from datetime import date
from datetime import time
from datetime import datetime, timedelta

birthday = date(1997, 2,21) # immutable object
print(birthday)

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

print(moon_landing.year)
print(moon_landing.month)
print(moon_landing.day)
print(type(birthday))

start = time()
print(start)
print(type(start))

print(start.hour)
print(start.minute)
print(start.second)

print((time(6)))
print(time(hour=6))
print(time(hour = 2, minute = 25))

print(time(23, 34, 22))

print(datetime(1999, 7, 24))
print(datetime(2001, 4, 17, 14, 16, 58))
# keyword arguments can be used with datetime

today = datetime.today()
print(today)

today_1 = datetime.now()
print(today_1)
# datetime objects are immutable

print(today.weekday())
# weekday returns 0-6, 0 denotes Monday

same_time_years_ago = today.replace(year = 2000, month = 1)
print(same_time_years_ago)

print(today.strftime("%m")) # month
print(today.strftime("%d")) # day
print(today.strftime("%m %d"))
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%m-%d-%Y"))
print(today.strftime("%m/%d/%y")) # lower case y gives 2 digit number for year

print(today.strftime("%A")) # day of date
print(today.strftime("%B")) # gives month as string

birthday_datetime = datetime(1997, 2, 21)
my_life_span = today - birthday_datetime
print(my_life_span) # returns timedelta object

print(my_life_span.total_seconds())

five_hundred_days = timedelta(days = 500, hours = 12) # doesnot accept months or years
print(five_hundred_days + five_hundred_days) # 1001 days

print(today + five_hundred_days)