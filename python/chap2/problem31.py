def parse(filename,i,j):
	print [x[:-1].split('!') for x in open(filename).readlines() if x[0]!='#']
parse('a.txt','!','#')
