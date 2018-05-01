import sys
import random
import string



def histogram_main(filename,skip=False):
  fp=open(filename)
    if skip==True: 
      skip_header(fp)
  words = word_list(f)
  print words
  return 

def word_list(f):
  str=string.punctuation+string.whitespace
  words=[]
  for line in f:
    line=line.translate(' ','-')
    linel=line.split()
      for w in linel:
        words.append(w.translate(None,str))
  return words





def main():
  histogram_main(sys.argv[1])


if __name__=='__main__':
  main()
