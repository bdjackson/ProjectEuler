#!/usr/bin/env python
# ============================================================================
import sys
import math
import operator

import primes_pp

# ===========================================================================
# = http://projecteuler.net/problem=41                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the largest n-digital pandigital prime that exists                 =
# ===========================================================================

# -----------------------------------------------------------------------------
def isPandigital(cand):
    n_digits = int(math.log(cand,10) + 1)
    cand_str = ''.join(sorted(str(cand)))
    test = ''.join([str(i) for i in range(1,n_digits+1)])
    return cand_str == test

# -----------------------------------------------------------------------------
def findLargestPrime():
    print 'getting prime seive'
    prime_seive = primes_pp.primeSeive(1e7)
    print 'prime seive constructed'

    max_prime = 0
    # definitely no 2,8, or 9 digit pandigital primes, so don't check
    for i in xrange(int(1e7),2,-1):
        # max_n_digit_prime = findLargestNDigitPrime(n_digit, prime_seive)
        if prime_seive.isPrime(i):
            if isPandigital(i):
                max_prime = i
                break

    print 'the max n-digit prime is %d' % max_prime
    return max_prime

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print findLargestPrime()

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# the max n-digit prime is 7652413
