#!/usr/bin/env python 
# ============================================================================
import sys
import math

#  ===========================================================================
#  = http://projecteuler.net/problem=34                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of all numbers that can be written as the sum of           =
#  = the factorial of their digits                                           =
#  ===========================================================================

# ----------------------------------------------------------------------------
def sumOfDigits(num, function_output):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

  sum_of_elements = 0
  for d in str(num):
    sum_of_elements += function_output[int(d)]
  return sum_of_elements

# ----------------------------------------------------------------------------
def findNumsEqualToSumOfFactorials(max):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if not isinstance(max, int): max = int(max)

  factorial_of_digits = [];
  for i in xrange(10):
    factorial_of_digits.append(math.factorial(i))

  sum_of_special_nums = 0
  for i in xrange(max):
    if i == 1 or i == 2: continue

    if sumOfDigits(i, factorial_of_digits) == i:
      print '%d = sum of factorial of digits' % (i)
      sum_of_special_nums += i

  print 'sum of numbers that can be written as the factorial of their digits is %d' % (sum_of_special_nums)
  return sum_of_special_nums


# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findNumsEqualToSumOfFactorials(100)
  print '========================================'
  findNumsEqualToSumOfFactorials(1000)
  print '========================================'
  findNumsEqualToSumOfFactorials(1e5)
  print '========================================'
  findNumsEqualToSumOfFactorials(1e6)
  print '========================================'
  findNumsEqualToSumOfFactorials(1e7)
  print '========================================'
# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 40730
