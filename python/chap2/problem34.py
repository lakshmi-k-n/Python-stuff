def decsort(x):
    f={}
    words=open(x).read().split()
    for w in words:
	f[w]=f.get(w,0)+1
    s=f.items()
    s.sort(key=lambda x:x[1])
    for n in s:
	print n[0],n[1]
decsort('she.txt')
