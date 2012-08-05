#!/usr/bin/env python
# ============================================================================
import math
import collections
import operator

#  ====================================================
#  = Helper functiones for working with prime numbers =
#  ====================================================

# ----------------------------------------------------------------------------
def isPrime(num):
  """
  Is this number prime?
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  # Special case for 0, 1
  if num == 0 or num == 1:
    return False

  # variables used in checking for primes
  is_prime = True
  max_possible = int(math.sqrt(num)+1)
  test = 2

  # check if num is factorable
  while test < max_possible and is_prime:
    if num % test == 0:
      is_prime = False
    test += 1
  return is_prime

# ----------------------------------------------------------------------------
def isPrime_dumb(num):
  """
  Is this number prime?
  TODO optimize isPrime function!
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  is_prime = True

  # check if num is divisible by all numbers less than it
  i = 2
  while i < num and is_prime:
    if num % i == 0:
      is_prime = False
    i+=1
  return is_prime

# ----------------------------------------------------------------------------
def getNextPrime(last_prime):
  """
  Given last_prime, find the next prime
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  found_next_prime = False
  next_prime = last_prime
  while not found_next_prime:
    next_prime += 1
    if isPrime(next_prime):
      found_next_prime = True
  return next_prime

# ----------------------------------------------------------------------------
def getPrimeSeive(max):
  """
  Get actual prime seive of number less than max
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  primes = [1]*int(max)
  prime_list = []

  for i in xrange(int(max)):
    if i == 0 or i == 1:
      primes[i] = 0
    if primes[i] == 0:
      continue

    prime_list.append(i)
    mults = 2*i
    while mults < max:
      primes[mults] = 0
      mults += i

  return primes


# ----------------------------------------------------------------------------
def primeSeive(max):
  """
  Get list of all primes less than max
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  primes = [1]*int(max)
  prime_list = []

  for i in xrange(int(max)):
    if i == 0 or i == 1:
      primes[i] = 0
    if primes[i] == 0:
      continue

    prime_list.append(i)
    mults = 2*i
    while mults < max:
      primes[mults] = 0
      mults += i

  return prime_list


# ----------------------------------------------------------------------------
def getFirstNPrimes(n):
  """
  Returns a list of the first n prime numbers
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  test = 0
  primes = [2]
  while len(primes) < n:
    primes.append(getNextPrime(primes[-1]))
  return primes

# ----------------------------------------------------------------------------
def getPrimesBelowN(max):
  """
  Returns a list of all primes less than and including max
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  primes = []
  for i in xrange(max+1):
    if isPrime(i):
      primes.append(i)
  return primes

# ----------------------------------------------------------------------------
def getPrimeFactors(num):
  """
  Returns a list of primes factors of num
  """
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0 or num == 1:
    return []

  # If num is prime, you are done! Return right away.
  if isPrime(num):
    return [num]

  factors = []
  found_factor = False
  max_possible = math.sqrt(num)
  prime = 0

  # Loop through possible primes
  while not found_factor and prime < max_possible:
    # get next prime
    prime = getNextPrime(prime)

    # if num is divisible by this prime, set found_factor and look for more
    if num%prime == 0:
      factors.append(prime)
      factors.extend(getPrimeFactors(num/prime))
      found_factor = True

  # if no prime factors found, this should have been prime! something is wrong
  assert(found_factor == True)

  return factors

# ----------------------------------------------------------------------------
def getPrimeFactorsWithSeive(num):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0 or num == 1:
    return []
  if isPrime(num):
    return [num]

  primes_factors = []
  # get all primes up to num
  primes = primeSeive(num)
  for p in primes:
    if num%p == 0:
      primes_factors.append(p)
  return primes_factors

# ----------------------------------------------------------------------------
def getPrimeFactors(num, primes_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0 or num == 1:
    return []

  test_num = num
  prime_factors = []
  for p in primes_list:
    while test_num % p == 0:
      prime_factors.append(p)
      test_num /= p
    if test_num == 1:
      break
  return prime_factors

# ----------------------------------------------------------------------------
def getNumDivisorsFromPrimes(prime_factors):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  num_primes = len(prime_factors)
  num_divisors = 1
  prime_counter = collections.Counter(prime_factors)

  for elt,count in prime_counter.most_common():
    num_divisors *= (count+1)
  return num_divisors

# ----------------------------------------------------------------------------
def getDivisorsFromPrimes(prime_factors, master = True):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  divisors = []
  if len(prime_factors) > 1:
    divisors.append(reduce(operator.mul, prime_factors))
    for i in xrange(len(prime_factors)):
      tmp_list = prime_factors[:i]+prime_factors[i+1:]
      divisors.extend(getDivisorsFromPrimes( prime_factors[:i]
                                           + prime_factors[i+1:]
                                           , False
                                           )
                     )

  if master and len(prime_factors) > 0:
      divisors.append(1)
      divisors.extend(prime_factors)
      divisors = list(set(divisors))
      divisors.sort()
  return divisors

# ----------------------------------------------------------------------------
def getDivisors(num, primes_list):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if num == 0:
    return []
  if num == 1:
    return [1]

  prime_factors = getPrimeFactors(num, primes_list)
  return getDivisorsFromPrimes(prime_factors)

