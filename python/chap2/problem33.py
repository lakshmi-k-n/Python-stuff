def mutate(w):
    llist = []

    l = 'abcdefghijklmnopqrstuvwxyz'
    #insert a character
    for i in range(len(w) + 1):
        for j in range(26):
            llist.append(w[:i] + l[j] + w[i:])

    #deleting a character
    for i in range(len(w)):
        llist.append(w[:i] + w[i + 1:])

    #replace a character
    for i in range(len(w)):
        for j in range(26):
           llist.append(w[:i] + l[j] + w[i + 1:])

    #swapping a characters
    current = []
    out_word = ''
    for i in range(len(w) - 1):
        for j in range(i + 1, len(w)):
            current = []
            for symbol in w:
                current.append(symbol)
            current[i], current[j] = current[j], current[i]
            for symbol in current:
                out_word += symbol
            llist.append(out_word)
            out_word = ''

    return llist

def nearly_equal(w,ww):
	
	mut=mutate(w)
	if ww in mut:
		print "nearly equal"
	else:
		print "not nearly equal"
	


nearly_equal("hello","kkello") 
#print mut
