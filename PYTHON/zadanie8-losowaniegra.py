import random
print("Witaj w grze! Wylosowałem liczbę w skali od 1 do 100. Zgadnij ją!")
los=random.randint(1,100)
wybor=int(input("Podaj swoja liczbę"))
proba=1

while wybor!=los:
    if wybor>los:
        print("Przesadziłeś trochę")
    else:
        print("Trochę za mało")
    wybor=int(input("Podaj swoja liczbę"))
    proba+=1
    
print("Odgadłeś! Moja liczba to: ",los)
print("Twoja liczba prób to: ",proba)
