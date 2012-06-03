#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=13                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the first ten digits of the sum of many 50 digit numbers           =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getSumOfFile(in_file_name):
  """
  read file and take the sum of all the numbers in the file
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  in_file = file(in_file_name)
  the_sum = 0
  for line in in_file:
    the_sum += int(line)
  return the_sum

# ----------------------------------------------------------------------------
def getNDigitsFromSum(in_file_name, num_digts):
  """
  read a file, take the sum, and print the first 10 digits
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num = getSumOfFile(in_file_name)
  num_str = str(num)

  digits_to_print = min(len(num_str), num_digts)
  first_n_digits = ''
  for i in xrange(0, digits_to_print):
    first_n_digits += num_str[i]

  print 'The first %d digits of the sum is %s' % (num_digts, first_n_digits)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  getNDigitsFromSum('prob_013_test.in', 10)
  print '================================================================'
  getNDigitsFromSum('prob_013.in', 10)
  print '================================================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 5537376230
