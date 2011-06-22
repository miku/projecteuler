#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from operator import mul

def primes_up_to(n): 
	if n == 2:
		return [2]
	elif n < 2:
		return []
	s = range(3, n + 1, 2)
	mroot = n ** 0.5
	half = (n + 1) / 2 - 1
	i, m = 0, 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3) / 2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	return [2] + [x for x in s if x]


def multiple_generator(n=20):
	""" 
	Generate infinite sequence of multiples of n.
	"""
	print "[Stepping] is", n
	i = 0
	while True:
		i += 1
		yield i * n
		
N = 20

numbers = range(1, N + 1)
restricted_numbers = set(numbers) - set(primes_up_to(N))

for x in multiple_generator(n=reduce(mul, primes_up_to(N))):
	found = True
	for y in restricted_numbers:
		if not (x % y == 0):
			# print "%s fails on %s" % (x, y)
			found = False
			break
	if found:
		print "[Smallest number] that is evenly divisible by each",
		print ', '.join(map(str, numbers))
		print "=>",
		print x
		break
