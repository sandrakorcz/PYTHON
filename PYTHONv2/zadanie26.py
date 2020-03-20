import random
a=random.sample(range(1,100),5)
b=random.sample(range(1,50),4)
cyfra=int(input("Wprowadź cyfrę: "))
print(a)
print(b)
if cyfra in a nad b:
    print("Cyfra ",cyfra," znajduje się w 1 i 2 tablicy")
elif cyfra in a:
    print("Cyfra ",cyfra," znajduje się w 1 tablicy")
elif cyfra in b:
    print("Cyfra ",cyfra," znajduje się w 2 tablicy")
else:
    print("Cyfra nie znajduje się w żadnej tablicy")
