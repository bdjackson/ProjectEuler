#!/usr/bin/env python 
# ============================================================================
import sys
import math

#  ===========================================================================
#  = http://projecteuler.net/problem=36                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of all numbers, less than one million, which are           =
#  = palindromic in base 10 and base 2.                                      =
#  ===========================================================================
# ----------------------------------------------------------------------------
def findBase10PalindromesWithNdigits(n_digits, master = True):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_distinct_digits = int((n_digits+1)/2)
  distinct_digits = []
  for i in xrange(10):
    if num_distinct_digits == 1:
      continue
    print 'i: %d' % i

  # num_distinct_digits = int((n_digits+1)/2)
  # print 'num distinct digits: %d' % num_distinct_digits
  # for i in xrange(10**num_distinct_digits):
  #   if i%10 == 0:
  #     continue
  #   distinct_digits = '%d' % i
  #   print 'i: %d -- distinct digits: %s' % (i, distinct_digits)

# =============================================================================
def isBase10Palindrome(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0: 
    return False

  num_str = str(num)
  num_digits = len(num_str)
  num_distinct_digits = int((num_digits+1)/2)
  is_palindrome = True
  for i in xrange(num_distinct_digits):
    if not num_str[i] == num_str[num_digits-1-i]:
      is_palindrome = False
      break
  # if is_palindrome:
  #   print 'num: %d' % num
  return is_palindrome

# =============================================================================
def isBase2Palindrome(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0: 
    return False
  
  bin_num = bin(num)
  bin_str = str(bin_num)[2:]
  bin_digits = len(bin_str)
  bin_distinct_digits = int((bin_digits+1)/2)
  # print 'num: %s bin_num: %s bin_digits: %d bin_distinct_digits: %d' % (num, bin_str, bin_digits, bin_distinct_digits)
  is_palindrome = True
  for i in xrange(bin_distinct_digits):
    if not bin_str[i] == bin_str[bin_digits-1-i]:
      is_palindrome = False
      break
  # if is_palindrome:
  #   print 'num: %d' % num
  return is_palindrome

# =============================================================================
def sumOfDoublePalindromes(terminal):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sum_of_palindromes = 0
  for i in xrange(terminal):
    if isBase10Palindrome(i) and isBase2Palindrome(i):
      print 'palindromic in both: %d' % i
      sum_of_palindromes += i
  print 'The sum of all palindromes less than %d is %d' % (terminal, sum_of_palindromes)
  return sum_of_palindromes

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sumOfDoublePalindromes(100)
  print '========================================'
  sumOfDoublePalindromes(int(1e6))
  print '========================================'
# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 872187

