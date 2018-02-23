import os

def peep(s):
	return s.next(),iter(list(s))
iterr = iter(range(5))
x,iterr1 = peep(iterr)
print x,
print list(iterr)
