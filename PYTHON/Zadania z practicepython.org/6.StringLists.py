x=input("Wpisz słowo: ")
x=str(x)
y=x[::-1]
if x==y:
    print("Jest to palindrom")
else:
    print("To słowo nie jest palindromem")
