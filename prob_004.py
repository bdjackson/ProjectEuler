#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=4                                       =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the largest palindrome made from the product of two 3-digit        =
#  = numbers                                                                 =
#  ===========================================================================

# ----------------------------------------------------------------------------
def isPalendrome(num):
  """
  is num a palendrome?
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_str = str(num)
  rev_num = num_str[::-1]
  # print '%s -- %s' % (num_str, rev_num)
  return num_str == rev_num

# ----------------------------------------------------------------------------
def findLargestPalendromeProduct(min_comp, max_comp):
  """
  Find the largest palendrome made from the product of numbers between 
  min_comp and max_comp
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  max_palendrome = 0
  for x in xrange(min_comp, max_comp+1):
    for y in xrange(x, max_comp+1):
      product = x*y
      # print 'x: %d - y: %d == x*y: %d' % (x, y, product)
      if isPalendrome(product) and product > max_palendrome:
        max_palendrome = product

  return max_palendrome
  
# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # print findLargestPalendromeProduct(10, 99)
  print findLargestPalendromeProduct(100, 999)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 906609
