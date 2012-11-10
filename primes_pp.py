#!/usr/bin/env python
# =============================================================================
import sys
import math
import collections
import operator

# =============================================================================
class primeSeive(object):
    # -------------------------------------------------------------------------
    def __init__(self, upper_bound):
        self.upper_bound = int(upper_bound)
        # self.prime_seive = [True]*(int(upper_bound)+1)
        # self.prime_seive = [False,True]*(int(upper_bound/2)+2)
        self.prime_seive = []
        self.prime_list = None
        self.performSeive()

    # -------------------------------------------------------------------------
    def performSeive(self):
        tmp_prime_seive = [False, True]*(int(self.upper_bound/2.)+2)
        for i in xrange(self.upper_bound+1):
            # Two special cases
            if i == 0 or i == 1:
                # self.prime_seive[i] = False
                tmp_prime_seive[i] = False
            if i == 2:
                # self.prime_seive[i] = True
                tmp_prime_seive[i] = True
                continue
            # if we have already excluded this, skip to save time
            # if not self.prime_seive[i]:
            if not tmp_prime_seive[i]:
                continue

            # if we get here, i is a prime, so exclude all multiples of i
            # mults = 2*i
            mults = 3*i
            while mults <= self.upper_bound:
                # self.prime_seive[mults] = False
                tmp_prime_seive[mults] = False
                mults += i
        self.prime_seive = tmp_prime_seive

    # -------------------------------------------------------------------------
    def isPrime(self, candidate):
        if candidate < 0 or candidate > self.upper_bound:
            print 'Prime candidate (%d) out of range [0,%d]' \
                    % (candidate, self.upper_bound)
            sys.exit( )

        return self.prime_seive[candidate]

    # -------------------------------------------------------------------------
    def getPrimeList(self):
        if self.prime_list == None:
            self.prime_list = []
            for cand in xrange(self.upper_bound):
                if self.isPrime(cand):
                    self.prime_list.append(cand)
        return self.prime_list

# -----------------------------------------------------------------------------
def isPrime(num):
    """
    Is this number prime?
    """
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Special case for 0, 1
    if num == 0 or num == 1:
        return False

    # variables used in checking for primes
    is_prime = True
    max_possible = int(math.sqrt(num)+1)
    test = 2

    # check if num is factorable
    while test < max_possible and is_prime:
        if num % test == 0:
            is_prime = False
        test += 1
    return is_prime

# -----------------------------------------------------------------------------
def getPrimeFactors(num, prime_seive):
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    if num == 0 or num == 1:
        return []

    primes_list = prime_seive.getPrimeList()
    prime_factors = []
    test_num = num
    for p in primes_list:
        while test_num % p == 0:
            prime_factors.append(p)
            test_num /= p
        if test_num == 1:
            break
    return prime_factors
