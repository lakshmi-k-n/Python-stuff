import os
import re

def listfiles(dir):
        f=[]
	ret=[]
        for dirr,dnames,fnames in os.walk(dir):
                #f=f+os.path.join(dirr, fnames)
                #print os.path.join(dirr, fnames)
                dirr=dirr.strip("/")
                for name in fnames:
			ret.append(os.path.join(dirr, name))
                        #print os.path.join(dirr, name)
	return ret
def freq():
	lis=listfiles("/home/lakshmi/projects/python")

	f={}
	s=[]
	for n in lis:
		file,ext=os.path.splitext(n)
		print file,ext
		f[ext]=f.get(ext,0)+1

	for key,value in f.iteritems():
		print key,'\t',value
	


freq()  
