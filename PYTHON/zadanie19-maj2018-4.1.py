file=open("sygnaly.txt","r")
odp=""

for i in range(1,40):
    file.readline()

n=file.readline()

while n:
    print(n)
    odp+=n[9]

    for i in range(1,40):
        file.readline()
    n=file.readline()

print(odp)


