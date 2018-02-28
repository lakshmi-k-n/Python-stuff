def treemap(f,lis):
	l=[]
	for i in range(len(lis)):
		#print lis[i]
		if isinstance(lis[i],list):
		#	print lis[i]," list"
			treemap(f,lis[i])
		else:
			lis[i]=f(lis[i])
			
	return lis

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
			
	
