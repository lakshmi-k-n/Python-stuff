import os
import re

dirfiles = os.listdir('/')

print('enter input:')
userReg = str(input())
stringRegex = re.compile(userReg)
fileRegex = re.compile(r'\w+\.txt')

for i in range(len(dirfiles)):
    if fileRegex.search(dirfiles[i]):
        openFile = open('/' + dirfiles[i])
        readFile = openFile.readlines()
        for line in range(len(readFile)):
            r = 0
            if stringRegex.search(readFile[r]):
                print(readFile[r])
                r = r + 1

