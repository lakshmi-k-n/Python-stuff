def product(y):
        a=1
        for x in y:
                a=a*x
	c=a	
	return c

def cumulative_pro(a):
	b=[]
	l=len(a)
	for x in range(l):
		b.append(product(a[:x+1]))
 	print b
