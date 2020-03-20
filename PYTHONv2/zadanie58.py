x=input(">>")
suma=0

l=1
for i in x:
    if i==x[-l]:
        suma+=1
    l+=1

if suma==len(x):
    print("Jest tak samo")
