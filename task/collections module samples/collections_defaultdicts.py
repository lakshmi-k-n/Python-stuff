import collections


s = [('a',10),('b',1),('c',2),('a',3)]
d= collections.defaultdict(list)
for n,m in s:
  d[n].append(m)
print d.items()



