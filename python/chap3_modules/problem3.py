import os
import time
import stat
def listfiles(dir):
        f=[]
        for dirr,dnames,fnames in os.walk(dir):
                #f=f+os.path.join(dirr, fnames)
                #print os.path.join(dirr, fnames)
               # dirr=dirr.strip("/")
                for name in fnames:
                        p=os.stat(os.path.join(dirr, name))
			print os.path.join(dirr, name),'\n',time.ctime(p.st_mtime),'\t',p.st_size,' bytes'
        #print '\n'.join(f)     

listfiles("/home/lakshmi/projects/python")

