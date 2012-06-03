#!/usr/bin/env python 
# ============================================================================
import sys
import math
import operator
import collections

import primes

#  ===========================================================================
#  = http://projecteuler.net/problem=21                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Evaluate the sum of all the amicable numbers under 10000                =
#  =                                                                         =
#  = Let d(n) be defined as the sum of proper divisors of n. If d(a) = b and =
#  = d(b) = a where a != b, a and b are amicable numbers.                    =
#  ===========================================================================

# ----------------------------------------------------------------------------
def sumOfDivisors(num, primes_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if num == 0 or num == 1: 
    return 0

  prime_factors = collections.Counter(primes.getPrimeFactors(num, primes_list))

  sum_of_divisors = 1
  for pf in prime_factors:
    temp = 0
    for i in xrange(prime_factors[pf]+1):
      temp += pf**i
    sum_of_divisors *= temp
  
  return sum_of_divisors - num

# ----------------------------------------------------------------------------
def findAmicableNumbersBelowValue(end):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # list_of_primes = primes.primeSeive(end**2)
  list_of_primes = primes.primeSeive(end*1000)
  num_checked     = [False]*(end+1)
  is_amicable_num = [False]*(end+1)

  for i in xrange(end+1):
    if num_checked[i] == True:
      continue
    
    num_checked[i] = True
    sum_of_divisors = sumOfDivisors(i, list_of_primes)
    print 'i: %d - d(%d): %d - d(%d): %d' % (i, i, sum_of_divisors, sum_of_divisors, sumOfDivisors(sum_of_divisors, list_of_primes))
    if not sum_of_divisors == i and sumOfDivisors(sum_of_divisors, list_of_primes) == i:
      # print '\tamicable pair found'
      is_amicable_num[i] = True
      if sum_of_divisors < end+1:
        is_amicable_num[sum_of_divisors] = True
        num_checked[sum_of_divisors] = True

  amicable_nums = []
  for i in xrange(end+1):
    if is_amicable_num[i]:
      amicable_nums.append(i)
  return amicable_nums

# ----------------------------------------------------------------------------
def sumOfAmicableNumbersBelowValue(end):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  amicable_numbers = findAmicableNumbersBelowValue(end)
  sum_of_amicable_numbers = reduce(operator.add, amicable_numbers)

  print 'The amicable numbers belowe %d are %s' % (end, amicable_numbers)
  print 'The sum of all amicable numbers below %d is %d' % (end, sum_of_amicable_numbers)
  return sum_of_amicable_numbers

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # list_of_primes = primes.primeSeive(1e4)
  # print sumOfDivisors(220, list_of_primes)
  # print sumOfDivisors(284, list_of_primes)
  # print '====================================================================='

  sumOfAmicableNumbersBelowValue(500)
  print '====================================================================='
  sumOfAmicableNumbersBelowValue(1000)
  print '====================================================================='
  sumOfAmicableNumbersBelowValue(2000)
  print '====================================================================='
  sumOfAmicableNumbersBelowValue(5000)
  print '====================================================================='
  sumOfAmicableNumbersBelowValue(10000)
  print '====================================================================='

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 31626
