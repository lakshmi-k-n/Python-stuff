import collections
import sys

''' functions to demonstrate collections'''

dict={}
listt=[]
def build_dict():
  file1=sys.argv[1]
  fopen=open(file1)
  for line in fopen:
    for ch in line:
      dict[ch]= dict.get(ch,0) + 1

def build_list():
  fopen=open(sys.argv[1])
  for line in fopen:
    for ch in line:
      listt.append(ch)

def count_show():
  global listt,dict
  c = collections.Counter(listt)
  d = collections.Counter(dict)
  
  print "LIST\n\n",c,"\n\n\n"
  print "DICT\n\n",d,'\ndict\n\n\n'

def most_common():

  '''function for 3 most collon characters in the text file'''

  c = collections.Counter(listt)
  print c.most_common(3)

def elements_gen():
  c = collections.Counter(a=4,b=1,c=4)
  list(c.elements())  

def subtract():
  a = collections.Counter(a=3,b=3,c=2)
  b = collections.Counter(a=2,b=3,c=1)
  a.subtract(b)
  print a

def update_gen():
  a = collections.Counter(a=5,b=9)
  print "original values:",a
  a.update(a=5,c=12)
  print "updated value:",a



build_list()
build_dict()
most_common()
elements_gen()
subtract()
update_gen()
#count_show()
#print dict
