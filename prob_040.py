#!/usr/bin/env python 
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=40                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Consider the irrational number formed by concatenating the positive     =
# = integers.                                                               =
# = if d_n is the nth digit in this irrational number, find the product     =
# =   d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000          =
# ===========================================================================

# -----------------------------------------------------------------------------
def findNthDigitInFraction(dig):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  nth_digit = None
  pow_of_ten = 0
  digits_covered = 0
  digits_left = dig
  last_num = 0
  
  while nth_digit == None:
    pow_of_ten += 1
    prev_digits_covered = digits_covered
    digits_covered += ((10**pow_of_ten - 10**(pow_of_ten-1))*pow_of_ten)
    
    if dig <= digits_covered:
      num_w_nth_digit = last_num + int((digits_left+pow_of_ten-1)/pow_of_ten) + 0
      ith_digit_in_num = ((digits_left-1)%pow_of_ten)

      nth_digit = num_w_nth_digit
      nth_digit /= (10**(pow_of_ten-ith_digit_in_num-1))
      nth_digit %= 10
    else:
      digits_left = dig - digits_covered
      last_num += (digits_covered-prev_digits_covered)/pow_of_ten

    # ran too long... bail
    if pow_of_ten == 100:
      nth_digit = -1
    
  return nth_digit

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  for i in xrange(1,200):
    print 'i: %d -- %d' % (i, findNthDigitInFraction(i))
  print '==================================='
  product = 1
  for i in xrange(7):
    print 'i: %d -- %d' % (10**i, findNthDigitInFraction(10**i))
    product *= findNthDigitInFraction(10**i)
  print 'The product of digits is %d' % product
  print '==================================='

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 210

