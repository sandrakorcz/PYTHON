a=int(input("Wpisz liczbę: "))
b=0
for i in range(2,a):
    if a%i==0:
        b+=1
if b==0:
    print("Jest to liczba pierwsza")
else:
    print("Nie jest to liczba pierwsza")
