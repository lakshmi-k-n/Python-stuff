def array(d1,d2):
	return [[None]*d2 for d1 in range(1,d2)]
a=array(3,4)
a[0][2]=8
print a
