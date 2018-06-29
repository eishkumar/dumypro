x=[[0,0],[0,0]]
y=[[0,0],[0,0]]
# x = []
# y = []
z=[[0,0],[0,0]]
print('enter the elements of x')
for i in range(len(x)):
	for j in range(len(x[0])):
		x[i][j]=int(input(x[i][j]))
		print('next element')
print('enter the elements of y')
for i in range(len(y)):
	for j in range(len(y[0])):
		print('enter the  element')
		y[i][j]=int(input(y[i][j]))
for i in range(len(x)):
	for  j in range(len(x[0])):
		z[i][j]=x[i][j]+y[i][j]
print('the addition value is')		 	
for r in z:
	print(r)				
 