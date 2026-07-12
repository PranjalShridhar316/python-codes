e = [10,20,30,40,50,]
w=bytes(e)
print("elements can not be modified in array")
for i in w: print(i)

q=bytearray(e)

q[0]=69
q[1]=96
print(" elements can be modified in bytearray  ")
for i in q: print(i)