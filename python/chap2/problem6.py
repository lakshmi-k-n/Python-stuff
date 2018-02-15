def rever(s):
	median = len(s)//2
	length = len(s)
	for index in range(median):
		temp = s[index]
		s[index] = s[(length - 1) - index]
		s[(length - 1) - index] = temp
	print s
		
rever(input())

