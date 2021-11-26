ans = 0
ca,nca, = int (input ('Start adding from ... ')),int (input ('...End adding at '))
un1 = ca
un2 = nca - ca

while ca <= nca:
    ans = ans + ca
    ca = ca + 1
if un2 == 0:
    print ("These are number comes when you add all numbers from " + str (un1) + " to " + str (nca) + " = " + str (un1)  + "  (Added 0 time)")
elif un2 == 1:
    print ("These are number comes when you add all numbers from " + str (un1) + " to " + str (nca) + " = " + str (ans) + ' (Added ' + str (un2) +  " time)")
else:
    print ("These are number comes when you add all numbers from " + str (un1) + " to " + str (nca) + " = " + str (ans) + ' (Added ' + str (un2) +  " times)")
