print("Wybierz działanie (oznaczone literami)")
print("a.dodawanie")
print("b.odejmowanie")
print("c.mnożenie")
print("d.dzielenie")
x=input("Podaj literę: ")
a=int(input("Podaj 1 liczbę: "))
b=int(input("Podaj 2 liczbę: "))

if x=="a":
    print("Wynik dodawania to:",a+b)
elif x=='b":
    print("Wynik odejmowania to:",a-b)
elif x=="c":
    print("Wynik mnożenia to:",a*b)
elif x=="d":
    if b!=0:
        print("Wynik dzielenia to:",a/b)
    else:
        print("Nie dzieli się przez 0!")
else:
    print("Podano nieprawidłowa literę")
