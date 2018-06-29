for i in range (1,4):
	for j in range (1,6):
		if(j%2 != 0):
			 print(''.join(map(str, '__')))
		else:
			 print(''.join(map(str, '|')))
'''a=['__','|','__','|','__']
for i in range(0,4):
	#if i==3 and a== '__':
	#	break
	print(''.join(map(str, a[i])))'''
