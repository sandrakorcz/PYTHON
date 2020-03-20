file.open("nazwapliku.txt","r")
line=file.readlines()

while line:
    print(line)
    line=file.readline()

file.close()
