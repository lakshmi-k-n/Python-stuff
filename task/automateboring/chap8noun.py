import re

textFile = open(input('enter name of file.'))
newTextFile = textFile.read()
textFile.close()


words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
while True:
    checkFile = newTextFile
    for i in words:
        if re.compile(i).search(newTextFile) != None:
            change = input('please enter '+ i.lower())
            newTextFile = re.compile(i).sub(change, newTextFile, count=1)
    if checkFile == newTextFile:
        break

print(newTextFile)
newFile = open('newfile.txt', 'w')
newFile.write(newTextFile)
newFile.close()
