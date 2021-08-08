import datetime

# t = datetime.time(23,45,45)
# print(t.microsecond)
dt = datetime.datetime(2021,7,23,23,34,12,50)
td = datetime.timedelta(hours=7,days=7,minutes=28)
print(dt+td)

t_tday = datetime.datetime.today()
t_tnow = datetime.datetime.now()
t_tday = datetime.datetime.utcnow()
print(t_tday)
print(t_tnow)
print(t_tday)
