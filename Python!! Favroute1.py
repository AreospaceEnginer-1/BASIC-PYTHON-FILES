class Signed_Families(object):
        def __init__(self,name,password):
                self.name = name
                self.password = password   
        def __del__(self):
                Che = input("Are you Sure? Y For Yes, N for No")
                if Che == 'Y':
                        print('-'*50)




















import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ('matchObj.group() : ', matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")



input()
