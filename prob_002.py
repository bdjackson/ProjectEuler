#!/usr/bin/env python 
# ============================================================================
import sys

import fibonacci

#  ===========================================================================
#  = http://projecteuler.net/problem=2                                       =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the sum of even Fibonacci numbers less than 4e6                    =
#  ===========================================================================

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def sumOfEvenFibNumbers(max = 100):
  """Find the sum of even Fibonacci numbers below max"""
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  last_num = 1
  this_num = 1
  sum_of_fib_nums = 0

  while this_num <  max: 
    if this_num % 2 == 0:
      sum_of_fib_nums += this_num
    print '%d -- %d' % (this_num, sum_of_fib_nums)
    next_num = fibonacci.nextFib(last_num, this_num)
    last_num = this_num
    this_num = next_num

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  sumOfEvenFibNumbers(4e+6)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 4613732
