# coding=utf-8
class Dog:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
# create object

dog1=Dog('Mike',10,20,35)
print("this dog name is {}, age is {}, wight is {} height is {}".format(dog1.name,dog1.age,dog1.weight,dog1.height))
 