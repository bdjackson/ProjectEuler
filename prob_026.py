#!/usr/bin/env python 
# ============================================================================
import sys

# ===========================================================================
# = http://projecteuler.net/problem=26                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = Find the unit fraction (1/d) that has the longest repeating cycle of    =
# = digits                                                                  =
# ===========================================================================

# -----------------------------------------------------------------------------
def findRecuringCycle(d):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  found_recurring = False
  f = [1]
  while not found_recurring:
    f.append((f[-1]*10)%d)
    if (f[-1] == 0 or f[-1] in f[0:-1]):
      found_recurring = True

  cycle_len = 0
  if not f[-1] == 0:
    for i in xrange(len(f) - 1):
      if f[i] == f[-1]:
        cycle_len = len(f)-i-1
        break

  return cycle_len

# -----------------------------------------------------------------------------
def findLongestRecurringCycle(sentinal):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  len_max = 0
  d_max   = -1
  for d in xrange(1,sentinal):
    len_cycle = findRecuringCycle(d)
    if len_cycle > len_max:
      len_max = len_cycle
      d_max = d
  print "d = %d gives the longest recurring cycle (at %d digits) for values of d < %d" % (d_max, len_max, sentinal)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findLongestRecurringCycle(10)
  print '========================================'
  findLongestRecurringCycle(100)
  print '========================================'
  findLongestRecurringCycle(1000)
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
