def wprowadzenieliczby(prompt):
    return int(input(prompt))

def czypierwsza(liczba):
    if liczba==1:
        pierwsza=False
    elif liczba==2:
        pierwsza=True
    else:
        pierwsza=True
        for sprawdzenie in range(2,(liczba/2)+1):
               if liczba%sprawdzdenie==0:
                   pierwsza=False
                   break
    return pierwsza

def odpowiedz(liczba):
    pierwsza=czypierwsza(liczba)
    if pierwsza:
        x=""
    else:
        x="nie"
    print(liczba,x,"jest liczbą pierwszą",sep="",end="\n\n")

while 1==1:
    odpowiedz(wprowadzenieliczby("Wprowadż liczbę do sprawdzenia. Ctrl+C aby wyjść: "))

#Coś nie działa nie wiem co#
