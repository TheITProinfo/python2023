# coding=utf-8
# example for private varable
class MyAccount:
    __interest_rate=0.0568 

    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount 

    def description(self):
        print("the account owner {0} amount{1}, interest {2}".format(self.owner,self.__amount,self._interest_rate))


account2=MyAccount("Tony",900.0)

print("account holder:{0}".format(account2.owner))

print("account amount {0}".format(account2.__amount))




