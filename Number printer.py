# This Program Takes A Number And Prints It At The End It Prints All Numbers
print ('This Program Takes a Number and prints it at the end it prints all numbers')

Quit = ""
bitwise = 0
a = 0

while Quit == "":
    Value = int(input('Enter a Number: **'))
    print (Value)
    bitwise = Value|bitwise
    Quit = input ('Hit Return to continue, or hit any another key (and Return) to quit: **')
result = bitwise
while a < Value:
    result = bitwise & a ** 2
    if result != 0:
        print ('You Have entered ' + str(a ** 2))
        a = int(a)
    else:
        print ('You Have not entered ' + str(a ** 2))
        a = int(a)
        
print('The Entered number(s) are ' + str(result))

# Prefarance
"""
0 < 8
bw = 0000 1111
val= 0000 1000
bw = 0000 1111
a**2=0000 0001
bw = 0000 1111
res= 0000 0001
res != 0 ( True )
You have entered 1
1 < 8
1 ** 2 = 2
bw = 0000 1111
a**2=0000 0010
res= 0000 0010
2 != 0 ( True )
You have entered 2
2 < 8
2 ** 2 = 4
bw = 0000 1111
a**2=0000 0100
res= 0000 0100
res != 0 ( True )
You have entered 4
4 < 8
4 ** 2 = 8
bw = 0000 1111
a**2=0000 1000
res= 0000 1000
res != 0 ( True )
You Have entered 4
8 < 8
"""
