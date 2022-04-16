#Task1
def copyingFiles(filename, filename2):
    with open('filename.txt', 'r') as file:
        myText=file.read()
    with open('filename2.txt', 'w') as file1:
        file1.write(f'{myText}')

#Task3
def findMinimumWord(filename):

    with open(filename) as file:
        text = file.read()

    words = text.split()
    minLen = len(words[0])
    for word in words:
        if len(word) < minLen:
            minLen = len(word)

    #print(minLen)
    smallestWords = []
    for word in words:
        if len(word) == minLen:
            smallestWords.append(word)

    print(f'Самое мальнько по длине слово: {smallestWords}')

#Task6
def showingDataCoord(filename):
    pass

def main():
    textFile = 'mytext.txt'
    textFile2 = 'mytext2.txt'
    excelFile = 'food.xlsx'

    copyingFiles(textFile, textFile2)
    findMinimumWord(textFile)
    showingDataCoord(excelFile)


if __name__ == '__main__':
    main()