import os

def linesnum(s):
	lenn=0
	for path,dirr,filee in os.walk(os.getcwd()):
		for i in filee:
			if s in i:
				print os.path.join(path,i)," : ",len(open(i).readlines())
				lenn+=len(open(i).readlines())

linesnum(".py")
