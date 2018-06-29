a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
pos=int(input('enter pos'))
for i in range(0,3):
	for j in range(0,3):
		if a[i][j]==pos:
			a[i][j]=pos
			pos=x 	
			print(pos)
			break
for i in range(0,3):
	for j in range(0,3):
		print(a[i][j])
