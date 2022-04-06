# Создание файла
myFile = open('info.txt','w')
myFile.close()

# myFile2 = open('info2.txt','r')
# myFile2.close()

# myFile2 = open('/Users/almazuulu/PycharmProjects/PythonLessonEvening/Lesson14_Modules/info2.txt','w')
# myFile2.close()

try:
    myFile3 = open('info2.txt','r')

    try:
        print('code....')
    except:
        print('Ошибка')

    finally:
        myFile3.close()

except FileNotFoundError:
    print('Мы не смогли найти файл!')


with open('info3.txt','w') as file3:
    print('Файл записан успешно!')

try:
    with open('info2.txt','r') as file2:
        print('код...')
except:
    print('Файл не найден!')

#Создание файла с записью

with open('infoUser', 'w') as fileUser:
    fileUser.write('Илья на данный момент изучает Python\nОн хочет устроится на новую работу ')


textUser = """
Меня зовут Олег, мне 32 года
Я проживаю в Бишкеке. В следующем  году
хочу поехать в Алмату
"""

#secondText = input('Введите второй текст: ')
childText = input(' Введите третий текст: ')
# with open('infoUser2','w') as fileUser2:
#     fileUser2.write(textUser + '\n' + secondText)

# Дозапись в существующий текст/информации
with open('infoUser2','a') as fileUser2:
    fileUser2.write(f'\n{childText}')

# Чтение текстового файла
#read()
with open('someText.txt', 'r') as file:
    textFromFile = file.read()

print(textFromFile)
#readline()
print('*'*10)
with open('someText.txt', 'r') as file3:
    line = file3.readline()

    while line:
        print(line, end=" ")
        line = file3.readline()

print('*' * 10)

with open('someText.txt', 'r') as file3:
    for i in file3:
        print(i, end=" ")


#readlines

with open('someText.txt', 'r') as file4:
    linesText = file4.readlines()
print('\n')
print(linesText[:3])

for i in linesText[:3]:
    print(i, end=" ")

print('\n')
for i in linesText[3:]:
    print(i, end=" ")








