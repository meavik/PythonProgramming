import  datetime
import pytz

dt_tz = datetime.datetime.now()
dt_ft = dt_tz.strftime('%d %b, %Y')
print(dt_ft)
input_date = '2016-07-25'
get_date = datetime.datetime.strptime(input_date,'%Y-%m-%d')
print(get_date)
print(get_date.strftime('%b %d, %Y'))
