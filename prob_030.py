#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=30                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of all numbers that can be written as the sum of fifth     =
#  = powers of their digits                                                  =
#  ===========================================================================

# ----------------------------------------------------------------------------
def sumOfDigits(num, function_output):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sum_of_elements = 0
  for d in str(num):
    sum_of_elements += function_output[int(d)]
  return sum_of_elements

# ----------------------------------------------------------------------------
def findNumsEqualToSumOfPowerOfDigits(power):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  pow_of_digits = [];
  for i in xrange(10):
    pow_of_digits.append(i**power)

  sum_of_special_nums = 0
  for i in xrange(10**(power+1)):
  # for i in xrange(10**(power+2)):
    if i == 1 or i == 0: continue

    if sumOfDigits(i, pow_of_digits) == i:
      print '%d = sum of %dth power of digits' % (i, power)
      sum_of_special_nums += i

  print 'sum of numbers that can be written as the %dth power of their digits is %d' % (power, sum_of_special_nums)
  return sum_of_special_nums


# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findNumsEqualToSumOfPowerOfDigits(4)
  print '========================================'
  findNumsEqualToSumOfPowerOfDigits(5)
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 
