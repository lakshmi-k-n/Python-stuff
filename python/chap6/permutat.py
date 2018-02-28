import itertools
def perm(s):
	k=list(itertools.permutations(s))
	for i in range(len(k)):
		k[i]=list(k[i])
	return k

print perm([1,2,3])
