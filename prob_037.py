#!/usr/bin/env python
# ============================================================================
import sys
import math
import operator

import primes_pp

# ===========================================================================
# = http://projecteuler.net/problem=37                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the sum of all prime numbers that are truncatable from both the    =
# = left and right                                                          =
# = Example: 3797                                                           =
# =   Right: 379                                                            =
# =          37                                                             =
# =          3                                                              =
# =   Left:  797                                                            =
# =          97                                                             =
# =          7                                                              =
# ===========================================================================

# -----------------------------------------------------------------------------
def checkPrimesFromRight(candidate, prime_seive):
    # num_digits = int(math.log(candidate, 10))
    num_digits = int(1 + math.log(candidate, 10))
    # print '\tnum_digits: %d' % num_digits
    is_removable = True
    test = candidate

    for i in xrange(num_digits):
        # test = int(test/10)
        test = int(candidate/(10**i))
        # print '\t\ttest: %s' % test
        if not prime_seive.isPrime(test):
            is_removable = False
            break

    return is_removable

# -----------------------------------------------------------------------------
def checkPrimesFromLeft(candidate, prime_seive):
    num_digits = int(1+math.log(candidate, 10))
    # print '\tnum_digits: %d' % num_digits
    is_removable = True
    test = candidate

    for i in xrange(num_digits):
        test = test%(10**(num_digits-i))
        # print '\t\ttest: %s' % test
        if not prime_seive.isPrime(test):
            is_removable = False
            break

    return is_removable

# -----------------------------------------------------------------------------
def findTruncatablePrimes(upper_limit):
    prime_seive = primes_pp.primeSeive(upper_limit)
    truncatable_primes = []
    for i in xrange(10, upper_limit):
        # print 'i: %d' % i
        if checkPrimesFromRight(i, prime_seive) and checkPrimesFromLeft(i, prime_seive):
            truncatable_primes.append(i)
    return truncatable_primes

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  trunc_primes = findTruncatablePrimes(1000000)
  print 'found %d truncatable primes' % len(trunc_primes)
  print trunc_primes
  print 'sum of truncatable primes: %d' % reduce(operator.add, trunc_primes)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# found 11 truncatable primes
# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# sum of truncatable primes: 748317
