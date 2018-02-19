import sys
import os
def tree(sys.argv[1],i=0):
	ls=os.listdir(x)
	n=0
	
	print ' '*i,x
	while n<len(ls):
		if '.' in ls[n]:
			print ' '*i,'|','_'*2,ls[n]
		else:
			tree(x+'/'+ls[n],i+2)
		n+=1
tree()
	
