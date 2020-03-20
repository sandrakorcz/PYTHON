wynik=0
a=1

while a<4:
  x=int(input("Podaj liczbę parzystą dodatnią: "))
  if x%2==0 and x>0:
    wynik+=x
  else:
    print("Podałeś złą liczbę")
    continue
  print("Aktualny wynik dodawania to: ",wynik)
  a+=1
