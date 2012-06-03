#!/usr/bin/env python
# ============================================================================
import sys
# import math

#  ===========================================================================
#  = http://projecteuler.net/problem=206                                     =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  =                                                                         =
#  = Find the unique positive integer whose square has the form              =
#  = 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.                  =
#  ===========================================================================

# -----------------------------------------------------------------------------
def prep_numbers(x):
  """
  docstring
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  # for i in xrange(len(x)):
  #   if x[i] == None:
  #     x[i] = range(10)
  #   if not isinstance(x[i], list):
  #     x[i] = [x[i]]
  # y = [range(10)]*int((len(x)+1)/2)
  y = [None]*int((len(x)+1)/2)
  return x, y

# -----------------------------------------------------------------------------
def passTest(x, y, test_place):
  """
  docstring
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  test_num = 0
  for t in xrange(test_place+1):
    # print 't: %d' % t

    pow_of_ten = 10**t
    test_num -= pow_of_ten * x[-1-t]
    y_indices = min(t, (len(y)-1))
    for i in xrange(y_indices+1):
      for j in xrange(y_indices+1):
        if (i+j) == t:
          test_num += pow_of_ten * (y[-1-i]*y[-1-j])
    # print 'test_num[t = %d]: %d' % (t, test_num)
  # print 'test_place: %d -- test_num: %d %% %d' % (test_place, test_num, (10**(test_place+1)))
  # print '\ttest: %d' % ((test_num)%(10**(test_place+1)))
  # return ( (abs(test_num)%(10**(test_place+1))) == 0 )
  if test_place == len(x)-1:
    return ( test_num == 0 )
  return ( ((test_num)%(10**(test_place+1))) == 0 )

# -----------------------------------------------------------------------------
def find_perfect_square(x, y = None, test_place = 0):
  """
  docstring
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  # print '--------------------------------------------------------'
  if test_place == len(x):
    return x,y,True

  found_solution = False

  if y == None:
    x,y = prep_numbers(x)
    # print 'x: %s' % x
    # print 'y: %s' % y

  x_vals = x[-1-test_place]
  reset_x = False
  if x_vals == None:
    reset_x = True
    x_vals = range(10)
  else:
    x_vals = [x_vals]

  y_place = min(test_place, (len(y)-1))
  y_vals = y[-1-y_place]
  reset_y = False
  if y_vals == None:
    reset_y = True
    y_vals = range(10)
  else:
    y_vals = [y_vals]

  for x_test in x_vals:
    x[-1-test_place] = x_test
    for y_test in y_vals:
      y[-1-y_place] = y_test
      # print '%sx: %s' % ('\t'*test_place, x)
      # print '%sy: %s' % ('\t'*test_place, y)
      # print passTest(x,y,test_place)
      if passTest(x,y,test_place):
        x,y,found_solution = find_perfect_square(x,y,test_place+1)
        if found_solution:
          return x,y,found_solution

  if reset_x:
    x[-1-test_place] = None
  if reset_y:
    y[-1-y_place] = None

  return x,y,False

# -----------------------------------------------------------------------------
def display_solution(x,y,found_solution):
  """
  display the solution
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if found_solution:
    print 'Found solution:'
    x_int = int(str(x).strip('[]').replace(', ', ''))
    y_int = int(str(y).strip('[]').replace(', ', ''))

    print '\tx: %d (%s)' % (x_int, x)
    print '\ty: %d (%s)' % (y_int, y)
  else:
    print 'No solution found'

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print '========================================'
  x = [1,None,6,None,1]
  x,y,found_solution = find_perfect_square(x)
  display_solution(x,y,found_solution)

  print '========================================'
  x = [1,None,4,None,4,None,9]
  x,y,found_solution = find_perfect_square(x)
  display_solution(x,y,found_solution)

  print '========================================'
  x = [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9,None,0]
  x,y,found_solution = find_perfect_square(x)
  display_solution(x,y,found_solution)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
#
