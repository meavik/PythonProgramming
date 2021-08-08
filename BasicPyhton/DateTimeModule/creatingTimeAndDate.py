import datetime

'''There are two types of date:
                            1.Naive Date[Doesn't have enough information]
                            2.Aware Date[Contains enough information about the date]'''
tm = datetime.time(20,12,12,12)
print(tm)
# print(tm.second)
tday = datetime.date(2021,1,3)
print(tday)
# print(tday.day)
print(tday.weekday())'''weekday() Monday 1 Sunday 6'''
print(tday.isoweekday())'''isoweekday() Monday 0 Sunday 1'''
