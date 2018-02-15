def parse_csv(filename):
	print [x[:-1].split(',') for x in open(filename).readlines()]

