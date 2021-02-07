#!/usr/bin/python

# Now we use for A the first 100 digits of p behind the decimal point:
# A=1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#
# and for B the next hundred digits:
# B=8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196


def fib(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

for index in range(0,17):
  passedN = (127+index*19)*(7**index)
  index =79 
  while fib(index)>(passedN/100):
    index-=1

print("fib number ", index, " equals ", fib(index) , " is less than or equal to ", passedN)
