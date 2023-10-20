# CasarEncode.py

puttxt=input("please enter your message")
for p in puttxt:   
      if "a" <=p <="z": 
            print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end='')
      elif "A" <= p <= "Z":
              print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end='')
      else:
       
             print(p,end='')
