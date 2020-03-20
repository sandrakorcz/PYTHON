x=input(">>")

file.open("nazwapliku.txt","a")
file.write(x)

file.close()

file.open("nazwapliku.txt","r")
print(file.read())
file.close()
