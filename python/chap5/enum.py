def my_enumerate(lis):
    n = 0

    for i in lis:
        yield (n,i)
        n+= 1

enum = my_enumerate([1,2,3,4,5])

for a ,b in enum:
	print(a,b)
