# This Is For Reversing A Number
print ('This Is For Reversing A Number')

n = int (input ('Enter The Number You Want To Reverse: '))
rev = 0

while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n / 10
 
print(rev)

# Preferance
"""
|| n = 45 | rev = 0 | digit = 0 ||
     4         5          5
     0        54          4 

"""
"""
45 % 10 = 5
0 * 10 = 0 + 5 = 5
45 / 10 = 4
4 % 10 = 4
5 * 10 = 50 + 4 = 54
4 / 10 = 0
"""
