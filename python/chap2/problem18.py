import sys

def reverse(a):
        k=[]
        s=open(a).readlines()
	for x in s:
			k=x.split(' ')
			t=k[::-1]
			print ' '.join(t)
			
a=sys.argv[1]
reverse(a)

