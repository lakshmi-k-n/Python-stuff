import sys
from inspect 
def pydoc(x):
        p=__import__(x)
        print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
        for y in dir(p):
                 print y
pydoc(sys.argv[1])

