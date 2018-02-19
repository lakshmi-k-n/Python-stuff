from zipfile

import sys
def zip(x=sys.argv[1],fi=sys.argv[2:]):
	f=ZipFile(fi,'w')
	for n in y:
		f.write(n)
zip()
