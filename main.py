import re

## not the most advanced word censorer. includes profanities. beware.  

listOfBadWords = ["fuck", "shit", "bitch", "slut", "harlot", "nigga", "nigger", "whore", "cunt", "ass", "fucker", "faggot", "cock", "dick", "chink", "hoe", "cuck", "motherfucker", "pussy", "dumbass", "porn", "butthole", "jackass", "moron", "dumbass", "dumb", "fucking", "tittes", "tits", "cocksucker", "retard", "asshole"]


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
