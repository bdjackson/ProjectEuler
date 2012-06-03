#!/usr/bin/env python 
# ============================================================================
import sys
from operator import mul

#  ===========================================================================
#  = http://projecteuler.net/problem=9                                       =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = There exists exactly one Pythagorean triplet (a^2+b^2=c^2) such that    =
#  = a+b+c=1000. Find this triplet and then find the product abc             =
#  ===========================================================================

# ----------------------------------------------------------------------------
def isPythagoreanTriplet(a,b,c):
  """
  Is a,b,c a Pythagorean triplet?
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  return (a*a + b*b == c*c)

# ----------------------------------------------------------------------------
def getPythagoreanTripletWithSum(sum):
  """
  Given value, sum, find the Pythagorean triplet for which a+b+c=sum.
  If none exists, return [0,0,0]
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  tripple_found = False
  a = 0.
  b = 0.
  c = 0.

  while a < sum/3 and not tripple_found:
    # increment a by 1
    a += 1

    # get b value which would correspond with this a. This may not be an integer.
    b = (sum/2.-a)/(1-a/sum)

    # Now, check if b is an integer
    if b%1 == 0:
      print 'found tripple'
      tripple_found = True
  # compute c 
  c = sum - a - b

  # if no tripple found, reset a, b, and c
  if not tripple_found:
    a = 0.
    b = 0.
    c = 0.

  return [a, b, c]


  
# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  triplet = getPythagoreanTripletWithSum(1000)
  print 'The triplet is: (%d, %d, %d)' % (triplet[0], triplet[1], triplet[2])
  print 'The product abc is: %d' % reduce(mul, triplet)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 
