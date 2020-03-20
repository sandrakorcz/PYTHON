import random
a=random.sample(range(1,100),5)
cyfra=int(input("Wprowadź cyfrę: "))

if cyfra in a:
    print('Cyfra ",cyfra," znajduje się w tablicy")
else:
    print("Cyfra nie znajduje się w tablicy")
