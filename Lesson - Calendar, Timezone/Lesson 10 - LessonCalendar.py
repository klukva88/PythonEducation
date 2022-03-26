import calendar
from calendar import TextCalendar, HTMLCalendar
# from calendar import *

someCal =  TextCalendar(calendar.MONDAY)
myYearMonth = someCal.formatmonth(2025,2)

someCal2 = TextCalendar(calendar.MONDAY).formatmonth(2000,2)

print(myYearMonth)
print(someCal2)

myHtmlCalendar = HTMLCalendar(calendar.MONDAY)
hCalendar = myHtmlCalendar.formatmonth(2022,3)
print(hCalendar)

for date in someCal.itermonthdays(2021,2):
    print(date)


for month in calendar.month_name:
    print(month)

listMonth = [month for month in calendar.month_name]
print(listMonth)
#listMonth.pop(0)
del listMonth[0]
print(listMonth)

for day in calendar.day_name:
    print(day)

weekDayList = [day for day in calendar.day_name]
print(weekDayList)

