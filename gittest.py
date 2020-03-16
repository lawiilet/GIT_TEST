from datetime import datetime, date, time

dt = datetime(2020, 3, 16, 18, 44, 30)
print(type(dt))

print(dt.day)
print(dt.minute)

print(dt.date())
print(dt.time())

print(dt.strftime('%y%m%d %H:%M'))
print(dt.strptime('20200316 20:17:01', '%Y%m%d %H:%M:%S'))
print(type(dt.strptime('20200316', '%Y%m%d')))