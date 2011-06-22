#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

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

print sum(primes_up_to(2000000))
# => 142913828922