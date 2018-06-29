a={1,'hell',(45,20,56),65+9j}
print(a)
print(type(a))
a.update([1,2,3,4])
a.add(56)
print(a)
a={i for i in range(0,10,2)}
print(a)
b={i for i in range(1,10,2)}
print(b)
print(a.difference(b))
print(a.symmetric_differece(b))
a.pop()
a.clear()
print(a|b)
print(a&b)
'''a={i for i in range(0,10,2)}
b={i for i in range(1,10,2)}
