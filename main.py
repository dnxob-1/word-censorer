import re

## not the most advanced word censorer. 

listOfBadWords = [] # add profanities 


def userIn():
    strInput = str(input("Enter sentence: "))
    return strInput.lower()


def wordCensorer():
    getInput = userIn() 
    getInput = re.findall(r'[A-Za-z]+|\d+', getInput)

    for i in getInput:
        for x in listOfBadWords:
            if i == x:
                lengthOfCensoring = "#" * len(x)
                i = i.replace(i, lengthOfCensoring)
        print(i)

wordCensorer()
