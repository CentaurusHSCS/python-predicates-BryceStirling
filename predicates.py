import random
import time
import math
import unittest
import pytest

# is x between a and b
def between(x, a, b):
  if x > a and x < b or x < a and x > b or x == a or x == b:
    return True
  else:
    return False
  
# is x divisibleBy a ?
def isDivisibleBy(x, a):
  if a == 0:
    return False 
  if x%a == 0:
    return True
  else:
    return False
  
# is x even?
def isEvenNumber(x):
  if x%2 == 0:
    return True
  else:
    return False
  
# is x odd?
def isOddNumber(x):
  if x%2 == 0:
    return False
  else:
    return True

  
# do the sides a, b, c make a Pythagorean triangle
# remember the Pythagorean theorem
def isPythagorean(a, b, c):
  pythagoreanSqaured = a*a+b*b
  pythagorean = math.sqrt(pythagoreanSqaured)
  if pythagorean%1 == 0:
    return True
  else:
    return False
def isInteger(x):
  if type(x) == int:
    return True
  else:
    return False
def pointWithinCircle(x, y, cx, cy, radius):
  if math.sqrt((x-cx)**2 + (y - cy)**2) <= radius:
    return True
  else:
    return False
  return False
def withinRadius(x1, y1, x2, y2, distance):
  if math.sqrt((x1-x2)**2 + (y1 - y2)**2) <= distance:
    return True
  else:
    return False
# test between
print( "Is 10 between 8 and 12 " + str(between (10, 8, 12)))  

# test divisible by
print( "Is 10 divible by 2 " + str(isDivisibleBy (10, 2))) 

# test isEvenNumber
print( "is 80 even " + str(isEvenNumber(80))) 

assert(between(5, 1, 10) == True)     # x is between a and b
assert(between(11, 1, 10) == False)   # x is greater than b
assert(between(0, 1, 10) == False)    # x is less than a
assert(between(10, 1, 10) == True)    # x is equal to b
assert(between(1, 1, 10) == True) 

assert(isDivisibleBy(10, 2) == True)  # 10 is divisible by 2
assert(isDivisibleBy(10, 3) == False) # 10 is not divisible by 3
assert(isDivisibleBy(0, 1) == True)   # 0 is divisible by any non-zero number
assert(isDivisibleBy(10, 0) == False) # Dividing by zero should be False
    
    # Test for isEvenNumber(x)

assert(isEvenNumber(2) == True)       # 2 is even
assert(isEvenNumber(3) == False)      # 3 is odd
assert(isEvenNumber(0) == True)       # 0 is even
assert(isEvenNumber(-3) == False)     # -3 is odd
    
    # Test for isOddNumber(x)

assert(isOddNumber(3) == True)        # 3 is odd
assert(isOddNumber(4) == False)       # 4 is even
assert(isOddNumber(-5) == True)       # -5 is odd
assert(isOddNumber(0) == False)       # 0 is even
    
    # Test for isPythagorean(a, b, c)

assert(isPythagorean(3, 4, 5) == True)   # Pythagorean triplet
assert(isPythagorean(5, 5, 5) == False)  # Not a Pythagorean triplet
assert(isPythagorean(6, 8, 10) == True)  # Another Pythagorean triplet
assert(isPythagorean(1, 1, 1) == False)  # Not a valid triangle

assert(isInteger(3) == True)          # 3 is an integer
assert(isInteger(3.5) == False)       # 3.5 is not an integer
assert(isInteger(0) == True)          # 0 is an integer
assert(isInteger("3") == False)       # A string is not an integer
    
    # Test for pointWithinCircle(x, y, cx, cy, radius)
assert(pointWithinCircle(0, 0, 0, 0, 1) == True)   # Center of the circle
assert(pointWithinCircle(1, 1, 0, 0, math.sqrt(2)) == True)  # Point on the edge
assert(pointWithinCircle(2, 2, 0, 0, 1) == False)  # Point outside the circle
assert(pointWithinCircle(0.5, 0.5, 0, 0, 1) == True) # Point within the circle
    # Test for isInteger(x)

assert(isInteger(3) == True)          # 3 is an integer
assert(isInteger(3.5) == False)       # 3.5 is not an integer
assert(isInteger(0) == True)          # 0 is an integer
assert(isInteger("3") == False)       # A string is not an integer
    
    # Test for withinRadius(x1, y1, x2, y2, distance)

assert(withinRadius(1, 1, 1, 1, 0) == True)  # Same point, distance 0
assert(withinRadius(0, 0, 3, 4, 5) == True)  # Point is exactly on the edge (Pythagorean triplet)
assert(withinRadius(0, 0, 3, 4, 4) == False) # Point is outside the distance
assert(withinRadius(1, 1, 1, 2, 1) == True)  # Point within distance