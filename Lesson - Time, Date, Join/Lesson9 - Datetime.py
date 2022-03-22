#Lesson - Datetime
import datetime
from datetime import date, datetime, time, timedelta
#from datetime import *

#dateConstitution = datetime.date(1991,8,31)
dateConstitution = date(1991,8,31)
print(dateConstitution)

todayDay = date.today()
print(todayDay)

print(f'Сегодняшний день: {todayDay.day}\nСегодняшний месяц: '
      f'{todayDay.month}\nТекущий год: {todayDay.year}')

somedatetime = datetime(2021,4,11,3,30,43,43)
print(somedatetime)

print(f'день: {somedatetime.day}\nмесяц: '
      f'{somedatetime.month}\nгод: {somedatetime.year}, час: {somedatetime.second}')


todayDayTime = datetime.now()
print(todayDayTime)

print(todayDayTime.date())
print(todayDayTime.time())

someTime = time(4,30,45)
print(someTime)

userDate = input('Input the date and time you purchased car d/m/yyyy s:m:h :')
datetimeUser = datetime.strptime(userDate,'%d/%m/%Y %S:%M:%H')
print(datetimeUser)

todayNow = datetime.now()
print(todayNow.strftime('%d/%m/%Y(%H:%M:%S)'))
print(todayNow.strftime('%d/%B/%Y - %A - (%H:%M:%S)'))
print(todayNow.strftime('%d/%b/%Y - %a - (%H:%M:%S:%f)'))


deadline = datetime(2022,5,8,0,0,0)
print(deadline)
print(f'Until deadline you left: {deadline - todayNow}')

birthChild = todayNow + timedelta(270)
print(birthChild)


ninemonth = timedelta(270)
year = timedelta(365)
birthChildandMonth = todayNow + ninemonth
print(birthChild)

theDayAfterTomorrow = todayNow + timedelta(days=2) + timedelta(hours=5) + timedelta(minutes=30)
print(theDayAfterTomorrow.strftime('%d/%B/%y %H:%M'))


#todayNow = datetime(2022,5,10)
todayNow = datetime.now()
if todayNow > deadline:
    deadlineMissed = todayNow - deadline
    print(f'Sorry you missed deadline: {deadlineMissed}')

else:
    deadlineLeft = deadline - todayNow
    print(f'You have some time, dont worry {deadlineLeft}')

#d/m/yy - h:m - Aizhan
#текст и отдельный список
#[I, want, to, go, to Europe, and, work, there] - join() - Ermek
#dateSome = datetime(2025,10,5,23,15) - weekday - d/m/yyyy - 12 hours/ min/ sec - Tilek
# Необходимо выяснить дату от сегодняшнего дня через неделю и 2 часа - Есбол
# # Необходимо выяснить дату до сегодняшнего дня за 10 дней - Динара
