def even(x):
	return x%2==0
def filter(fun,list):
	print [x for x in list if fun(x) is True]
print filter(even,range(10))
