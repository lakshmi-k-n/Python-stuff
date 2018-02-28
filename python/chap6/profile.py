import datetime

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
	lis=[]
	ip=[]
	def g(x):
		ip.append(x)
#
		lis.append(datetime.datetime.now())
		n=f(x)
		lis.append(datetime.datetime.now())
		if x==ip[0]:
			print "time taken:- ",max(lis)-min(lis)
		return n
	return g


fi=profile(fib)
fb=fi(20)
print fb
