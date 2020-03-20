file.open("nazwapliku.txt","r")

lines=file.readlines(50)

for i in lines:
    print(i)

file.close()
