class Dog:
    # define construction method
    def __init__(self,name,age,gender="male"):
        self.name=name
        self.__age=age
    ## define insttance method
    def run(self):
        print(" this dog {} is running".format(self.name))

    ## define get and set method
    def get_age(self):

        return self.__age
    def set_age(self,age):
        self.__age=age  
dog1= Dog('Sucy',10)
print("the dog age is {0}".format(dog1.get_age()))

dog1.set_age(20)
print("the dog age is {0}".format(dog1.get_age()))
