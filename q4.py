a=int(input('enter a number'))
def fac(b):
	a=1
	for i in range(b,1,-1):
		a=a*i
		#print(a)
	return a

print(fac(a))		