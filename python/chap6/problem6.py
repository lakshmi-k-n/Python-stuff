import os
import sys


def tree(n,i=0):
	try:
		ls=os.listdir(n)
		k=0
		print ' '*i,n
		while k<len(ls):
			if '.' in ls[k]:
				print ' '*i,'|', '_'*2,ls[k]
			else:
				tree(n+'/'+ls[k],i+2)
			n=n+1
	except OSError:
		return 


tree(sys.argv[1])
	
