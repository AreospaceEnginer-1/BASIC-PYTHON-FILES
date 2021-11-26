a_str,b_str = input ('Start from ... '),input ('...End at ')
print ("Values from " + a_str + " to " + b_str)
a_int = int(a_str)
b_int = int(b_str)
while a_int <= b_int:
    print (a_str)
    a_int = a_int + 1
    a_str = str(a_int)
    b_str = str(b_int)
 
