import os


def findfiles(x,dir=os.getcwd()):
	for dirr,dnames,fnames in os.walk(dir):
		for name in fnames:
			if name == x:
				print os.path.join(dirr, name)

print os.getcwd()
findfiles("f1")
