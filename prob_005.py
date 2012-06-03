#!/usr/bin/env python 
# ============================================================================

#  =====================================
#  = http://projecteuler.net/problem=5 =
#  =====================================

# ----------------------------------------------------------------------------
def find_factors(num):
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 1: return []
  lowest_factor = 1
  for i in xrange(2,num+1):
    if num%i == 0:
      lowest_factor = i
      break
  factors = [lowest_factor]
  factors.extend(find_factors(num/lowest_factor))
  return factors

# ============================================================================
common_multiple = 1
# for i in xrange(20, 0, -1):
for i in xrange(1, 20):
  # print find_factors(i)
  factors = find_factors(i)
  for f in factors:
    if common_multiple%i or common_multiple%f:
      common_multiple *= f
  # if common_multiple%i:
  #   common_multiple *= i
  print i, ' - ', common_multiple
  
print common_multiple

# ============================================================================
#  ============
#  = solution =
#  ============
# 232792560
