def valuesort(s):
	f=[]
	k=sorted(s.items(),key=lambda s: s[0])
	for n,m in k:
		f.append(str(m))
	print ' '.join(f)



valuesort({'x': 1, 'y': 2, 'a': 3})
