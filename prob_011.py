#!/usr/bin/env python 
# ============================================================================
import sys
import operator

#  ===========================================================================
#  = http://projecteuler.net/problem=11                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = Find the maximum product of adjacent digits in a grid                   =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getNumberGrid(in_file_name):
  """
  read grid from file
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  in_file = file(in_file_name)
  grid = []
  for line in in_file:
    digits = line.split()
    grid.append(digits)
  
  # convert strings to ints and return 
  return [map(int, x) for x in grid]

# ----------------------------------------------------------------------------
def printLine(line):
  """
  print all entries in a given line
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  to_print = ''
  for el in line:
    to_print += '%4d ' % el
  print to_print

# ----------------------------------------------------------------------------
def printGrid(grid):
  """
  print full grid
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  for line in grid:
    printLine(line)

# ----------------------------------------------------------------------------
def findMaxProductInList(nums, size = 4):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # print '-----------------------------------------'
  # print 'findMaxProductInList(%s, %d)' % (nums, size)
  roi = []
  max_product = 0
  for el in nums:
    roi.append(el)
    if (len(roi) > size):
      roi.pop(0)
    # print '\t%s' % roi
    if len(roi) == size: 
      # print '\t\tcorrect size, finding product'
      product = reduce(operator.mul, roi)
      # print product
      if product > max_product:
        max_product = product
  return max_product

# ----------------------------------------------------------------------------
def findMaxHorizProduct(grid, size = 4):
  """
  find the maximum product of size elements in all rows of the grid
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  local_max = []
  for row_num in xrange(len(grid)):
    row = grid[row_num]
    # print row
    local_max.append(findMaxProductInList(row, size))
  # print local_max
  return max(local_max)

# ----------------------------------------------------------------------------
def findMaxVertProduct(grid, size = 4):
  """
  find the maximum product of size elements in all columns of the grid 
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  local_max = []
  for col_num in xrange(len(grid[0])):
    col = [grid[r][col_num] for r in xrange(len(grid))]
    local_max.append(findMaxProductInList(col, size))
  return max(local_max)

# ----------------------------------------------------------------------------
def transposeToDiamond(grid, direction = 'left'):
  """
  transpose a square grid to a diamond
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  diamond = []
  num_rows = len(grid)
  num_cols = len(grid[0])
  if direction == 'left':
    for x_start in xrange(num_cols-1, -num_cols, -1):
      diamond.append([])
      # print x_start
      for y, x in enumerate(xrange(x_start, num_cols)):
        if x < 0 or x >= num_cols or y < 0 or y >= num_rows: 
          continue
        # print '\tx: %d -- y: %d' % (x, y)
        diamond[-1].append(grid[x][y])
  elif direction == 'right':
    for x_start in xrange(-num_cols+1, num_cols, +1):
      diamond.append([])
      # print x_start
      for y, x in enumerate(xrange(x_start, num_cols)):
        if x < 0 or x >= num_cols or y < 0 or y >= num_rows: 
          continue
        # print '\tx: %d -- y: %d = %d' % (x, y, num_rows-y-1)
        diamond[-1].append(grid[x][num_rows-y-1])
  
  return diamond

# ----------------------------------------------------------------------------
def findMaxDiagProduct(grid, size = 4, direction = 'left'):
  """
  find the maximum product of adjacent number in a down-right line with 
  starting points in row
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # print 'direction: %s' % direction
  # print 'size: %s' % size
  diamond = transposeToDiamond(grid, direction)
  # printGrid(diamond)
  return findMaxHorizProduct(diamond, size)

# ----------------------------------------------------------------------------
def findMaxProduct(in_file_name, size = 4):
  """
  read input rectangle from file, and then find the maximum product of 
  adjacent numbers
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  grid = getNumberGrid(in_file_name)
  print 'Finding max product of %d adjacent digits in: '
  printGrid(grid)

  local_max = []
  local_max.append(findMaxHorizProduct(grid, size))
  local_max.append(findMaxVertProduct(grid, size))
  local_max.append(findMaxDiagProduct(grid, size, 'left'))
  local_max.append(findMaxDiagProduct(grid, size, 'right'))

  print '---------------------------------------------------------------------'
  print 'The maximum product of %s adjacent values is: %d' % (size, max(local_max))

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  findMaxProduct('prob_011_test.in', 4)
  print '====================================================================='
  findMaxProduct('prob_011.in', 4)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 70600674
