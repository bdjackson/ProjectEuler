#!/usr/bin/env python 
# ============================================================================
import sys
import math

#  ===========================================================================
#  = http://projecteuler.net/problem=6                                       =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the difference in the sum of squares and the square of the sum     =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getSumOfSquares(list_of_nums):
  """
  returns the sum of squares of the list of numbers
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sum = 0
  for i in list_of_nums:
    sum += i*i
  return sum

# ----------------------------------------------------------------------------
def getSquareOfSum(list_of_nums):
  """
  returns the square of the sum of the list of numbers
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sum = 0
  for i in list_of_nums:
    sum += i
  return sum*sum

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  list_of_nums = xrange(100+1)
  print getSquareOfSum(list_of_nums)-getSumOfSquares(list_of_nums)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 6857
