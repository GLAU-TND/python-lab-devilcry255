class myexception:
	def __init__(self,v):
		self.v=v
	def __str__(self):
		return (self,v)
def Xyz(a,b):
	c=a+b
	if c<150:
		raise myexception("custom exception occured")
	else:
		return c
a=int(input())
b=int(input())
print(Xyz(a,b))
