file.open("nazwapliku.txt","r")
lines=file.readlines()

for i in lines:
    print(i)
file.close()
