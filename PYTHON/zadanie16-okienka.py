lekcje=int(input("Podaj ilość lekcji: "))
godziny=input("Podaj godziny  1 i 0 rozdzielając je spacją: ")

if len(godziny.split())==lekcje:
    godziny = godziny.replace("1 0 1","1 1 1").replace("1 0 1","1 1 1").split()
    lst=map(int,godziny)
    print("Liczba godzin, które Kalinka musi spędzić w szkole to: ",sum(lst))
else:
    print("Pomyliłeś się przy wpisywaniu godzin w 1 i 0")
