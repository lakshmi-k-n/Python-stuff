import sys
import random
import string
import bisect


def histogram_main(filename,skip=False):
  fp=open(filename)
  if skip==True: 
    skip_header(fp)
  hist = create_hist(fp)
  print len(hist)
  return hist

def create_hist(fp):
  hist={}
  str=string.punctuation+string.whitespace
  words=[]
  for line in fp:
    line=line.replace("-", " ")
    linel=line.split()
    for w in linel:
      word=w.translate(None,str).lower()
      hist[word] = hist.get(word,0) + 1      
  return hist

def skip_header(fp):
  for line in fp:
    if line.startswith("*END*THE SMALL PRINT!"):
      break

def common(hist):
  sort=sorted(hist,key=lambda x:hist[x],reverse=True)
  print "\nCOMMON WORDS"
  for i in range(20):
    print sort[i]

def compare(words,hist):
  hist=set(hist.keys())
  #print hist
  words=set(words.keys())
  diff=hist.difference(words)
  for i in diff:
    print i,
 # print diff


def cumsum(hist):
  #print hist
  csum=[]
  sum=0
  words=sorted(hist,key=lambda x: hist[x])
  #print words
  for i in sorted(hist,key=lambda x: hist[x]):
    sum=sum+hist[i]
    csum.append(sum)
  return words,csum

def random_words(words,csum): 
    randnum=random.randint(0,csum[-1])
    i = bisect.bisect(csum, randnum)
    return words[i]


def main():
  hist=histogram_main(sys.argv[1],True)
  common(hist)
  print "------\nno of diff words:",len(hist)
  print "total number of words:",sum(hist.values())
  if len(sys.argv) == 3:
    words=[]
    f=open(sys.argv[2])
    words=create_hist(f)
    compare(words,hist)
  print "--------\n10 random words"
  words,csum=cumsum(hist)
  for i in range(10):
    print random_words(words,csum)



if __name__=='__main__':
  main()
