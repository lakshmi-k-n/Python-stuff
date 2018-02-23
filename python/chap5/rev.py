class reverse(object):
	def __init__(self,n):
		self.n=n
		self.i=len(n)-1
	def __iter__(self):
		return self
	def next(self):
		if self.i>=0:
			i=self.i
			self.i-=1
			return self.n[i]
		else:
			raise StopIteration()

a=[1,2,3,4,5]
s=reverse(a)

while True:
	print s.next()
