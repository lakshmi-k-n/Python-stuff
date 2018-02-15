def triplets(num):
	print [(x,y,z) for x in range(1,num) for y in range(x,num) for z in range(y,num) if x+y==z]
print triplets(5)
