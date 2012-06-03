#!/usr/bin/env python 
# ============================================================================
import sys
import operator
import collections

import primes

# ===========================================================================
# = http://projecteuler.net/problem=33                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = There are several fractions that can be reduced incorrectly, yet yield  =
# = a correct result.  For example: 49/98 = 4/8.                            = 
# = Ignoring trivial cases (30/50 = 3/5), find the sum of these fractions   =
# = which are less than 1, and have 2-digit numbers in then numerator and   =
# = denominator                                                             =
# ===========================================================================

# -----------------------------------------------------------------------------
def hasSimilarDigit(n1, n2):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  d1 = list(str(n1))
  d2 = list(str(n2))

  digit_index = [-1, -1]
  for i1 in xrange(len(d1)):
    for i2 in xrange(len(d2)):
      if d1[i1] == d2[i2]:
        digit_index = [i1, i2]

# -----------------------------------------------------------------------------
def doDumbReduction(n1, n2):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  d1 = list(str(n1))
  d2 = list(str(n2))

  found_common = False

  for i1 in xrange(len(d1)):
    for i2 in xrange(len(d2)):
      if d1[i1] == d2[i2]:
        found_common = True
        d1.pop(i1)
        d2.pop(i2)
        break
    if found_common:
      break

  red_num = 0
  red_den = 1
  if found_common:
    red_num = int(d1[0])
    red_den = int(d2[0])
  return {'num':red_num, 'den':red_den}

# -----------------------------------------------------------------------------
def findNumsWithDumbReduction():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  reducible_num = []
  reducible_den = []

  for den in xrange(11, 100):
    if den%10 == 0:
      continue
    for num in xrange(11, den):
      if num%10 == 0:
        continue
      reduced = doDumbReduction(num, den)
      red_frac = float(reduced['num'])/reduced['den']
      if float(num)/den == red_frac:
        reducible_num.append(reduced['num'])
        reducible_den.append(reduced['den'])

  print 'reduced nums: %s' % reducible_num
  print 'reduced denoms: %s' % reducible_den
  red_product_num = reduce(operator.mul, reducible_num)
  red_product_den = reduce(operator.mul, reducible_den)
  print 'product of reduced nums: %d'   % red_product_num
  print 'product of reduced denoms: %d' % red_product_den
  print 'product of reduced fracs: %f'  % (float(red_product_num)/red_product_den)

  primes_list = primes.primeSeive(red_product_num)
  print primes_list
  prime_factors_num = collections.Counter( primes.getPrimeFactors( red_product_num
                                                                 , primes_list)
                                                                 )
  prime_factors_den = collections.Counter( primes.getPrimeFactors( red_product_den
                                                                 , primes_list)
                                                                 )
  common_prime_factors = list((prime_factors_num & prime_factors_den).elements())
  for p in common_prime_factors:
    red_product_num /= p
    red_product_den /= p
  print 'Fully reduced product of special fractions is %d/%d = %f' % ( red_product_num
                                                                     , red_product_den
                                                                     , ( float(red_product_num)/red_product_den)
                                                                     )


# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findNumsWithDumbReduction()
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 100
