def treemap(lis):
	lis=lis[::-1]
        for i in range(len(lis)):
                #print lis[i]
                if isinstance(lis[i],list):
                #       print lis[i]," list"
                        #lis=lis[i][::-1]
			lis[i]=treemap(lis[i])
	return lis

print treemap([1, 2, [3, 4, [5]]])


