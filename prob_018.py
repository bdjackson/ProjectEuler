#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=18                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the maximum sum traveling down a triangle                          =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getTriangle(in_file_name):
  """
  read triangle from file
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  in_file = file(in_file_name)
  triangle = []
  for line in in_file:
    digits = line.split()
    # print digits
    triangle.append(digits)
  # convert strings to ints and return 
  return [map(int, x) for x in triangle]

# ----------------------------------------------------------------------------
def printLine(line):
  """
  print all entries in a given line
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  to_print = ''
  for el in line:
    to_print += '%d ' % el
  print to_print

# ----------------------------------------------------------------------------
def findMaxForLines(line_1, line_2):
  """
  given two lines, find the maximum sum one could obtain stepping down from 
  the shorter line to the longer line 
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  long_line = line_1
  short_line = line_2

  if len(long_line) < len(short_line):
    long_line, short_line = short_line, long_line

  best_sum = []
  for i in xrange(len(short_line)):
    best_sum.append( max( short_line[i]+long_line[i]
                        , short_line[i]+long_line[i+1]
                        )
                   )
  return best_sum

# ----------------------------------------------------------------------------
def findMaxPath(in_file_name):
  """
  Given a triangle, find the maximum sum one can obtain following any path 
  from the top to bottom
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # get triangle from file
  triangle = getTriangle(in_file_name)
  print "Finding max sum for: "
  for line in triangle:
    printLine(line)
  print '----------------------------------------------------------------'

  # we want to work from the bottom up, not top down 
  rev_triangle = triangle[::-1]
  best_sum = rev_triangle[0]

  # loop through lines (bottom up), and find the maximum sum one can obtain
  # from each node one line up 
  for i in xrange(1, len(rev_triangle)):
    best_sum = findMaxForLines(best_sum, rev_triangle[i])

  # Done looping, print/return the answer
  assert(len(best_sum) == 1)
  print "The max sum is %d" % best_sum[0]
  return best_sum[0]

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findMaxPath('prob_018_test.in')
  print '================================================================'
  findMaxPath('prob_018.in')

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 1074
