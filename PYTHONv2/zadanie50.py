import random

for i in range(10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    print("Pierwsza liczba to: ",x)
    print("Druga liczba to: ",y)
    z=int(input("Podaj wartość iloczynu tych liczb: "))

    wynik=x*y
    dobrze=0
    if wynik==z:
        print("Brawo, podałeś dobry wynik")
        dobrze+=1
    else:
        print("Musisz jeszcze poćwiczyć. Poprawy wynik to: ",wynik)

if dobrze<4:
    print("niedostateczny")
elif dobrze==4:
    print("dopuszczający")
elif dobrze==5 or dobrze==6:
    print("dostateczny")
elif dobrze==7 or dobrze==8:
    print("dobry")
elif dobrze==9:
    print("bardzo dobry")
elif dobrze==10:
    print("celujący")
