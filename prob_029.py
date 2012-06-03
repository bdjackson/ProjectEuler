#!/usr/bin/env python 
# ============================================================================
import sys
import math
import collections

#  ===========================================================================
#  = http://projecteuler.net/problem=29                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  =                                                                         =
#  ===========================================================================

# ----------------------------------------------------------------------------
def findDistinctNums(a_max, b_max):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  filter = collections.Counter()
  # filter = [False]*((a_max)**(b_max)+1)
  # filter = set()

  for a in xrange(2, a_max+1):
    last_num = a
    for b in xrange(2, b_max+1):
      last_num *= a
      # filter[last_num] = True
      filter[last_num]+=1

  distinct_nums = list(filter)
  distinct_nums.sort()

  print 'There are %d distinct terms for 2<=a<=%d, 2<=b<=%d' % (len(distinct_nums), a_max, b_max)
  
  return distinct_nums

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findDistinctNums(5, 5)
  print '========================================'
  findDistinctNums(10, 10)
  print '========================================'
  findDistinctNums(100, 100)
  print '========================================'
# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 9183
