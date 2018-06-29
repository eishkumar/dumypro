def add(c,d):
	print(c+d)
	#return main() pmo@digitallynctech.com
def sub(c,d):
	print(c-d)
	#return main()
def mul(c,d):
	print(c*d)
	#return main()
def div(c,d):
	print(c/d)
	#return main()
def and_(c,d):
	print(c&d)
	#return main()	
def or_(c,d):
	print(c|d)
	#return main()
def btand(c,d):
	print(c and d)
def btor(c,d):
	print(c and d)	
#def not_(c,d):
#	print(!c)
#	return main()						
while 1:
	def main():
		print('1.arithematic operation')
		print('2.logical operation')
		print('3.main menu')
		print('4.exit')
		print('5.bitwise operation')
		#return'a'
	main()
	a=int(input('choose any operation'))	
	if a==1:
		print('1.addition')
		print('2.subtraction')
		print('3.multiplication')
		print('4.division')
		b=int(input('choose the operator to be performed'))
		if b==1:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			add(c,d)
		elif b==2:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			sub(c,d)
		elif b==3:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			mul(c,d)
		elif b==4:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			div(c,d)			
	elif a==2:
		print('1.AND operation')
		print('2.or operation ')
		print('3.Not operation')
		b=int(input('choose the num'))
		if b==1:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			and_(c,d)
		elif b==2:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
			or_(c,d)
		'''elif b==3:
			c=int(input('enter the first value '))
			d=int(input('enter the second value'))
		not_(c,d) '''

	elif a==3:
		main()
	elif a==4:
		break
	elif a==5:
		print('1.and operation')
		print('2.or operation')
		b=int(input('choose any num'))
		if b==1:
			c=int(input('enter first value'))
			d=int(input('enter the second value'))	
			btand(c,d)
		elif b==2:
			c=int(input('enter first value'))
			d=int(input('enter the second value'))
			btor()		
	#elif a==(5,6,7,8):	
	#	print('wrong choice')
	#	main()
