mydict1={100:"John",101:"Alice",102:"Bob",103:"Joy"}

for studentId in mydict1.keys():
   # print("studentID "+str(studentId))
   print("studentID is {}".format(studentId))

# value

for studentName in mydict1.values():
   print("studnet Name are {}".format(studentName))

## key and value
 
for sudentID,studentName in mydict1.items():
   print("student ID is {}---student Name {}".format(sudentID,studentName))   