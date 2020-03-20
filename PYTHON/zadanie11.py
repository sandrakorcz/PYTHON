import random

for i in range(10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    print("Pierwsza liczba: ",x)
    print("Druga liczba: ",y)
    z=int(input("Podaj wartość iloczynu tych liczb: "))
    wynik=x*y
    while z!=wynik:
        z=(int(input("Podaj jeszcze raz: ")))
    print("Brawo ty!")
