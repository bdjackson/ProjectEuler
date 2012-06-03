#!/usr/bin/env python 
# ============================================================================
import sys
import math
import operator
import collections

import primes

#  ===========================================================================
#  = http://projecteuler.net/problem=23                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of all positive integers which cannot be written as the    =
#  = sum of two abundant numbers                                             =
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
def getListOfAbundantNumbers(min = -1, max = -1):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if min < 0: min = 0
  # this number is chosen based on the problem statement
  if max < 0: max = 28125
  
  list_of_primes = primes.primeSeive(max)
  abundant_nums = []

  for i in xrange(min, max+1):
    # if abundant number
    if sumOfDivisors(i, list_of_primes) > i: 
      # print '------------------------------------'
      # print '%d is an abundant number' % i
      # print '\tprime divisors: %s' % primes.getPrimeFactors(i, list_of_primes)
      # print '\tsum of divisors: %d' % sumOfDivisors(i, list_of_primes)
      abundant_nums.append(i)

  return abundant_nums

# ----------------------------------------------------------------------------
def findNumsNotMadeFromPairsInList(list, upper_limit):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # print list
  # from_list = [True]*(list[-1]+list[-2]+1)
  from_list = [True]*(upper_limit+1)

  for i in xrange(len(list)):
    # for j in xrange(i+1, len(list)):
    for j in xrange(i, len(list)):
      if list[i]+list[j] <= upper_limit:
        # print list[i]+list[j]
        from_list[list[i]+list[j]] = False

  nums_not_from_list = []
  for i in xrange(len(from_list)):
    if from_list[i]:
      nums_not_from_list.append(i)

  return nums_not_from_list

# ----------------------------------------------------------------------------
def sumOfNumsNotFromAbundantNums(min = -1, max = -1):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if min < 0:   min = 0
  if max < min: max = 28123
  abundant_nums = getListOfAbundantNumbers(min, max)
  nums_not_from_abundant_pair = findNumsNotMadeFromPairsInList(abundant_nums, max)
  sum = reduce(operator.add, nums_not_from_abundant_pair)
  
  # print 'list of abundant_nums: %s' % abundant_nums
  # print 'nums not from abundant pair: %s' % nums_not_from_abundant_pair
  print 'The sum of abundant numbers is %d' % sum
  return sum

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sumOfNumsNotFromAbundantNums(-1, 20)
  print '====================================================================='
  sumOfNumsNotFromAbundantNums(-1, 50)
  print '====================================================================='
  sumOfNumsNotFromAbundantNums()
  print '====================================================================='

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 4179871
