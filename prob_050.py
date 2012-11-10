#!/usr/bin/env python
# =============================================================================
import sys
import math
import operator

import primes_pp

# ==============================================================================
# = http://projecteuler.net/problem=50                                         =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -=
# = 
# ==============================================================================

# ------------------------------------------------------------------------------
def getLongestSum(num, prime_list):
    tail_it = 0
    running_sum = 0
    running_sum_length = 0
    longest_sum_length = 0

    for head in prime_list:
        running_sum += head
        running_sum_length += 1

        while running_sum > num:
            running_sum -= prime_list[tail_it]
            tail_it += 1
            running_sum_length -= 1
        if running_sum == num:
            longest_sum_length = running_sum_length
            break
            # if running_sum_length > longest_sum_length:
            # if running_sum_length < longest_sum_length:

    return longest_sum_length

# ------------------------------------------------------------------------------
def findLongestSum(terminal = 100):
    print 'Generating primes from 2-%d' % terminal
    prime_seive = primes_pp.primeSeive(terminal)
    print 'Primes successfully generated'
    special_sequences = []

    prime_list = prime_seive.getPrimeList()
    longest_prime = 2
    max_length = 0
    print 'Looping over %d primes' % len(prime_list)
    for i, p in enumerate(prime_list):
        if i%1000 == 0: print 'i: %d -- p: %d' % (i,p)

        this_length = getLongestSum(p, prime_list)
        if this_length > max_length:
            longest_prime = p
            max_length = this_length

    print ''
    print 'prime below %d with longest sum: %d' % (terminal, longest_prime)
    print 'sum length: %d' % max_length

# ==============================================================================
def main():
    findLongestSum(10**6)

# ==============================================================================
if __name__ == "__main__":
  sys.exit( main() )

# ==============================================================================
# ============
# = solution =
# ============
