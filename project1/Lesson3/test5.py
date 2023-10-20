# coding=UTF-8
myscore=int(input("please neter your score:0-100 "))

if myscore>=90:
    grade='A'
elif myscore>=80:
    grade='B'
elif myscore>=70:
    grade="C"
elif myscore>=60:
    grade='D'
else:
     grade='F'

print("your grade is - {}".format(grade))