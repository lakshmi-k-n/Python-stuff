def group(l,s):
	new=[]
	new1=[]
	for i in range(0,len(l),s):
		new1= l[i:i+s]
		new.append(new1)
	print new
