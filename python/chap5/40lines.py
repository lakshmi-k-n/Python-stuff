import sys

def ylinesfiles(files):
	for f in files:
		for line in open(f):
			print line
			yield line

def forlines(lines): 
	return (line for line in lines if len(line)>40)

def printlines(lines): 
	for line in lines:
		print line
def forty():
	lines=ylinesfiles(sys.argv[x] for x in range(1,len(sys.argv)))
	rlines=forlines(lines)
	printlines(rlines)

forty()
	
