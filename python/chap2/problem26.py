def even(x):
	return x%2==0
def filter(function,list):
	print [x for x in list if function(x) is True]
print filter(even,range(10))
