# coding=utf-8
import re
emailTemplate=r'\w+@cstcollege\.ca'
staffEmail='eric@cstcollege.ca'
result=re.match(emailTemplate,staffEmail)
type(result)
print(result)