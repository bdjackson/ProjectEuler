#!/usr/bin/env python 
# ============================================================================
import sys
import math
import primes

#  ===========================================================================
#  = http://projecteuler.net/problem=35                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = How many circular primes are there below 1 million                      =
#  ===========================================================================

# -----------------------------------------------------------------------------
def rotateNum(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  num_str = str(num)
  rotated_num = num_str[1:]+num_str[0]
  return int(rotated_num)

# -----------------------------------------------------------------------------
def firstPass(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  possible_circle_prime = True
  if not num == 2:
    bad_digits = ['0', '2', '4', '6', '8']
    num_str = str(num)
    for d in num_str:
      if d in bad_digits:
        possible_circle_prime = False
        break
  return possible_circle_prime

# ----------------------------------------------------------------------------
def findCircularPrimesBelow(terminal):
  """docstring for findCircularPrimesBelow"""
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  prime_seive = primes.primeSeive(terminal)
  # print prime_seive
  checked = [False]*terminal
  circular_primes = []
  num_checked = 0
  for i in xrange(terminal):
    if checked[i]:
      continue
    
    if num_checked%1000 == 0:
      print 'checking %dth digit -- %d' % (num_checked, i)
    num_checked+=1

    # circle_prime = (not i%10 == 0)
    # circle_prime = True
    circle_prime = firstPass(i)
    last_num = i
    next_num = -1
    while not next_num == i and circle_prime:
      next_num = rotateNum(last_num)
      # if not len(str(next_num)) == len(str(i)):
      if next_num < i:
        circle_prime = False
        break
      circle_prime = circle_prime and next_num in prime_seive
      last_num = next_num
      checked[next_num] = True
    # print 'i: %d - is circular prime: %s' % (i, circle_prime)
    
    if circle_prime: 
      # print 'saving circular primes!'
      last_num = i
      next_num = -1
      while not next_num == i:
        next_num = rotateNum(last_num)
        # print '\tnext_num: %d' % next_num
        circular_primes.append(next_num)
        last_num = next_num
  
  # circular_primes = []
  # for i, p in enumerate(is_circular_prime):
  #   if p: circular_primes.append(i)
  print 'There are %d circular primes less than %d' % (len(circular_primes), terminal)

  return circular_primes

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # for i in xrange(100):
  #   print 'i: %s -- rot: %d' % (i, rotateNum(i))

  cp = findCircularPrimesBelow(100)
  cp.sort()
  print cp
  print '========================================'
  cp = findCircularPrimesBelow(int(1e6))
  cp.sort()
  print cp
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 55

