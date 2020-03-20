imie=(input("jak masz na imię?: "))

if(imie.upper() =='KUBA'):
    print("Jesteś wyjątkowy!")
elif(imie.upper()[-1]=='A'):
    print("Cześć! Jesteś kobietą")
elif(imie.upper()[-1]!='A'):
    print("Cześć! Jesteś mężczyzną")
