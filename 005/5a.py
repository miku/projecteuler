#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

LIMIT = 12000000
UPPER = 21

print "The smallest number that can be divided by each of the numbers"
print range(1, UPPER)
print "=>",
try:
	print min(
		reduce(set.intersection, 
			[ set(range(d, LIMIT, d)) for d in range(1, UPPER) ]))
except ValueError:
	print "Not found. Smallest number exceeds", LIMIT