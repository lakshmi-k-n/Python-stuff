import sys
def wrap(ff):
 k = int(sys.argv[2])
 f=open(ff).readlines()
 for i in f:
  new=i
  while len(new)>k:
    print new[:k]
    new=new[k:]
  print new
wrap(sys.argv[1])
