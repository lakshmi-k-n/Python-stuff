def unflatten_dict(a, result=None):
    if result is None:
        result = {}
    new={}
    for n in a:
        y=a[n]
        if '.' in n:
	    l=n.split('.')
	    i=0
	    while i<len(l):
		new[l[i+1]]=y
		result[l[i]]=new
		i+=2
        else:
           result[n]=y
    return result


print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
	
