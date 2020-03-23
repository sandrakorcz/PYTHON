x=int(input("Podaj liczbę: "))
y=int(input("Podaj liczbę: "))

'''if x%4==0:
    print(x," dzieli się przez 4")
elif x%2==0:
    print(x,"jest liczbą parzystą")
else:
    print(x,"jest liczbą nieparzystą")'''

if y!=0:
    if x%y==0:
        print(x,"dzieli się przez",y)
    else:
        print(x,"nie dzieli się przez",y)
else:
    print("Nie dziel cholero przez 0")
