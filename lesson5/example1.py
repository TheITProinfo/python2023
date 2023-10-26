# coding=utf-8
i=input("please enter number:  ")
n=8999
try:
    result=n/int(i)
    print(result)
    print("the number {0} devide number {1} is {2}".format(n,i,result) )
except ZeroDivisionError as e:
    print("devide by zero: error code:{}".format(e))


