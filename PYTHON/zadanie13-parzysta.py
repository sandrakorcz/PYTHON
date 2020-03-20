a=int(input("Podaj liczbę do sprawdzenia: "))

if a%2==0:
    print(a," jest liczbą parzystą.")
else:
    print(a," nie jest liczbą parzystą.")


b=str(a)


if b[-1]=="0" or b[-1]=="2" or b[-1]=="4" or b[-1]=="6" or b[-1]=="8":
    print(a," jest liczbą parzystą.")
else:
    print(a," nie jest liczbą parzystą.")


while a>1:
    a-=2
    if a==1:
      print(" nie jest liczbą parzystą.")
    elif a==0:
        print("Jest to liczba parzysta.")
