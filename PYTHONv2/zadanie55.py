list=['a','b','c','d','e']
x=int(input(">>"))
'''
for x, i in enumerate(list):
    print(x,i)
'''
for x, i in enumerate(range(1,x)):
    if i%2==0:
        print(x,"parzysta")
    else:
        print(x,"nieparzysta")
