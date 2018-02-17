def zip(a,b):
	print [(a[x],b[x])for x in range(min(len(a),len(b))) ]
print zip([1,2,3],['a','b','c'])
