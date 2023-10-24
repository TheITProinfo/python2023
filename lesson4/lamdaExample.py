# coding=utf-8
def calculator(myoperation):
    if myoperation=="+":    
        return lambda a,b:(a+b)
    else:
        return lambda a,b:(a-b)
    

f1=calculator("+")    
f2=calculator("-")
print("100+198={0}".format(f1(100,198)))
print("200-198={0}".format(f2(200,198)))

