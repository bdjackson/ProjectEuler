#!/usr/bin/env python
# ============================================================================
import sys
import math

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
def checkPrimesFromLeft(candidate, prime_seive):
    num_digits = int(1+math.log(candidate, 10))
    print 'num_digits: %d' % num_digits
    is_removable = True
    test = candidate

    for i in xrange(num_digits):
        test = test%(10**(num_digits-i))
        print 'test: %s' % test
        if not prime_seive.isPrime(test):
            is_removable = False
            break

    return is_removable

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  prime_seive = primes_pp.primeSeive(10000)
  print checkPrimesFromLeft(3797, prime_seive)
  print checkPrimesFromLeft(3787, prime_seive)
  pass

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
#

