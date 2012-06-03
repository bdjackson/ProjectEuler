#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=8                                       =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find largest product of consecutive digits in large number              =
#  ===========================================================================

# ----------------------------------------------------------------------------
def findProductOfList(list_of_nums = []):
  """
  return the product of values in a list
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # special cases: return 0 if empty list or if 0 is in list
  if len(list_of_nums) == 0 or 0 in list_of_nums:
    return 0

  # get product of digits in list 
  product = 1
  for n in list_of_nums:
    product *= n
  return product

# ----------------------------------------------------------------------------
def getLargestProductOfConsecutiveDigits(num, num_digits):
  """
  returns the largest product of num_digits consecutive digits
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # if num is an int, convert to a string. this helps when looping over digits
  if isinstance(num, int) or isinstance(num, long): num = str(num)

  max_product = 0
  num_list = []
  for i, n in enumerate(num):
  # for n in num:
    # add latest digit to list 
    num_list.append(int(n))
    # remove oldest digit 
    if len(num_list) > num_digits: 
      num_list.pop(0)
    # if we have the right number of digits, check for max product
    if len(num_list) == num_digits:
      product = findProductOfList(num_list)
      if product > max_product: 
        max_product = product
      # print '%d -- %s -- %s -- %d -- %d' % (i,n,num_list, product, max_product)

  return max_product

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  large_num = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

  print  getLargestProductOfConsecutiveDigits(large_num, 5)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 40824
