u1=input("Podaj swoje imię: ")
u2=input("Podaj swoje imię: ")
u1a=input("Papier, kamień czy nożyce? ")
u2a=input("Papier, kamień czy nożyce? ")

if u1a==u2a:
    print("Remis!")
elif u1a=="papier":
    if u2a=="nożyczki":
        print(u2,"wygrałeś!")
    elif u2a=="kamień":
        print(u1,"wygrałeś!")
elif u1a=="kamień":
    if u2a=="papier":
        print(u2,"wygrałeś!")
    elif u2a=="nożyce":
        print(u1,"wygrałeś!")
elif u1a=="nożyce":
    if u2a=="papier":
        print(u1,"wygrałeś!")
    elif u2a=="kamień":
        print(u2,"wygrałeś!")
elif u1a or u2a != "papier" or "kamień" or "nożyce":
    print("Podaliście nieprawidłową wartość")

