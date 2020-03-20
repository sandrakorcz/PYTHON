a=[1,1,3,4,5,6,5,3,2]
b=[]
print(a)
for x in a:
    if x not in b:
        b.append(x)
print(b)
