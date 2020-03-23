a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
c=int(input("Podaj liczbę: "))
'''for i in a:
    if i<5:
        print(i)'''

'''for i in a:
    if i<5:
        b.append(i)
print(b)'''


for i in a:
    if i<c:
        b.append(i)
print(b)
