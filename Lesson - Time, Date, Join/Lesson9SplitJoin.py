 # метод split()- раздаеление слова или текста определенным разделителем на
 # отдельный элемент списка

text = 'I love programming'
text2 = 'I,love,programming, swimming, reading, and, drawing'
text3 = 'I love programming. Thats why I learn Python. I started my course in 22th Feb'
someList = list(text)
print(someList)

splittedText = text.split(' ')
print(splittedText)

splittedText2 = text2.split(',')
print(splittedText2)

splittedText3 = text3.split('.')
print(splittedText3)

word = 'H?el?lo'
wordSplitter = word.split('?')
print(wordSplitter)


someListtext = ['I', 'love', 'programming', ' swimming', ' reading', ' and', ' drawing']
sometext = someListtext[0] + someListtext[1] + someListtext[2]
semeListtext2 = text2.split(',',4)


 # метод join()- соединение слов или текста определенным разделителем на

sometext2 = " ".join(someListtext)
print(sometext2)

sometext2 = ",".join(someListtext)
print(sometext2)

#sometext3 = " ".join(someListtext, 3)
print(semeListtext2)

listProglang = ['Python', 'Java', 'C#', 'JavaScript', 'PHP']
myskills  = 'I have some skills in those programming languages: ' + ', '.join(listProglang)

print(myskills)

word = 'Programming Language'
wordList = word.split(' ')
wordFormated = '/'.join(wordList)
joinedWord = '/'.join(word)

print(joinedWord)
print(wordFormated)





