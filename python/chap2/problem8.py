def cumulative_sum(a):
	b=[]
	l=len(a)
	for x in range(l):
		b.append(sum(a[:x+1]))
	print b
