def func(f):
        def g(filenames):
            printlines(out for line in readlines(filenames)
                               for out in f(line))
        return g

	@func
	def wrap(line):
		while(len(line)>int(40)):
        		yield line[:40]+"\n"+line[40:]
			line=line[40:]
		yield line 
