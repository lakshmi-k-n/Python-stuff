def square(x):
	return x*x
print square(2)
def map(fun,s):
	print [fun(x) for x in s]
print map(square,[1,2,3])
