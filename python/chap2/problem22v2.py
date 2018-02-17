import sys

def wordwrap(num):
	#print num
	num=int(num)
	count=0

	s=open(sys.argv[1]).readlines()
	for l in s:
		count=0

		k=l.split(' ')
		#print k
		for w in k:
			#print "w\n",w
			if w.isspace():
				print "whitespace"
				count=len(w)+count
				if count < num:
					print count,"<",num
                               		print w.rstrip('\n')
                       		elif count >= num:
					count=0
					print w.rstrip('\n')
                                	

			else:
				count=len(w)+count+1
				#print count
                                ''.join([w,' '])
				
				if count < num:
					print "count less than"
					print w.rstrip('\n')
				elif count >= num:
					print "count more than or equal"
					count=0
					print w.rstrip('\n')
					


wordwrap(sys.argv[2])
