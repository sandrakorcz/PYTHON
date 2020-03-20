a=int(input("Wpisz liczbę; "))
b=0
i=2
while i<a:
    if a%i==0:
        b+=1
        i+=1
    if b==0:
        print("Jest to liczba pierwsza")
    else:
        print("Nie jest to liczba pierwsza")
