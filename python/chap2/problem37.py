def invert(s):
	items=s.items()
	lis={}
	i=0
	while i<len(items):
		lis[items[i][1]]=items[i][0]
		i=i+1
	
	return lis


inn=invert({'x': 1, 'y': 2, 'z': 3})
print inn
