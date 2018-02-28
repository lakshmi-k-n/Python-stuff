def vectorize(f):
	def g(x):
		return list(map(f,x))
	return g

def square(n): return n*n	

fun=vectorize(square)
res=fun([1,2,3,4])
print res
	
