from datetime import date, datetime, time, timedelta
from time import strptime, strftime

'''Задача 1
Примите от пользователя какой-нибудь текст о нем. Пусть он/она распишет
свою биографию вкратце.
• Затем вам надо будет весь принятый текст от пользователя записать в
список, где каждое слово представлено как отдельный
элемент списка.
• Отобразите первые 3 слова с этого списка
• Отобразите последние 5 слов из этого списка
• Составьте какой-нибудь текст из этого списка объединив при этом
первые 5 слов с последними 2мя словами
'''

userText = input('Введите текст: ')
textToList = userText.split()  # Запист текста в список
print(textToList[0:3])  # Первые 3 слова из списка
print(textToList[-5:])  # Последние 4 слов из списка
someText = " ".join(textToList[0:5]) + " " + " ".join(textToList[-2:])  # Текст из первых 5 и последних 3-х слов списка
print(someText)

'''Задача 2
Есть данный текст «Бишкек@Самый@лучший@город@в@мире»
Необходимо убрать знак «@» в этом тексте и составить новый текст уже без
этого знака'''

initialText = 'Бишкек@Самый@лучший@город@в@мире'
initialText = initialText.split("@")
initialText = " ".join(initialText)
print(initialText)

'''Задача 3
Как написать текущее время? Напишите пожалуйста'''
currentTime = datetime.now()
print(currentTime.strftime('%X'))

'''Задча 4
Примите от пользователя дату в следующем формате d-m/yyy-(H:M:S)
Создайте на основе принятого от пользователя времени новую дату'''

userDate = input('Введите дату в формате d-m/yy-(H:M:S): ').strip()
userDate = strptime(userDate, '%d-%m/%y-(%H:%M:%S)')  # Парсинг строки юзера
userDate = datetime(userDate.tm_year, userDate.tm_mon, userDate.tm_mday, userDate.tm_hour, userDate.tm_min,
                    userDate.tm_sec)  # вот здесь не очень понял, как сделать по другому, например сразу через strftime()
print(f' The Date is {userDate.strftime("%c")}')
# '%d/%m/%Y(%H:%M:%S)' 10-02/22-(23:13:00)

'''Задача 5
Созданную дату из задания №4 переделайте в следующий формате
«день-название месяца полностью-(день недели)-год с двумя цифрами - Часы:
Минута»'''

print(f'{userDate.strftime("%d-%B-(%A)-%y-%I:%M")}')

'''Задача 6
Выясните какое будет время спустя:
• 2 месяца от текущей даты?
• через 2 Года?
• Через год и 2 дня?
• Через 3 месяца и 3 дня?
И отобразите эти значения на экране'''

currentDate = datetime.now()
afterTwoMonth = currentDate + timedelta(weeks=8)
afterTwoYears = currentDate + timedelta(days=730)
afterOneYearTwoDays = currentDate + timedelta(days=367)
afterTreeMonthThreeDays = currentDate + timedelta(weeks=12) + timedelta(days=3)

print(f' Время через 2 месяца от текущей даты - {afterTwoMonth.strftime("%d-%B %I:%M")}')
print(f' Время через 2 года от текущей даты - {afterTwoYears.strftime("%d-%B %I:%M")}')
print(f' Время через 1 год и 2 дня от текущей даты - {afterOneYearTwoDays.strftime("%d-%B %I:%M")}')
print(f' Время через 3 месяца и 3 дня от текущей даты - {afterTreeMonthThreeDays.strftime("%d-%B %I:%M")}')
