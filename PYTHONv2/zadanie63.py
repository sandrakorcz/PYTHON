file.open("liczby_przyklad.txt","r")
lst=[]

n=file.readline()
while n:
    n=n[:-1]
    i=1
    x=""
    while i<=len(n):
        x+=n[-i]
        i+=1
    spr=0
    n=int(n)
    x=int(x)
    for i in range(2,n):
        if n%i==0:spr+=1
    for i in range(2,x):
        if x%i==0:spr+=1
    if spr==0: lst.append(n)
    n=file.readline()

print(lst)
file.close()
