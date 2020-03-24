import random
a=random.randint(0,10)
proby=0
b=0

while b != a and b != "exit":
    b=input("Spróbuj odgadnąć wylosowaną liczbę z przedziału 1-9 lub wpisz 'exit' aby zakończyć grę: ")
    if b == "exit":
        break
    b=int(b)
    proby+=1
    if b<a:
        print("Podałeś za małą liczbę!")
    elif b>a:
        print("Podałeś za dużą liczbę!")
    else:
        print("Udało ci się!")
        print("Musiałeś próbować aż",proby,"razy!")
