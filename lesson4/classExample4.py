# coding=utf-8
class Animal:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        return "my name is {0}".format(self.name)

    # string.fomat()

    def run(self):
        print(" I am running")

class Cat(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age

cat1=Cat("Tom",12)
cat1.run()
print(cat1.show_info())

