import calendar
from datetime import datetime
from time import strptime
import pytz
from pytz import timezone, all_timezones
from calendar import TextCalendar, Calendar, HTMLCalendar
''' Задача 1
Примите от пользователя год и число месяца и в зависимости от
этого составьте календарь.
Начало дня недели в месяце установите «Вторник»
'''

month = int(input('введите число месяца: '))
year = int(input('введите год: '))
myCalendar = calendar.TextCalendar(calendar.TUESDAY)
formatterCalendar = myCalendar.formatmonth(year, month)
print(formatterCalendar)

'''Задача 2
Сгенерируйте список дней принятое от пользователя в задании No1,
где в качестве дня недели установлен Вторник'''

for day in myCalendar.itermonthdays(year, month):
    print(day)

'''Задача 3
Сгенерируйте HTML код принятое от пользователя в задании No1,
где в качестве дня недели установлен Вторник'''

myCalendar2 = calendar.HTMLCalendar(calendar.TUESDAY)
htmlCalendar = myCalendar2.formatmonth(year, month)
print(htmlCalendar)

'''Задача 4
Примите от пользователя любую дату и время и сконвертируйте эту
дату и время для следующих временных зон (можно любой город
взять из этих стран):
• Франция
• Япония
• Австралия
• Южная Африка
• Индия'''
# все поддерживаемые часовые пояса
print('Часовые пояса, поддерживаемые модулем pytz: \n', pytz.all_timezones, '\n ')
userDate = input('Введите дату в формате d m yyyy H:M: ').strip()
userDate = strptime(userDate, '%d %m %y %H:%M')
timeFrance = userDate(pytz.timezone('Europe/Paris'))
print(f'Во Франции {timeFrance}')