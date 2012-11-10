#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# ==============================================================================
# = http://projecteuler.net/problem=49                                         =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ==
# = The sequence [1487, 4817, 8147] is special because is has the following    =
# = properties:                                                                =
# = - each term increases by 3330                                              =
# = - each term is prime                                                       =
# = - each term is a permutation of each other                                 =
# = There exists one additional sequence with these properties. Find this      =
# = sequence                                                                   =
# ==============================================================================

# ----------------------------------------------------------------------------
def isPermutation(n1, n2):
    return sorted('%d' % n1) == sorted('%d' % n2)

# -----------------------------------------------------------------------------
def findSpecialSequences(lower_bound = 1000, upper_bound = 3339, delta = 3330):
    max_prime = 10**(int(math.log10(upper_bound)+1))
    print 'Generating primes from 2-%d' % max_prime
    prime_seive = primes_pp.primeSeive(max_prime)
    print 'Primes successfully generated'
    special_sequences = []

    for cand in xrange(lower_bound, upper_bound):
        n1 = cand
        n2 = cand + delta
        n3 = cand + 2*delta
        if not prime_seive.isPrime(n1): continue
        if not prime_seive.isPrime(n2): continue
        if not prime_seive.isPrime(n3): continue

        if not isPermutation(n1, n2): continue
        if not isPermutation(n1, n3): continue

        special_sequences.append([n1, n2, n3])

    print 'Found %d special sequences' % len(special_sequences)
    for ss in special_sequences:
        print '%s -- %d%d%d' % (ss, ss[0], ss[1], ss[2])
    return special_sequences

# =============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  findSpecialSequences(1000, 3339)

# =============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# =============================================================================
# ============
# = solution =
# ============
# Found 2 special sequences
# [1487, 4817, 8147] -- 148748178147
# [2969, 6299, 9629] -- 296962999629
# 
# real	0m0.053s
# user	0m0.035s
# sys	0m0.016s

