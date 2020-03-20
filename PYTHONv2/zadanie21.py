def sprawdzenie(a,b,c):
    if a>b and a>c:
        print(a, "jest największa liczbą")
    elif b>a and b>c:
        print(b, "jest największą liczbą")
    elif c>a and c>b:
        print(c, "jest największą liczbą")


x=int(input("Podaj liczbę a: "))
y=int(input("Podaj liczbę b: "))
z=int(input("Podaj liczbę c: "))

spradzenie(x,y,z)
