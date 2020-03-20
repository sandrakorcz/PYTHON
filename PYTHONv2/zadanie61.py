class Users:
    num_of_users=0

    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

        Users.num_of_users+=1

    def dane(self):
        return"{} {}".format(self.name,self.pay)


user_1=Users("Adam",0)
user_2=Users("Ola",1000)

print(user_1.dane())
print(user_2.dane())
print(Users.num_of_users)
