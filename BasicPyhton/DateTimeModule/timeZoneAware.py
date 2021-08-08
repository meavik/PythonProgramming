import  datetime
import pytz

dt = datetime.datetime.now(tz=pytz.utc)
print(dt)
dt_mytz = dt.astimezone(pytz.timezone('Asia/Dhaka'))
print(dt_mytz)
# for tz in pytz.all_timezones:
#     print(tz)

'''making a naive datetime an aware datetime'''
dt_tz = datetime.datetime.now()
my_tz = pytz.timezone('Asia/Dacca')
dt_tz = my_tz.localize(dt_tz)
dt_in = dt_tz.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_tz)
print(dt_in)
