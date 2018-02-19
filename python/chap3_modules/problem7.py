import string
import re
def makeaslug(x):
	p=string.punctuation
	for n in range(len(p)):
		x=x.replace(p[n],' ')
		x=re.sub('\s+', ' ', x)		
	print x.replace(' ','-').strip('-')


makeaslug("  -   --hello- +    world--   +")
