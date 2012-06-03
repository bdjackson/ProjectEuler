#!/usr/bin/env python 
# ============================================================================
import sys
import math

import primes

#  ===========================================================================
#  = http://projecteuler.net/problem=42                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Looking at a list of common english words, how many are triangular?     =
#  ===========================================================================

# -----------------------------------------------------------------------------
def getWordListFromFile(f_name):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  f = open(f_name)
  file_contents = f.readlines()
  words = []
  for c in file_contents:
    c = c.replace('"', '')
    words.extend(c.split(','))
  return words

# -----------------------------------------------------------------------------
def isTriangularNumber(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  is_triangular = False
  x = int(math.sqrt(2*num))
  if 0.5*x*(x+1) == num:
    is_triangular = True
  return is_triangular

# -----------------------------------------------------------------------------
def isTriangularWord(word):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print 'word: %s' % word
  word_num = 0
  for l in word.lower():
    word_num += ord(l)-96
    print '\tl: %s - num: %d -- word_num: %d' % (l, (ord(l)-96), word_num)

  return isTriangularNumber(word_num)
    
# -----------------------------------------------------------------------------
def findTriangularWordsInList(f_name):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  words = getWordListFromFile(f_name)
  triangular_words = []
  for w in words:
    if isTriangularWord(w):
      triangular_words.append(w)

  print 'There are %d triangular words in the file %s' % (len(triangular_words), f_name)
  return triangular_words

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # getWordListFromFile('words.txt')
  print '====================================================================='
  for i in xrange(60):
    print 'i: %d -- is tri: %s' % (i, isTriangularNumber(i))
  print '====================================================================='
  print isTriangularWord('abcd')
  print '====================================================================='
  print isTriangularWord('sky')
  print '====================================================================='
  print isTriangularWord('SKY')
  print '====================================================================='
  findTriangularWordsInList('words.txt')
  print '====================================================================='

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# 162

