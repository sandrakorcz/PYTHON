file=open("sygnaly.txt","r")
max_dl=0
odp=""
linia=file.readline()

while linia:
    linia=linia[:-1]
    spr=[]
    dl=0
    for i in linia:
        if i not in spr:
            dl+=1

    if max_dl<dl:
        max_dl=dl
        odp=linia

    linia=file.readline()

print("Wyraz:",odp)
pritn("Ilość różnych liter:",max_dl)
