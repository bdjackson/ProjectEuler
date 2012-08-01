#!/usr/bin/env python
# ============================================================================
import math
import collections
import operator

# =============================================================================
class primeSeive(object):
    # -----------------------------------------------------------------------------
    def __init__(self, upper_bound):
        self.upper_bound = int(upper_bound)
        self.prime_seive = [True]*(int(upper_bound)+1)
        self.performSeive()

    # -----------------------------------------------------------------------------
    def performSeive(self):
        for i in xrange(self.upper_bound+1):
            # Two special cases
            if i == 0 or i == 1:
                self.prime_seive[i] = False
            # if we have already excluded this, skip to save time
            if not self.prime_seive[i]:
                continue

            # if we get here, i is a prime, so exclude all multiples of i
            mults = 2*i
            while mults <= self.upper_bound:
                self.prime_seive[mults] = False
                mults += i

    # -----------------------------------------------------------------------------
    def isPrime(self, candidate):
        if candidate < 0 or candidate > self.upper_bound:
            print 'Prime candidate (%d) out of range [0,%d]' \
                    % (candidate, self.upper_bound)
            sys.exit( )

        return self.prime_seive[candidate]
