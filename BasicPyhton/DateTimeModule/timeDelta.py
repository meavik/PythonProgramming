import datetime
''''timedelta = date1 + dat2 or date1-date2
    date1+dat2 = timedelta or date1-date2 = timedelta'''
# tday = datetime.datetime.today()
tday = datetime.date.today()
fday = datetime.timedelta(days=7)
print(tday+fday)

''''Counting days to my Birthday'''
mybday = datetime.date(2021,4,27)
print(tday-mybday)
