import re

def stripp(string):
    global stringg
    bspace = re.compile(r'\s*$')
    
    stringg = bspace.sub('', string)
    fspace = re.compile(r'^\s*')
    stringg = fspace.sub('', stringg)
    return stringg

stripp('    here is the string    ')
print(stringg)
