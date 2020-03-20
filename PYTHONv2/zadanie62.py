file=open("liczby_przyklad.txt"),"r")
lst=[]
n=file.readline()
while n:
    spr=0
    n=int(n)
    if 100<=n<=5000:
        for i in range(2,n):
            if n%1==0: spr+=1

        if spr==0: lst.append(n)
    n=file.readline()

print(lst)
file.close()
