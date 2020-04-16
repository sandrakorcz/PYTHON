file=open("sygnalytxt","r")
odp=[]
linia=file.readline()

while linia:
    linia=linia[:-1]
    litera=0
    for i in linia:
        poprawna_litera=0
        for j in linia:
            if -10<ord(i)-ord(j)<10:
                poprawna_litera+=1
        if poprawna_litera==len(linia):
            litera+=1
    if litera==len(linia):
        odp.append(linia)

    linia=file.readline()

print(odp)
                
