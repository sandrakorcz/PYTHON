a=input("Podaj nazwę pliku; ")
b=input("A, W czy R?")
a+=".txt"
if b=="a":
    file=open(a,b)
    x=input("Podaj tekst do wpisania; ")
    file.write(x)
elif b=="w":
    file=open(a,b)
    print(file.read())
elif b=="r":
    file=open(a,b)
    x=input("Podaj tekst do wpisania; ")
    file.write(x)
    print(file.read())
else:
    print("Podałeś zły atrybut")


file.close()


'''
r - file.read() .readline() , .readlines()
w - file.write()
a - file.write()
'''
