import datetime
from datetime import date, datetime, time, timedelta
'''
Принять текст от пользователя и сделать из него отдельный список
'''

userText = input('Введите текст: ')

newList = userText.split() #разбивает принятый текс через какждый пробел, () - дефолтный пробел
print(newList)

nowDate = datetime.now()
theDate = timedelta(weeks=1, hours=2)
print(nowDate + theDate)