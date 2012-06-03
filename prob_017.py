#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=17                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = How many letters are neded to write all the numbers between 1 and 1000  =
#  ===========================================================================

# ============================================================================
map_1 = [ 'zero'   , 'one'    , 'two'      , 'three'   , 'four'
        , 'five'   , 'six'    , 'seven'    , 'eight'   , 'nine'
        , 'ten'    , 'eleven' , 'twelve'   , 'thirteen', 'fourteen'
        , 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' 
        ]
map_2 = [ ''     , 'ten'  , 'twenty' , 'thirty', 'forty'
        , 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ]
# map_3 = ['hundred', 'thousand']

# ----------------------------------------------------------------------------
def getWord(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  word = ''
  if num < 20:
    word = map_1[num]
  elif num < 100:
    tens_digit = int(num/10)
    remainder = num%10
    word = map_2[int(num/10)]
    if remainder:
      word += ' %s' % getWord(remainder)
  elif num < 1000:
    hundreds_digit = int(num/100)
    remainder = num%100
    # word = '%s hundred' % map_1[hundreds_digit]
    word = '%s hundred' % getWord(hundreds_digit)
    if remainder:
      word += ' and %s' % getWord(remainder)
  elif num < 1e6:
    thousands_digits = int(num/1000)
    remainder = num%1000
    word = '%s thousand' % getWord(thousands_digits)
    if remainder:
      word += ' %s' % getWord(remainder)
  return word

# ----------------------------------------------------------------------------
def getNumberOfLetters(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  num_word = getWord(num)
  num_word = num_word.replace(' ', '')
  num_word = num_word.replace('-', '')
  return len(num_word)

# ----------------------------------------------------------------------------
def getNumLettersInRange(start, end):
  total_num_letters = 0
  for i in xrange(start, end+1):
    total_num_letters += getNumberOfLetters(i)

  print 'The sum of the letters used to write out all the numbers between %d \
and %d inclusive is %d' % (start, end, total_num_letters)
  return total_num_letters

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # for i in xrange(1,1001):
  #   print '%d: %s (%d)' % (i, getWord(i), getNumberOfLetters(i))
  getNumLettersInRange(1, 5)
  print '========================================'
  getNumLettersInRange(1,1000)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 
