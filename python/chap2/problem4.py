def product(y):
        a=1
        for x in y:
                a=a*x
        print a

a=raw_input()
b=int(a)

if b==0:
	print 1
else:
	product(range(1,b+1))

