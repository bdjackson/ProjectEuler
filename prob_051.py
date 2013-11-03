#!/usr/bin/env python
# ============================================================================
import sys
import primes_pp
from collections import Counter

import cProfile
import re

# ===========================================================================
# = http://projecteuler.net/problem=51                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# =
# ===========================================================================

# ------------------------------------------------------------------------------
def hasDuplicate(val):
    return len(list(str(val))) != len(list(set(str(val))))

# ------------------------------------------------------------------------------
def replaceDuplicates(initial_value, num_to_replace = 2):
    # print 'initial value: %d' % initial_value
    initial_value_str = str(initial_value)
    count = Counter(initial_value_str)
    values_to_replace = []
    for val, instances in count.iteritems():
        if instances >= num_to_replace:
            values_to_replace.append(val)
    # print 'values to replace: %s' % values_to_replace

    indices_to_replace = []
    for vtr in values_to_replace:
        # print 'vtr: %s' % vtr

        occurances_of_vtr = [i for i, x in enumerate(initial_value_str) if x == vtr]

        indices_to_replace.extend(findCombinatorics( occurances_of_vtr
                                                   , target_len = num_to_replace
                                                   )
                                 )
        # print indices_to_replace

    #$ with_replacement = [[] for i in xrange(len(indices_to_replace))]
    with_replacement = []
    for itr in indices_to_replace:
        tmp_list = []
        for new_value in xrange(10):
            value_with_replacement = list(initial_value_str)
            for i in itr:
                value_with_replacement[i] = str(new_value)
            tmp_list.append(int(''.join(value_with_replacement)))
        with_replacement.append(tmp_list)

    # print 'with_replacement: %s' % with_replacement

    return with_replacement

# ------------------------------------------------------------------------------
def findCombinatorics(complete_list, target_len = 2, current_comb_list = [], start_index = 0, level = 0):
    if len(current_comb_list) == target_len:
        return current_comb_list

    new_comb_list = []
    for it in xrange(start_index, len(complete_list)):
        temp_list = current_comb_list[:]
        temp_list.append(complete_list[it])

        combinations_to_append = findCombinatorics( complete_list
                                              , target_len
                                              , temp_list
                                              , it+1
                                              , level+1
                                              )
        if combinations_to_append != []:
            # extend or append based on the level to ensure we end up with the
            # right list structure in the end
            if level >= target_len-1:
                new_comb_list.append(combinations_to_append)
            else:
                new_comb_list.extend(combinations_to_append)

    return new_comb_list


# ------------------------------------------------------------------------------
def findPrimesWithRepeats_old(upper_bound):
    ps = primes_pp.primeSeive(upper_bound)
    prime_list = ps.getPrimeList()

    for p in reversed(prime_list):
        if not hasDuplicate(p):
            prime_list.remove(p)
    return prime_list

# ------------------------------------------------------------------------------
def findPrimesWithRepeats(upper_bound):
    ps = primes_pp.primeSeive(upper_bound)
    prime_list = [p for p in ps.getPrimeList() if hasDuplicate(p)]

    # for p in reversed(prime_list):
    #     if not hasDuplicate(p):
    #         prime_list.remove(p)
    return prime_list

# ------------------------------------------------------------------------------
def findPrimeFamilies(family_size, upper_bound, max_replacements = 2):
    print 'constructing primes list'
    prime_list = findPrimesWithRepeats(upper_bound)
    print 'primes list completed'
    print 'constructing primes with dupliates filter'
    primes_filter = genPrimeWithDuplicateFilter(prime_list, upper_bound)
    print 'primes with dupliates filter completed'


    for i_pl, pl in enumerate(prime_list):
        if i_pl%1000 == 0:
            print 'checking prime number: %d' % pl
        for num_replacements in xrange(2, max_replacements+1):
            replacement_list = replaceDuplicates(pl, num_replacements)
            # print replacement_list

            for rl in replacement_list:
                rl_size = len(rl)
                if rl_size < family_size: continue

                family_list = []
                # print 'checking for these numbers in primes list: %s' % rl
                rejected = 0
                for cand in rl:
                    if rl_size - rejected < family_size: break

                    if primes_filter[cand]:
                        if cand < pl: break
                        family_list.append(cand)
                    else:
                        rejected += 1

                # print '\tfamily of primes: %s' % family_list
                if len(family_list) == family_size:
                    print 'Found family of size %d! %s' % (family_size, family_list)
                    return family_list
    return None

# # ------------------------------------------------------------------------------
# def optIsIn(cand, test_list, starting_index = 0):
#     for i_tl in xrange(starting_index, len(test_list)):
#         tl = test_list[i_tl]
#         if cand == tl: return i_tl
#         if cand < tl: break
#     return None

# ------------------------------------------------------------------------------
def genPrimeWithDuplicateFilter(primes_with_duplicates, upper_bound):
    primes_with_duplicates_filter = [False]*int(upper_bound)
    for pwd in primes_with_duplicates:
        primes_with_duplicates_filter[pwd] = True
    return primes_with_duplicates_filter

# ============================================================================
def main():
    # print 'true: %s' % hasDuplicate(555)
    # print 'false: %s' % hasDuplicate(123)
    # print 'true: %s' % hasDuplicate(12526785)
    # print 'false: %s' % hasDuplicate(123456789)

    # print findPrimesWithRepeats(100)
    # print findPrimesWithRepeats(10000)

    # replaceDuplicates(112)
    # replaceDuplicates(1122)
    # print replaceDuplicates(1112, 3)

    # print findCombinatorics([0, 1, 2, 3])
    # print findCombinatorics(['a', 'b', 'c', 'd'], target_len = 3)
    # print findCombinatorics(['a', 'b', 'c'])

    # findPrimeFamilies(7, 1e5)
    # findPrimeFamilies(7, 1e6)
    # findPrimeFamilies(7, 5e5)
    findPrimeFamilies(8, 1e6, 3)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# Found family of size 8! [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
#
# real	0m2.746s
# user	0m2.691s
# sys	0m0.038s

