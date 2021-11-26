a = int (input ('Enter a Number: '))
b = int (input ('Enter a Number: '))
c = int (input ('Enter a Number: '))
if (a < b) and (a < c):
  print (str (a) + ' Is The Smallest.')
elif (b < a) and (b < c):
  print (str (b) + ' Is The Smallest.')
else:
  print (str (c) + ' Is The Smallest.') 

