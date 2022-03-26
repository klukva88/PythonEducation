import pytz
from datetime import *

now  = datetime.now()
print(now)

timeUsa = datetime.now(pytz.timezone('US/Central'))
timeUsa2 = datetime.now(pytz.timezone('US/Eastern'))
timeCanada = datetime.now(pytz.timezone('Canada/Mountain'))

print(timeUsa)
print(timeUsa2)

for tz in pytz.all_timezones:
    print(tz)

print(timeUsa2)
print(timeCanada)

for tzCountry in pytz.country_timezones['US']:
    print(tzCountry)

print(timeCanada.strftime('%B/%d/%y - %I:%M'))
print(now.strftime('%B/%d/%y - %I:%M'))
