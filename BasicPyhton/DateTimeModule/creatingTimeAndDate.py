import datetime

'''There are two types of date:
                            1.Naive Date[Doesn't have enough information]
                            2.Aware Date[Contains enough information about the date]'''
tm = datetime.time(20,12,12,12)
print(tm)
# print(tm.second)
cday = datetime.date(2021,1,3)
print(cday)
# print(tday.day)
'''weekday() Monday 1 Sunday 6'''
print(cday.weekday())
'''isoweekday() Monday 0 Sunday 1'''
print(cday.isoweekday())

# tday = datetime.datetime.today()
tday = datetime.date.today()
print(tday)
