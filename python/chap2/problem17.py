import sys

def reverse(a):
	k=[]
	s=open(a).readlines()
	k=(s[::-1])
	print ''.join(k)
a=sys.argv[1]
reverse(a)
