class Users:
    fname="Norman"
    lname="Poorman"
     def Dane(self,fname,lname):
         return("{} {}".format(fname,lname)

user_1=Users()
user_2=Users()
x=user_1.Dane("Anna", "Kowalska")
y=user_2.Dane("Dawid", "Rybka")

print(x)
print(y)
