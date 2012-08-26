#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# =============================================================================
# = http://projecteuler.net/problem=47                                        =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the first four consecutive integers that have four distinct prime    =
# = factors                                                                   =
# =============================================================================

# -----------------------------------------------------------------------------
def findConsecutiveIntegers(num_integers, num_primes, terminal = None):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # if terminal == None: terminal = int(1e7)
    if terminal == None: terminal = int(10**(2+num_primes))

    print 'Generating primes from 2-%d' % terminal
    prime_seive = primes_pp.primeSeive(terminal)
    consecutive_integers = []
    print 'Primes successfully generated'

    for cand in xrange(terminal):
        prime_factors = set(primes_pp.getPrimeFactors(cand, prime_seive))
        if len(prime_factors) == num_primes:
            consecutive_integers.append(cand)
        else:
            del consecutive_integers[:]
        if len(consecutive_integers) == num_integers:
            break
    return consecutive_integers

# =============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print findConsecutiveIntegers(2,2)
  print findConsecutiveIntegers(3,3)
  print findConsecutiveIntegers(4,4)
  pass

# =============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# =============================================================================
# ============
# = solution =
# ============
# Generating primes from 2-10000
# Primes successfully generated
# [14, 15]
# Generating primes from 2-100000
# Primes successfully generated
# [644, 645, 646]
# Generating primes from 2-1000000
# Primes successfully generated
# [134043, 134044, 134045, 134046]
#
# real	0m34.028s
# user	0m33.834s
# sys	0m0.099s
