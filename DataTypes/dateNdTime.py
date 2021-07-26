import datetime
import DateTime
from DateTime import Timezones
zones = set(Timezones())


s_date = "02-sep-1987"
timestamp = datetime.datetime.now()
# cur_date = datetime.date(day=2, month=9, year=1986)
cur_date = timestamp.date()
cur_time = timestamp.time()

time_zone = timestamp.astimezone()

print(timestamp)
print("cur_date: ", cur_date)
print("cur_time: ", cur_time)
print("time_zone: ", time_zone)

print("%D", cur_date.strftime("%D"))
print("%d", cur_date.strftime("%d"))
print("%m", cur_date.strftime("%m"))
print("%M", cur_date.strftime("%mmm"))
print("%MM", cur_date.strftime("%MM"))
print("%Y", cur_date.strftime("%Y"))
print("%y", cur_date.strftime("%y"))
print("%YYYY", cur_date.strftime("%YYYY"))
print("%a", cur_date.strftime("%a"))
print("%b", cur_date.strftime("%b"))

print("zones", zones)
print(Timezones)
