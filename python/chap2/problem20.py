import sys

def grepp(f):
	ff=open(f).readlines()
        for a in ff:
		if sys.argv[2] in a:
			print a

k=sys.argv[1]
grepp(k)
