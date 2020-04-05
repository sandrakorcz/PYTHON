

def duplikaty(x):
    b=[]
    for i in x:
        if i not in b:
            b.append(i)
    return b
a=[1,1,2,4,5,3,6,5,7,6,7,8,4,9,34,23,12,12,34]
print(a)
print(duplikaty(a))
