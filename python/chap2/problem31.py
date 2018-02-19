def parse(file,s,j):
	print [x[:-1].split(s) for x in open(file).readlines() if x[0]!=j]
parse('aa.txt','!','#')
