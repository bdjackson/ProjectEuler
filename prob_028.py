#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=28                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = What is the sum of the numbers on the diagonals in a 1001 by 1001       =
#  = spiral?                                                                 =
#  ===========================================================================

# ----------------------------------------------------------------------------
def addNewLayer(start, size):
  # ----------------------------------------------------------------------------
  # print '---------------------------------------------'
  # print 'start: %d' % start
  # print 'size: %d' % size

  contribution_from_layer = 0
  corner = start
  for i in xrange(1,5):
    corner += size-1
    contribution_from_layer += corner
    # print '\tcorner: %d' % corner
    # print '\tcontribution from layer: %d' % contribution_from_layer

  return (contribution_from_layer, corner)

# ----------------------------------------------------------------------------
def findSumOfDiagonals(max_size):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  size = 1
  last_corner = 1
  sum_of_diagonals = 1

  while size < max_size:
    size += 2
    (contribution_from_layer, last_corner) = addNewLayer(last_corner, size)
    sum_of_diagonals += contribution_from_layer

  print 'Sum of diagonals of a %dx%d spiral is %d' % (max_size, max_size, sum_of_diagonals)
  return sum_of_diagonals

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findSumOfDiagonals(5)
  print '========================================'
  findSumOfDiagonals(1001)
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 669171001
