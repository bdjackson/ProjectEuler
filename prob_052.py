#!/usr/bin/env python 
# ============================================================================
import sys

# ===========================================================================
# = http://projecteuler.net/problem=52                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the smallest positive integer x, such that 2x, 3x, 4x, 5x, 6x      =
# = contain the same digits                                                 =
# ===========================================================================

# -----------------------------------------------------------------------------
def hasSameDigits(n1, n2):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  s1 = list(str(n1))
  s2 = list(str(n2))

  s1.sort()
  s2.sort()

  return s1 == s2

# -----------------------------------------------------------------------------
def findNumWithSimilarMultiples(multiple_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  test_num = 0
  found_num = False
  while not found_num:
    test_num += 1
    # print 'test num: %d' % test_num
    same_digits = True
    for m in multiple_list:
      if not hasSameDigits(test_num , m*test_num):
        same_digits = False
        break
    if same_digits:
      found_num = True

  print '%d has the same digits as its multiples' % test_num
  print '\t%d' % test_num
  for m in multiple_list:
    print '\t%d' % (m*test_num)
  return test_num

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # for i in xrange(100):
  #   for j in xrange(100):
  #     print 'i: %d j: %d -- %s' % (i, j, hasSameDigits(i,j))
  print '========================================'
  # findNumWithSimilarMultiples([1,2])
  print '========================================'
  findNumWithSimilarMultiples([1,2,3,4,5,6])
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 142857
