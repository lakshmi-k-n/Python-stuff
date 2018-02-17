import sys
def wrap(num):
        s=open(sys.argv[1]).readlines()
        for x in s:
                for n in range(0,len(x),int(num)):
                        print (''.join(x[n:n+int(num)])).rstrip('\n')

	sys.stdout.write(' ')

wrap(sys.argv[2])
sys.stdout.flush()
