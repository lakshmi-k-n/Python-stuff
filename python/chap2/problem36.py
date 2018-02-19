import itertools 
def anagrams(x):
	s={}
	while len(x)>0:
		popp=x.pop()
		s[popp]=s.get(popp,[])
		s[popp].append(popp)
		for n in x:
			per=[''.join(p) for p in itertools.permutations(popp)]
			if n in per:
				x.remove(n)
				s[popp].append(n)
	return s.values()


print anagrams(['souep','eat','node','ate','done','tea'])
