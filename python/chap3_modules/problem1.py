import os 

def listfiles(dir):
	f=[]
	for dirr,dnames,fnames in os.walk(dir):
		#f=f+os.path.join(dirr, fnames)
		#print os.path.join(dirr, fnames)
		#dirr=dirr.strip("/")
		for name in fnames:
			print os.path.join(dirr, name)
	#print '\n'.join(f)	

listfiles("/home/lakshmi/projects/python")
