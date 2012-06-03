#!/usr/bin/env python 
# ============================================================================
import sys

#  ===========================================================================
#  = http://projecteuler.net/problem=19                                      =
#  = - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =
#  = How many Sundays fell on the first of the month in the 20th century     =
#  ===========================================================================

# ----------------------------------------------------------------------------
def getDaysInMonth(month, year):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  days = 0
  if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
  if month in [4, 6, 9, 11]:
    days = 30
  if month == 2:
    days = 28
    if year%4 == 0 and (not year%100 == 0 or year%400 == 0):
      days += 1
  return days 

# ----------------------------------------------------------------------------
def getDayOfWeek(day_number):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  return (day_number)%7

# ----------------------------------------------------------------------------
def getYearStartDay(start_year):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  # we know jan 1 1900 was a Monday
  day = 1
  for year in xrange(1900, start_year):
    for month in xrange(1,13):
      day += getDaysInMonth(month, year)
  return day%7

# ----------------------------------------------------------------------------
def getNumOccurancesInTimePeriod( start_year = 1900
                                , end_year = 2000
                                , day = 0
                                ):
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  day_count = getYearStartDay(start_year)
  print 'Jan 1 %d occured on day: %d' % (start_year, day_count)
  num_occurances = 0
  for year in xrange(start_year, end_year+1):
    days_this_year = 0
    annual_occurances = 0
    for month in xrange(1, 13):
      if getDayOfWeek(day_count) == day:
        annual_occurances += 1
        num_occurances += 1
      day_count += getDaysInMonth(month, year)
      days_this_year += getDaysInMonth(month, year)
    print 'In year %d -- total days: %d -- occurances: %d -- total occurances: %d' % ( year
                                                                                     , days_this_year
                                                                                     , annual_occurances
                                                                                     , num_occurances
                                                                                     )
  print 'Day %d occurs %d times between Jan 1 %d - Dec 31 %d' % ( day
                                                                , num_occurances
                                                                , start_year
                                                                , end_year
                                                                )

# ============================================================================
def main():
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
  getNumOccurancesInTimePeriod(1901, 2000, 0)

# ============================================================================
if __name__ == "__main__":
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  sys.exit( main() )

# ============================================================================
#  ============
#  = solution =
#  ============
# 171
