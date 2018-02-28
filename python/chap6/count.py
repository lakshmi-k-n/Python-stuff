def count_change(num,ways):
	if num == 0: 
		return 1
	if num < 0 or len(ways) == 0:
		return 0
	w=ways[0]
	return count_change(num,ways[1:]) + count_change(num-w,ways)


print count_change(50,[1,2,5])
