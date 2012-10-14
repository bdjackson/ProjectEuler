#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# =============================================================================
# = http://projecteuler.net/problem=352                                       =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Suppose T(m,p) is the average number of tests needed to screen a flock of =
# = sheep with size m for a virus with probability p of being present         =
# = Find sum( T(100000, p) for p = 0.01, 0.02, ... 0.50)                      =
# =============================================================================

# -----------------------------------------------------------------------------
def testWithinGroup(n, p, prime_sieve, certain = False):
    if n < 2: return n

    # Always do at least one test
    num_tests = 1

    # Only test further if the first test comes up positive. This gives the
    # probability of needing to do further tests
    master_mult = (1-(1-p)**n)
    master_mult = (1-(1-p)**n)

    if certain:
        num_tests = 0
        master_mult = 1

    # If the number of sheep is prime, we just have to check a single group
    if prime_sieve.isPrime(n):
        # If positive, we test all but one sheep in group
        num_tests += master_mult*(n-1)

        # Finally, if at least one of the (n-1) tests is positive, test the
        # final sheep
        num_tests += master_mult*(1-(1-p)**(n-1))

    else:
        # If we have a non-prime number of sheep, we make smaller groups
        num_grps = primes_pp.getPrimeFactors(n, prime_sieve)[0]
        num_per_grp = n/num_grps
        twg = testWithinGroup(num_per_grp, p, prime_sieve)
        twg_certain = testWithinGroup(num_per_grp, p, prime_sieve, True)

        # First, fully test all but one group
        num_tests += master_mult * ((num_grps-1) * twg)

        # If any of those groups is positive, test final group
        mult = master_mult * (1 - (1-p)**((num_grps-1)*num_per_grp))
        num_tests += mult * twg

        # If none of the groups were positive, we know the final group has an
        # infected sheep
        mult = master_mult * (1-p)**((num_grps-1)*num_per_grp)
        num_tests += mult * twg_certain

    return num_tests

# =============================================================================
def main():
    prime_sieve = primes_pp.primeSeive(1000)
    print '-------------------------------------'
    print testWithinGroup(1, 0.02, prime_sieve)
    print '-------------------------------------'
    print testWithinGroup(2, 0.02, prime_sieve)
    print '-------------------------------------'
    print testWithinGroup(3, 0.02, prime_sieve)
    print '-------------------------------------'
    print testWithinGroup(4, 0.02, prime_sieve)
    print '-------------------------------------'
    print testWithinGroup(5, 0.02, prime_sieve)
    print '-------------------------------------'
    print testWithinGroup(25, 0.02, prime_sieve)

# =============================================================================
if __name__ == "__main__":
    sys.exit( main() )

# =============================================================================
# ============
# = solution =
# ============
