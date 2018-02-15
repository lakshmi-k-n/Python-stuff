import sys

def reverse(a):
        k=[]
        s=open(a).readlines()
	k=s[:10]
	print "head:\n\n"
	print ' '.join(k)
	k=s[-10::]
	#k=k[::-1]
	print "\n\ntail\n\n"
	print ' '.join(k) 

a=sys.argv[1]
reverse(a)

          
