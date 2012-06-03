#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=22                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = The score of a name in a list is given by summing the alphabetical      = 
#  = value of each letter and multiplying that value by the position in the  =
#  = list. Given a list of names, sort the names alphabetically, and find    = 
#  = the sum of scores                                                       =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getAlphaScore(name):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  name = name.lower()
  score = 0
  for l in name: 
    score += ord(l) - 96
  return score

# ----------------------------------------------------------------------------
def getNameScore(name, pos):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  return getAlphaScore(name)*pos

# ----------------------------------------------------------------------------
def getNameListFromFile(file_name):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  f = file(file_name)
  contents = f.read()
  contents = contents.replace('"', '')
  name_list = contents.split(',')
  return name_list

# ----------------------------------------------------------------------------
def getScoreForList(name_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  if isinstance(name_list, str):
    name_list = getNameListFromFile(name_list)

  name_list.sort()
  score = 0
  for i, name in enumerate(name_list):
    # print 'i: %d - %s' % (i+1, name)
    score += getNameScore(name, i+1)

  print 'The sum of scores for the names provided is %d' % (score)

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  getScoreForList('names_test.txt')
  print '========================================'
  getScoreForList('names.txt')
  print '========================================'

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 871198282
