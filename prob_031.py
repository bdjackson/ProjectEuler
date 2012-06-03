#!/usr/bin/env python 
# ============================================================================
import sys

# ===========================================================================
# = http://projecteuler.net/problem=31                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the number of combinations of coins than make up 2 pounds          =
# ===========================================================================

# ----------------------------------------------------------------------------
def findNumCombos(goal, denoms, master = True):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if goal < 0: 
    # print '\tovershoot!'
    return 0
  if goal == 0:
    # print '\tsolution found!'
    return 1
  
  num_combos = 0
  for i, coin in enumerate(denoms):
    # print '\tcoin -- %d -- next goal: %d' % (coin, goal-coin)
    num_combos += findNumCombos(goal-coin, denoms[i:], False)

  if master:
    print 'Found %d combinations of coins that add up to %dp' % (num_combos, goal)
  return num_combos

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # denoms = [200, 100, 50, 20, 10, 5, 2, 1]
  denoms = [5, 2, 1]
  for i in xrange(1, 5):
    findNumCombos(i, denoms)
    print '========================================'
  denoms = [200, 100, 50, 20, 10, 5, 2, 1]
  findNumCombos(200, denoms)
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 
