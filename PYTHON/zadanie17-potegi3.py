import math
file=open("przyklad.txt","r")

n=file.readline()
spr=range(1,10000)
odp=0
while len(n)>1:
    n=int(n)
    if math.log(n,3) in spr:
        odp+=1
    n=file.readline()
print(odp)

'''matura 2019 zad 4.1'''
