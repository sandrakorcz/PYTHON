file.open("nazwapliku.txt","r")
a=int(input("Podaj liczbę linijek do wyświetlenia: "))
line=file.readline()
i=0

while i<a:
    print(line)
    line=file,readline()
    i+=1

file.close()
