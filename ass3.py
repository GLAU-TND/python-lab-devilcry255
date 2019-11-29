try:
	n=int(input())
	b=int(input())
	a=input()
	c=n+b
	l=a+b
	n.append(3)
except ValueError:
	raise ValueError("here value error occured")
except TypeError:
	raise TypeError("here value error occured")
except:
	raise AttributeError("here Attribute Error occured")
