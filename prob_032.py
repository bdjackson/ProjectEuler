#!/usr/bin/env python
# ============================================================================
import sys
import math

# ===========================================================================
# = http://projecteuler.net/problem=32                                      =
# = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
# = find the sum of all products whose multiplicand/multiplier/product can  =
# = be written as 1-9 pandigital                                            =
# ===========================================================================

# -----------------------------------------------------------------------------
def isPandigital(a,b,c):
    sorted_string = ''.join(sorted('%d%d%d' % (a,b,c)))
    return sorted_string == '123456789'

# -----------------------------------------------------------------------------
def isPandigitalProduct(product):
    is_pandigital_product = False
    for a in xrange(2,product/2):
        if not product%a == 0:
            continue
        b = product/a
        is_pandigital_product = isPandigital(a,b,product)
        if is_pandigital_product:
            break
    return is_pandigital_product

# -----------------------------------------------------------------------------
def findSumOfPandigitalProducts():
    sum_of_pandigitals = 0
    # for i in xrange(int(1e8)):
    #     pass
    # I think the product have <= 4 digits because >= 5 digits will require
    # too many digits in multiplicands to be pandigital
    for i in xrange(int(1e4)):
        if isPandigitalProduct(i):
            print 'found pand prod: %d' % i
            sum_of_pandigitals += i

    print 'Sum of pandigital products: %d' % sum_of_pandigitals
    return sum_of_pandigitals

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  print isPandigitalProduct(7254)
  print isPandigitalProduct(7253)
  print isPandigitalProduct(7252)
  print isPandigitalProduct(22)

  findSumOfPandigitalProducts()


# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
# ============
# = solution =
# ============
# Sum of pandigital products: 45228
