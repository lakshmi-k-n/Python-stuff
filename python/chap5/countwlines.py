import os

def linesnum(x):
        l=0
        for path,dirr,files in os.walk(os.getcwd()):
                for a in files:
                        if x in a:
				n=0
				for b in open(a):
					if b[0] not in ['#','\n']:
						l+=1
						n+=1
				print os.path.join(path,a),": ",n
  

linesnum(".py")
