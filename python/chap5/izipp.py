
def izip(a, b):
    for a1 in a:
        for b1 in b:
            if a.index(a1) == b.index(b1):
                yield a1,b1


a=["a","b","c","d"]
b=[1,2,3,4]
s = izip(a,b)


for a, b in s:
	print(a,b)
