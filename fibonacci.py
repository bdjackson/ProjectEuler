#!/usr/bin/env python 
# ============================================================================

#  =========================================================
#  = Helper functions for working with Fibonacci sequences =
#  =========================================================

# ----------------------------------------------------------------------------
def nextFib(x1, x2):
  """Find the next Fibonacci number given the previous two"""
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  return x1+x2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def sumOfFibNumbers(max = 100):
  """Find the sum of Fibonacci numbers below max"""
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  last_num = 1
  this_num = 1
  sum_of_fib_nums = 0

  while this_num <  max: 
    sum_of_fib_nums += this_num
    print '%d -- %d' % (this_num, sum_of_fib_nums)
    next_num = nextFib(last_num, this_num)
    last_num = this_num
    this_num = next_num
