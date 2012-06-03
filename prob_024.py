#!/usr/bin/env python 
# ============================================================================
import sys
import math

#  ===========================================================================
#  = http://projecteuler.net/problem=24                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the millionth lexicographic permutation of the digits              =
#  = 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9                                         =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getPermutations(num_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  assert(len(num_list) > 0)
  if len(num_list) == 1: 
    return [num_list]

  perm_list = []
  for i in xrange(len(num_list)):
    tmp = num_list[:i]
    tmp.extend(num_list[i+1:])
    sub_perms = getPermutations(tmp)

    for j in xrange(len(sub_perms)):
      perm = [num_list[i]]
      perm.extend(sub_perms[j])
      perm_list.append(perm)
    
  return perm_list

# ----------------------------------------------------------------------------
def getLexicographicPermutations(num_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_list.sort()
  return getPermutations(num_list)

# ----------------------------------------------------------------------------
def list2string(list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  string = ''
  for el in list:
    string += str(el)
  return string

# ----------------------------------------------------------------------------
def getNthLexicographicPermutation(num_list, n, print_result = True):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  n -= 1
  num_list.sort()
  perm = []

  length = len(num_list)
  perms_if_first_fixed = math.factorial(length-1)
  index_to_store = int(n/perms_if_first_fixed)
  perm.append(num_list[index_to_store])
  if index_to_store > 0:
    n %= perms_if_first_fixed

  num_list.pop(index_to_store)
  if len(num_list):
    perm.extend(getNthLexicographicPermutation(num_list, n+1, False))

  if print_result:
    print 'The %dth lexicographic permutation is %s' % (n, list2string(perm))

  return perm

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  print '========================================'
  for i in xrange(1, 25):
    getNthLexicographicPermutation([0,1,2,3], i)
    print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5,6], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5,6,7], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5,6,7,8], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
  print '========================================'
  getNthLexicographicPermutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], int(1e6))
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 2783915460
